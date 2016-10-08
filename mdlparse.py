import os
import sys
import pfp

datafileName = sys.argv[1].split("\\")[-1].split(".")[0]
os.environ["CYGWIN"]="nodosfilewarning"
mdl = pfp.parse(data_file=sys.argv[1], template_file="mdl.bt", cpp_path=".//cpp//bin//i686-nacl-cpp.exe")
types = mdl._pfp__types._types_map

def process(chunk):
    if not os.path.exists("./%s" % (datafileName)):
        os.mkdir("./%s" % (datafileName))
    if chunk.tag == 'Mesh    ':
        print 'extract  : Mesh'
        i = 0
        for submesh in chunk.meshs._pfp__children:
            if isinstance(submesh,types["MESH"]):
                i = i + 1
                # submesh
                f = open("./%s/mesh-%d.obj" % (datafileName,i),'wb')
                for block in submesh.blocks:
                    f.write("v %f %f %f\r\n" % (block.v1._pfp__value,block.v2._pfp__value,block.v3._pfp__value))
                f.write("g submesh_0\r\n")
                for face in submesh.faces:
                    f.write("f %d %d %d\r\n" % (face.i1._pfp__value + 1,face.i2._pfp__value + 1,face.i3._pfp__value + 1))                  
                f.close()
    elif chunk.tag == 'Texture ':
        print 'extract  : Texture'
        for texture in chunk.textures._pfp__children:
            if isinstance(texture,types["TEXTURE"]):
                # texture
                f = open("./%s/%s.texture" % (datafileName,texture.name2.raw_data.replace(chr(0x0),"")),'wb')
                f.write(texture.data.raw_data)         
                f.close()
    else:
        print 'pass     : %s' % chunk.tag

for chunk in mdl._pfp__children:
    if isinstance(chunk,types["CHUNK"]):
        process(chunk)
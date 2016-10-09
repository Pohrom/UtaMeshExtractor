# Utawarerumono Game Resource Extractor
传颂之物游戏资源提取

## 运行环境
* Windows x86_64 / Python27 
* python-pfp (pip install pfp)

## 测试
* 传颂之物:虚伪的假面 PS3版本 (Texture & Mesh)

## 用法
拖动 mdl 文件到 extract.bat 或执行 ```python mdlparse.py filename.mdl``` 以获得模型(wavefront obj 格式)  
拖动生成的 obj 文件到 mesh_viewer.exe 预览模型

## 信息
### 贴图

* 可以用 TextureFinder 查看
* 宽度512 
* DXT 格式

### SDAT 解密

* 使用 [aniruddh22/make_npdata](https://github.com/aniruddh22/make_npdata) 解包 (此版本 make_npdata 参数处理有点小问题)  
```make_npdata -d filename.sdat filename.dat 0```

### DAT 解包
* DAT/PCK (sig = Filename) 的文件包可以使用 exwatfopck 拆分  
```exwatfopck filename.dat```

### 角色
* ch000 = 哈克
* ch002 = 奥修特尔
* ch003 = 久远
* ch004 = 麻吕
* ch005 = 露露缇耶
* ch006 = 锁之巫女
* ch007 = 锁之巫女
* ch009 = 鵟
* ch010 = 猫音
* ch012 = 裘鲁
* ch013 = 阿图依
* ch014 = 杏树

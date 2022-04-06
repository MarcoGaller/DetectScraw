# 零件检测UI

## 安装虚拟环境
```shell
# cmd 执行
pip install virtualenv
virtualenv venv
"./venv/Scripts/activate" # 激活
"./venv/Scripts/deactivate" # 取消激活
```

## 安装依赖
```shell
pip install -r requirements.txt
```
## 运行
```
python Program.py
```

## ui文件转换
```shell
pyuic5 ui/main.ui -o ui/ui_main.py
```

## 打包程序
```shell
pyinstaller -i cam.ico  --add-data="cam.ico;." --add-data="sound\\*;sound\\" --add-data="config.yml;." --add-data="cameraFunc\models\yolox_nano_components_openvino_2021.4_6shave.blob;cameraFunc\\models\\" --distpath="C:\\OAK_Detection_Scraw" --exclude-module=pyinstaller -y -w Program.py
```
### 参数说明
-i 程序图标 <br>
--add-data 追加打包的资源 <br>
--distpath 打包dist输出路径 <br> 
--exclude-module 打包忽略的依赖 <br>
-w 关闭命令行显示 <br>
-y 交互选择为yes

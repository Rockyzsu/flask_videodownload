# 基于flask的视频下载页面（非常简易！！）



### 效果图
![](http://xximg.30daydo.com/webupload/20221012001.jpg)



### 部署与运行（非常简单！！！）

* 安装flask, gunicorn

  ```
  pip install flask
  
  pip install gunicorn
  ```

  

* 修改配置文件 gunicorn.conf , 

  ```
  bind = "0.0.0.0:18080"
  workers = 4
  backlog = 2048
  pidfile = "log/gunicorn.pid"
  accesslog = "log/access.log"
  errorlog = "log/debug.log"
  timeout = 6000
  debug=False
  capture_output = True
  ```

* 修改配置文件conf.py

  ```
  youget_path ='/home/opc/othergit/you-get/you-get'
  target_folder = '/home/opc/video'
  ```

  youget_path : github上 下载到本地的路径  https://github.com/soimort/you-get

  target_folder : 视频保存的路径

  

* 运行

  ```
  chmod +x start.sh
  ./start.sh
  ```

  


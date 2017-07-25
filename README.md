# DjangoMxOline
Django 1.9 Python 2.7.10+ 环境下建立的网上学院Web项目
首先安装Python2.7.10+
pip install virtualenv 安装沙漏
pip install virtualenvwrapper
初始化

第一次安装完成后需要，先设置一个变量WORKON_HOME，它将作为所有环境的前缀，并且source /usr/local/bin/virtualenvwrapper.sh

$ mkdir -p $WORKON_HOME
$ export WORKON_HOME=~/Envs
$ source /usr/local/bin/virtualenvwrapper.sh
把export命令和source命令，加入到~/.bash_profile，就无需重复初始化了
mkvirtualenv env1创建环境
workon env1进入空间
切换环境

workon env1

workon env2
列出已有环境

workon
退出环境

deactivate
删除环境

rmvirtualenv

安装django 
pip install django==1.9.0(这里指定版本)
创建第一个项目
使用 django-admin.py 来创建 HelloWorld 项目：
django-admin.py startproject HelloWorld
cd HelloWorld/
$ tree
.
|-- HelloWorld
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
接下来我们进入 HelloWorld 目录输入以下命令，启动服务器：
python manage.py runserver 0.0.0.0:8000
0.0.0.0 让其它电脑可连接到开发服务器，8000 为端口号。如果不说明，那么端口号默认为 8000

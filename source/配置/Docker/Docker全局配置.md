# Docker配置

注：可以将vim改为nano

## 国内源配置

1. 修改/etc/docker/daemon.json，没有的话直接新建

   ```bash
   vim /etc/docker/daemon.json
   ```

2. 添加如下配置

   ```json
   {
       "registry-mirrors": [
       "https://2a6bf1988cb6428c877f723ec7530dbc.mirror.swr.myhuaweicloud.com",
       "https://docker.m.daocloud.io",
       "https://hub-mirror.c.163.com",
       "https://mirror.baidubce.com",
       "https://your_preferred_mirror",
       "https://dockerhub.icu",
       "https://docker.registry.cyou",
       "https://docker-cf.registry.cyou",
       "https://dockercf.jsdelivr.fyi",
       "https://docker.jsdelivr.fyi",
       "https://dockertest.jsdelivr.fyi",
       "https://mirror.aliyuncs.com",
       "https://dockerproxy.com",
       "https://mirror.baidubce.com",
       "https://docker.m.daocloud.io",
       "https://docker.nju.edu.cn",
       "https://docker.mirrors.sjtug.sjtu.edu.cn",
       "https://docker.mirrors.ustc.edu.cn",
       "https://mirror.iscas.ac.cn",
       "https://docker.rainbond.cc"
       ]
   }
   ```

3. 重新加载配置文件

   ```bash
   systemctl daemon-reload 
   ```

4. 重启docker服务

   ```bash
   systemctl restart docker
   ```


## 配置用户组

配置用户组是为了让非root用户可以使用docker，非root用户无法直接运行Docker命令的主要原因是权限不足

解决权限不足的方法是将用户添加到具有docker权限的用户组

1. 创建docker用户组
   一般情况下安装docker就会创建docker用户组，如果未创建则执行命令进行创建

   ```bash
   sudo groupadd docker
   ```

2. 将用户添加到docker组

   ```bash
   sudo gpasswd -a $USER docker 
   ```

   这里`$USER`是添加到docker组的用户名

3. 更新用户组

   ```bash
   newgrp docker
   ```

## 验证配置

在终端输入

```bash
docker run hello-world
```

检查是否能运行Docker命令

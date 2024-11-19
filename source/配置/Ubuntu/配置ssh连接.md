# 配置ssh连接

## 配置ssh

1. 安装openssh-server

   ```bash
   sudo apt install openssh-server
   ```

2. 修改ssh配置文件

   ```bash
   vim /etc/ssh/sshd_config
   ```

   注释这一行PermitRootLogin prohibit-password

   添加一行PermitRootLogin yes

   然后保存退出

3. 重启ssh服务

   ```bash
   /etc/init.d/ssh restart
   ```

   
To add in super user group
https://linuxconfig.org/rhel7-user-is-not-in-the-sudoers-file-error


To get super user permission
```
su
```

# To add User name
```
adduser user_name
```
Add User to the Sudo Group[User with root permission can add a user to sudo group]
```
usermod -aG sudo username
```

The command consists of the following components:

usermod command modifies a user account.

-aG is an option that adds the user to a specific group. The -a option adds a user to the group. It does that without removing them from the current groups. The -G option is used to state where to add the existing user.

sudo is the group that is appended to the options mentioned above.

username is the user account you want to add to the sudo group.

#Verify the new Debian sudo user is added to the group with the command:
```
getent group sudo
```
mYSQL wRONG PASSWORD

https://stackoverflow.com/questions/50995864/mysql-set-root-password-wrong

# STOP my sql service
```
service mysql stop
```

start msql server without password
```
mysqld_safe --skip-grant-tables &
```

Connect to the MySQL server using the MySQL client:
```
mysql -u root
```

Set a new MySQL root user password:
```
mysql> use mysql;
mysql> update user set password=PASSWORD("NEW-ROOT-PASSWORD") where User='root';
mysql> flush privileges;
mysql> quit
```

# MySQL 5.7.6 and newer
```
mysql> use mysql;
mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD("newpass");
mysql> flush privileges;
mysql> quit
```
Stop the MySQL server:
```
service mysql stop
```
Output:

Stopping MySQL database server: mysqld
STOPPING server from pid file /var/run/mysqld/mysqld.pid
mysqld_safe[6186]: ended

[1]+  Done                    mysqld_safe --skip-grant-tables

To start service
```
sudo service mysql start
```
mysql runs with configitation based files on linux
```
sudo mysql --defaults-file=/etc/mysql/debian.cnf
```

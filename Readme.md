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

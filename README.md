# ldmauth
log into lightdm with alternative login methods such as usblogin

## configuration
if a program specified in /etc/ldmauth.conf exits sucessfully for an user, the user gets access without a password.

example config:

`usblogin verify $username`

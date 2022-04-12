# ldmauth
log into lightdm with alternative login methods such as usblogin and bluetoothlogin

## configuration
if a program specified in /etc/ldmauth.conf exits sucessfully for an user, the user gets access without a password. The program is required to utilize $username.

example config:

```usblogin verify $username
bluetoothlogin verify $username```

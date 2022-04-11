#!/bin/bash
sudo cp /etc/pam.d/lightdm /etc/pam.d/lightdm.before-ldmauth
sudo bash -c 'echo "#%PAM-1.0
auth        sufficient  pam_succeed_if.so user ingroup nopasswdlogin
auth        include     system-login
-auth       optional    pam_gnome_keyring.so
account     include     system-login
password    include     system-login
session     include     system-login
-session    optional    pam_gnome_keyring.so auto_start" > /etc/pam.d/lightdm'

sudo cp src/main.py /bin/ldmauthd
sudo cp src/ldmauth.service /etc/systemd/system/ldmauth.service
sudo systemctl enable ldmauth
sudo touch /etc/ldmauth.conf
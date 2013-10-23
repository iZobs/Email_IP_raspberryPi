#use
in raspberry pi which runing Raspbian
$ git glone https://github.com/iZobs/Email_IP_raspberryPi.git
$ sudo vim /ect/rc.local :
---------------------------------------
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP"  ]; then
  printf "My IP address is %s\n" "$_IP"
+ python /home/pi/python/emailIP.py
    fi

exit 0


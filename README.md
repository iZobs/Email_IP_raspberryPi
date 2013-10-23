#use
in raspberry pi which runing Raspbian
$ git glone https://github.com/iZobs/Email_IP_raspberryPi.git

$ sudo vim /ect/rc.localadd this "python /home/pi/python/emailIP.py"

_IP=$(hostname -I) || true
if [ "$_IP"  ]; then
  printf "My IP address is %s\n" "$_IP"
+ python /home/pi/python/emailIP.py
    fi

exit 0


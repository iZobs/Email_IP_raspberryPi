#USE
***
in raspberry pi which runing Raspbian:

    $git glone https://github.com/iZobs/Email_IP_raspberryPi.git

    $sudo vim /ect/rc.local add this "python /home/pi/python/emailIP.py"
- - -
**/ect.rc.local**
- - -

    _IP=$(hostname -I) || true
    if [ "$_IP"  ]; then
        printf "My IP address is %s\n" "$_IP"
        python /home/pi/python/emailIP.py

    fi
    exit 0


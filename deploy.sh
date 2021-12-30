scp -r . pi@192.168.72.20:/usr/apps/tv-api/
ssh pi@192.168.72.20 "sudo systemctl restart tv-api.service"
sleep 2
ssh pi@192.168.72.20 "sudo systemctl status tv-api.service"

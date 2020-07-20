echo 'start Application Server'
server_state=false
server_name=server1
cd /opt/IBM/WebSphere/AppServer/profiles/AppSrv05/bin/
sudo ./startServer.sh $server_name -user test -password test || echo 'server has already staterd'
echo 'started server: ' + $server_name
server_state=true

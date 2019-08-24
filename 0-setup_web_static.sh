#!/usr/bin/env bash
# script to isntall a create a nginx
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
touch /data/web_static/releases/test/index.html
echo -e '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' | tee -a '/data/web_static/releases/test/index.html'
ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '29i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/hbnb_static/;\n\t\tautoindex off;\n\t}' /etc/nginx/sites-available/default
sudo service nginx reload
sudo service nginx restart

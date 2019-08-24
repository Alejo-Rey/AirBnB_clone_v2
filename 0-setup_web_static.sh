#!/usr/bin/env bash
# script to isntall a create a nginx
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
sudo touch /data/web_static/releases/test/index.html
echo -e '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' | sudo tee '/data/web_static/releases/test/index.html'
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '29i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/hbnb_static/;\n\t}' /etc/nginx/sites-enabled/default
sudo service nginx reload
sudo service nginx restart

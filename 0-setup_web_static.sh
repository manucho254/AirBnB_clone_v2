#!/usr/bin/env bash
# file that setups all directories in server

sudo apt-get -y update && sudo apt-get -y upgrade
sudo apt-get install nginx
sudo service nginx start

# create all directories
sudo mkdir /data
sudo mkdir /data/web_static
sudo mkdir /data/web_static/shared
sudo mkdir /data/web_static/current
sudo mkdir /data/web_static/releases
sudo mkdir /data/web_static/releases/test

# create a fake html file
echo "
<html>
    <head>
    </head>
    <body>
          Holberton School
    </body>
</html>" | sudo tee data/web_static/current/index.html

#change owner and group of path /data/ and all subpaths
sudo chown -R ubuntu:ubuntu /data/

# create a symbolic link
sudo ln -fs /data/web_static/current data/web_static/releases/test

#change default file
echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                   # First attempt to serve request as file, then
                   # as directory, then fall back to displaying a 404.
                   try_files \$uri \$uri/ =404;
        }
        
        location /hbnb_static {
                 # serve content in /data/web_static/current/;
                 alias /data/web_static/current/;
        }
}" | sudo tee /etc/nginix/sites-available/default /etc/nginx/sites-enabled/default

# restart nginx
sudo service nginx restart

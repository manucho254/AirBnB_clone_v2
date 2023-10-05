#!/usr/bin/env bash
# file that setups all directories in server

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install nginx

# create all directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# create a fake html file
echo "Holberton Shchool" | sudo tee "/data/web_static/releases/test/index.html"

source_path="/data/web_static/releases/test/"
target_link="/data/web_static/current"

# create a symbolic link
sudo ln -sf "$source_path" "$target_link"

#change owner and group of path /data/ and all subpaths
sudo chown -R ubuntu:ubuntu /data/

#change default file
echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        add_header X-Served-By \$hostname;

        # 404 error
        error_page 404 /error404.html;

        location / {
                   # First attempt to serve request as file, then
                   # as directory, then fall back to displaying a 404.
                   try_files \$uri \$uri/ =404;
        }
        
        location /redirect_me {
                  return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
        
        location /hbnb_static {
                 # serve content in /data/web_static/current/;
                 alias /data/web_static/current/;
        }
}" | sudo tee /etc/nginx/sites-available/default

sudo cp -f /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

# restart nginx
sudo service nginx restart

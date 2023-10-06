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

my_alias="location /hbnb_static { alias /data/web_static/current/;}"
#change default file
sed -i "s/server _;/server _;\n$my_alias" /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart

#!/usr/bin/env bash
# file that setups all directories in server

sudo killall apache2
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install nginx -y

# start nginx service
sudo service nginx start

# create all directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# create a fake html file
touch index.html
echo "Holberton Shchool" > index.html
sudo mv index.html /data/web_static/releases/test/

source_path="/data/web_static/releases/test"
target_link="/data/web_static/current"

# remove symbolic link
sudo rm -rf "$target_link"

# create a symbolic link
sudo ln -s "$source_path" "$target_link"

#change owner and group of path /data/ and all subpaths
sudo chown -R ubuntu:ubuntu /data/

# delete default files
sudo rm -rf /etc/nginx/sites-available/default
sudo rm -rf /etc/nginx/sites-enabled/default

#create default file
touch default

echo "
server {
        listen 80 default_server;
	listen [::]:80 default_server;
	
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	
	server_name _;

	location /hbnb_static {
	         alias /data/web_static/current/;
	}

        # 404 error file
	error_page 404 /error404.html;

	location / {
		 # First attempt to serve request as file, then
		 # as directory, then fall back to displaying a 404.
		 try_files \$uri \$uri/ =404;
	}

	location /redirect_me {
	        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}
}" > default

sudo mv default /etc/nginx/sites-available/default
sudo cp -r /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

# restart nginx
sudo service nginx reload

# file that setups all directories in server

exec { 'Kill apache2 process':
    command => 'sudo killall apache2',
    path    => ['/usr/bin', '/usr/sbin',],
}

exec { 'Update and upgrade os':
    command => 'sudo apt-get update -y && sudo apt-get upgrade -y',
    path    => ['/usr/bin', '/usr/sbin',],
}

exec { 'Install nginx':
    command => 'sudo apt-get install nginx -y',
    path    => ['/usr/bin', '/usr/sbin',],
}

exec { 'start nginx service':
    command => 'sudo service nginx start',
    path    => ['/usr/bin', '/usr/sbin',],
}

exec { 'create all directories':
    command => 'sudo mkdir -p /data/web_static/releases/test /data/web_static/shared',
    path    => ['/usr/bin', '/usr/sbin',],
}

exec { 'create html file':
    command => 'touch index.html',
    path    => ['/usr/bin', '/usr/sbin',],
}
exec { 'add data to index file':
    command => 'echo "Holberton Shchool" > index.html',
    path    => ['/usr/bin', '/usr/sbin',],
}
exec { 'move html file':
    command => 'sudo mv index.html /data/web_static/releases/test/',
    path    => ['/usr/bin', '/usr/sbin',],
}

$source_path='/data/web_static/releases/test'
$target_link='/data/web_static/current'

exec { 'remove symbolic link':
    command => "sudo rm -rf ${target_link}",
    path    => ['/usr/bin', '/usr/sbin',],
}

exec { 'create a symbolic link':
    command => "sudo ln -s ${source_path} ${target_link}",
    path    => ['/usr/bin', '/usr/sbin',],
}

exec { 'change owner and group of path /data/ and all subpaths':
    command => 'sudo chown -R ubuntu:ubuntu /data/',
    path    => ['/usr/bin', '/usr/sbin',],
}

exec { 'delete /etc/nginx/sites-available/default':
    command => 'sudo rm -rf /etc/nginx/sites-available/default',
    path    => ['/usr/bin', '/usr/sbin',],
}
exec { 'delete /etc/nginx/sites-enabled/default':
    command => 'sudo rm -rf /etc/nginx/sites-enabled/default',
    path    => ['/usr/bin', '/usr/sbin',],
}

exec { 'create default file':
    command => 'touch default',
    path    => ['/usr/bin', '/usr/sbin',],
}

file { '/etc/nginx/sites-available/default':
    ensure  => present,
    path    => '/etc/nginx/sites-available/default',
    content =>
'server {
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
}
',
}

exec {'copy sites-available/default to sites-enabled/default':
    command => 'sudo cp -r /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default',
    path    => ['/usr/bin', '/usr/sbin',],
}

exec { 'restart nginx':
    command => 'sudo service nginx reload',
    path    => ['/usr/bin', '/usr/sbin',],
}

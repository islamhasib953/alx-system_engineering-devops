# Configure a server

exec { 'update':
  command => 'apt-get update',
  path    => '/usr/bin',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => 'Hello World!',
}

exec { 'redirect':
  command => "sed -i '/server_name _;/a \\n\tlocation /redirect_me {\n\t\treturn 301 https://x.com/islamhasib953;\n\t}' /etc/nginx/sites-available/default",
  path    => '/usr/bin',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

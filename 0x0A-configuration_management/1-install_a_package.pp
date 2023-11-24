# installing flask
package { 'python3-pip':
ensure  => 'installed'
}
exec { 'werkzeug':
command => '/usr/bin/pip3 install Werkzeug==2.0,2'.
path    => ['/usr/bin'],
require => Package['python3-pip'],
}
exec { 'install flask':
command => '/usr/bin/pip3 install flask==2.1.0',
path    => ['/usr/bin'],
unless  => 'pip3 show flask | grep -q "Version: 2.1.0"',
require => [Package['python3-pipi'], Exec['werkzeug']],
}

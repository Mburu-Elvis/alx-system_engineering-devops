# installing flask
package { 'python3-pip':
ensure  => 'installed',
}
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => '/usr/bin',
  require => Package['python3-pip'],
}
exec { 'check_flask_version':
  command     => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  path        => '/usr/bin',
  refreshonly => true,
  subscribe   => Exec['install_flask'],
}

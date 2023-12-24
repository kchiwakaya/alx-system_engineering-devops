# install flask
package { 'python3-pip':
  ensure => present,  # Ensure pip3 is installed
}



package { 'flask':
  ensure   => '2.1.0',  # Specify exact version
  provider => 'pip3',   # Use pip3 for installation
  require  => Package['python3-pip'],  # Ensure pip3 is installed first
}

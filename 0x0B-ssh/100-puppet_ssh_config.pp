#!/usr/bin/env bash
# Seting up my client config file

file {'etc/ssh/ssh_config':
ensure => present,
content =>"
	#SSH client configuration
	host*
	IdentityFle ~/.ssh/school
}
include stdlib

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Delare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '     IdentityFile ~/.ssh/school',
  replace => true,
}

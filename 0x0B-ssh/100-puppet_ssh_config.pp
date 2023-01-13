# setting up client SSH config file
include stdlib

file_line { 'Turn off passwd auth':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
    replace => true,
}

file_line { 'Turn off passwd auth':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => '   IdentifyFile ~/.ssh/school',
    replace => true,
}

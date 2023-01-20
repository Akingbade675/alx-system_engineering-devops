# setting up client SSH config file
file_line { 'Turn off passwd auth':
    ensure  => 'present',
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
}

file_line { 'Turn off passwd auth':
    ensure  => 'present',
    path    => '/etc/ssh/ssh_config',
    line    => '   IdentifyFile ~/.ssh/school',
}

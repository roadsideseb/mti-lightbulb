# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "precise64"

  # port for POSTGRESQL database
  config.vm.network :forwarded_port, guest: 5432, host: 9932
  # port for MySQL database server
  config.vm.network :forwarded_port, guest: 3306, host: 9906

  ## For masterless, mount your salt file root
  config.vm.synced_folder "salt/", "/srv/"

  ## Use all the defaults:
  config.vm.provision :salt do |salt|
    salt.minion_config = "salt/minion"
    salt.run_highstate = true
    salt.verbose = true
  end
end

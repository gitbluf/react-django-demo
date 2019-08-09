#!/usr/bin/env ruby

PROVIDER = :virtualbox
IMAGE= "ubuntu/xenial64"
PROVISONER = :shell

$script = <<-SCRIPT

mkdir -p /home/vagrant/Documents/code

sudo apt-get update

sudo apt-get install -y build-essential libssl-dev

# JS crap

sudo apt-get install curl python-software-properties

sudo curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -

curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

sudo apt-get update -y

sudo apt-get install -y nodejs \
     yarn \
     npm

sudo curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt-get install -y apt-transport-https
sudo apt-get update -y
sudo apt-get install -y code

sudo apt-get install -y \
apt-transport-https \
ca-certificates \
curl \
gnupg-agent \
software-properties-common

sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update -y

sudo apt-get install -y docker-ce \
     docker-ce-cli \
     containerd.io \
     docker-compose

groupadd docker

usermod -aG docker vagrant

sudo apt install -y git

sudo apt-get install -y git \
     virtualbox-guest-dkms \
     virtualbox-guest-utils\
     virtualbox-guest-x11 \
     xserver-xorg-legacy

VBoxClient-all

sudo apt-get install -y --no-install-recommends lubuntu-desktop

sudo reboot -h now

SCRIPT


Vagrant.configure("2") do |config|
  config.ssh.insert_key = false

  config.vm.define "dev" do |dev|
    dev.vm.box = IMAGE
    dev.vm.hostname = "devbox.com"
    dev.vm.network "private_network", ip: "192.168.50.15"
    #dev.vm.synced_folder "./", "/home/vagrant/code"
    dev.vm.provider PROVIDER do |vbc|
      vbc.gui = true
      vbc.customize ["modifyvm", :id, "--memory", "4096"]
      vbc.customize ["modifyvm", :id, "--cpus", "2"]
    end
    dev.vm.provision PROVISONER, inline: $script, privileged: false
  end
end

# for ubuntu 14.04

export LC_ALL=C
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y
sudo apt-get install build-essential -y
sudo apt-get install cowsay mongodb python-dev python-pip pdf2svg libxml2-dev libxslt1-dev python-lxml libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk libreoffice
sudo pip install pymongo
# for python 0.4.2, i had problems with 0.5.1
sudo pip install -Iv https://pypi.python.org/packages/source/p/python-pptx/python-pptx-0.4.2.tar.gz

cowsay "that should work! now install your slides to the slides/ directory and convert them with sweep.sh 

also need reboot!"
# peace out
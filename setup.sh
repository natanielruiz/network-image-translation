sudo apt-get update
sudo apt install git-all
git clone https://github.com/natanielruiz/network-image-translation.git
sudo mv sites-available/* /etc/apache2/sites-available/.
sudo mv www/* /var/www/.
sudo apt-get install apache2
sudo service apache2 restart
sudo apt-get install python3.6
sudo apt install python3-pip
pip3 install virtualenv
cd /var/www
python3 -m venv myVM3.6
source myVM3.6/bin/activate
sudo chmod _R 777 myVM3.6
pip3 install tensorflow, scipi, moviepy, imageio, ffmpeg, cgi-tools
sudo chmod -R 777 style-image
sudo chmod -R 777 out_images

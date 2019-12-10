# network-image-translation
Image translation on a webpage using a server-client architecture on a GENI slice.

To reproduce:

0. Create a slice on GENI and ssh into the server.

1. Clone repo.
2. ```sudo mv sites-available/* /etc/apache2/sites-available/.```
3. ```sudo mv www/* /var/www/.```
4. Download checkpoints to folder "/var/www/checkpoints" from here: https://drive.google.com/drive/folders/0B9jhaT37ydSyRk9UX0wwX3BpMzQ
5. ```sudo apt-get update```
6. ```sudo apt-get install apache2```
7. ```sudo service apache2 restart```
8. ```sudo apt-get install python3.6```
9. ```sudo apt install python3-pip```
10. ```pip3 install virtualenv```
11. ```cd /var/www```
12. ```python3 -m venv myVM3.6```
13. ```source myVM3.6/bin/activate```
14. ```sudo chmod _R 777 myVM3.6```
15. ```pip3 install tensorflow, scipi, moviepy, imageio, ffmpeg, cgi-tools```
16. ```sudo chmod -R 777 style-image```
17. ```sudo chmod -R 777 out_images```

The server is online and ready to go.

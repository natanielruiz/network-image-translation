# network-image-translation
Image translation on a webpage using a server-client architecture on a GENI slice.

<p float="left">
<img src="images/hassan.jpg" width="200"/>
<img src="images/la_muse.jpg" height="258"/>
<img src="images/hassan_translated.jpg" width="200"/>
</p>

<p float="left">
<img src="images/dina.jpg" width="200">
<img src="images/scream.jpg" height="200">
<img src="images/dina_translated.jpg" width="200">
</p>

<p float="left">
<img src="images/nataniel.png" width="200">
<img src="images/wave.jpg" height="200">
<img src="images/nataniel_translated.png" width="200">
</p>

To reproduce:

0. Create a slice on GENI using the 'rspec' file and ssh into the server.
1. ```sudo apt install git-all```
2. Clone repo.
3. ```sudo mv sites-available/* /etc/apache2/sites-available/.```
4. ```sudo mv www/* /var/www/.```
5. Download checkpoints to folder "/var/www/checkpoints" from here: https://drive.google.com/drive/folders/0B9jhaT37ydSyRk9UX0wwX3BpMzQ
6. ```sudo apt-get update```
7. ```sudo apt-get install apache2```
8. ```sudo service apache2 restart```
9. ```sudo apt-get install python3.6```
10. ```sudo apt install python3-pip```
11. ```pip3 install virtualenv```
12. ```cd /var/www```
13. ```python3 -m venv myVM3.6```
14. ```source myVM3.6/bin/activate```
15. ```sudo chmod _R 777 myVM3.6```
16. ```pip3 install tensorflow, scipi, moviepy, imageio, ffmpeg, cgi-tools```
17. ```sudo chmod -R 777 style-image```
18. ```sudo chmod -R 777 out_images```

The server is online and ready to go.

You can also use the setup.sh script.

To use:

1. Navigate to http://192.12.245.162/hello.py on your web browser.
2. Click on 'Choose File'
3. Select a .png or .jpg image from your computer.
4. Click on 'Upload'

[Demo Video](https://youtu.be/XAjBHadoKOg)

The system will randomly select one of our style images. It will then present your original input, the style image used as well as the resulting stylized image which contains your original content with the style of the style image.

Enjoy!

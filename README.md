# network-image-translation
Image translation on a webpage using a server-client architecture on a GENI slice.

<img src="images/hassan.jpg" width="300">

![Hassan](images/hassan.jpg?raw=true "Hassan"){:height="50%" width="50%"}
![La Muse](images/la_muse.jpg?raw=true "La Muse"){:height="50%" width="50%"}
![Translated Hassan](images/hassan_translated.jpg?raw=true "Translated Hassan"){:height="50%" width="50%"}

![Dina](images/dina.jpg?raw=true "Dina"){:height="50%" width="50%"}
![Scream](images/scream.jpg?raw=true "Scream"){:height="50%" width="50%"}
![Translated Dina](images/dina_translated.jpg?raw=true "Translated Dina"){:height="50%" width="50%"}

![Nataniel](images/nataniel.png?raw=true "Nataniel"){:height="50%" width="50%"}
![Wave](images/wave.jpg?raw=true "Wave"){:height="50%" width="50%"}
![Translated Nataniel](images/nataniel_translated.png?raw=true "Translated Nataniel"){:height="50%" width="50%"}


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

To use:

1. Navigate to http://192.12.245.162/hello.py on your web browser.
2. Click on 'Choose File'
3. Select a .png or .jpg image from your computer.
4. Click on 'Upload'

The system will randomly select one of our style images. It will then present your original input, the style image used as well as the resulting stylized image which contains your original content with the style of the style image.

Enjoy!

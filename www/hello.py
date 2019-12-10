#! /var/www/myVM3.6/bin/python

#print ("Content-type: text/html\r\n\r\n")
import cgi
import cgitb; cgitb.enable()
import os
import datetime
import sys
sys.path.append('/users/hsaadi13/.local/lib/python3.6/site-packages')
print ("Content-type: text/html\r\n\r\n")
import server_transfer
print ("<html>")
print ("<head><title>My First CGI Program</title></head>")
print ("<body>")
print ("<p> In this webpage you can upload an image. Then the server will send back the same image but with a style transformation.</p>")

def is_jpg_png(filename):
    im = filename.split(".")
    if im[-1]=='jpg' or im[-1]=='png':
        return True
    else:
        return False

form = cgi.FieldStorage()
if "file" in form:
    fileitem = form["file"]
    if is_jpg_png(fileitem.filename):
        ipadd = cgi.escape(os.environ["REMOTE_ADDR"])
        date = datetime.datetime.now()
        f = open('images/'+ipadd+"_"+str(date)+"_"+fileitem.filename, "wb")
        f.write(fileitem.file.read())
        print("<p>This is the orginal image:</p>")
        print ('''<img src="images/{0}_{1}_{2}" width=500 height=600> '''.format(ipadd,str(date),fileitem.filename))
        input_file_path= "/var/www/images/"+ipadd+"_"+str(date)+"_"+fileitem.filename
        output_image, style_image = server_transfer.stransfer_from_file(input_file_path)
        out_list = output_image.split('/')[3:]
        out_path = '/'.join(out_list)
        style_list = style_image.split('/')[3:]
        style_path = '/'.join(style_list)
        print("<p>This is the style image:</p>")
        print('''<img src="{0}" width=500 height=600> '''.format(style_path))
        print("<p>This is the output image:</p>")
        print('''<img src="{0}" width=500 height=600> '''.format(out_path))
        
        f.close()
    else:
        print ("<p> The image should be in jpg or png format small letters.</p>")



print ('<form enctype="multipart/form-data" method="post">')
print ('<p>Image: <input type="file" name="file"/></p>')
print ('<input type="submit" value="Upload" />')
print ("</form>")
print ("</body>")
print ("</html>")

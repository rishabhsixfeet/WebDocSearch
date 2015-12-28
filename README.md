# WebDocSearch

### Requirements 

* Install textract 
apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac lame libmad0 libsox-fmt-mp3 sox

pip install textract


* install Xapian
On Fedora 11, the easiest way to install Xapian is through the graphical interface. Go to System > Administration > Add/Remove Software and search for xapian. Make sure to install both the core libraries and their Python bindings: xapian-core-libs, xapian-bindings-python.

similarly  on ubuntu  you can search for Xapian  on software center 

using commandline 

$yum install xapian-core-libs xapian-bindings-python



* Install Pylons 
pip install Pylons


### Deploying on local host 

$cd WebDocSearch/demo

WebDocSearch/demo$ paster serve --reload development.ini

on your browser go to 
http://127.0.0.1:5000/



## ABout 
Workspace/data    contains   all the data  files in formats like pdf csv docx txt  jpg gif png 


* screenshot1
![Screen shot](https://raw.githubusercontent.com/rishabhsixfeet/WebDocSearch/master/Screenshot2.png)

* screenshot2
![Screen shot 2](https://github.com/rishabhsixfeet/WebDocSearch/blob/master/Screenshot%20from1.png)









 

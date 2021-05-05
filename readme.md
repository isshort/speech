Sorry about the inappropriate answer last time, I will post the solution of the question. It might be helpful for Ubuntu distributions.

First we need to install portaudio modules: 
    
    $ sudo apt-get install libasound-dev

Download the portaudio archive from: http://files.portaudio.com/download.html

Unzip the archive: 
        
    $ tar -zxvf [portaudio.tgz]

Enter the directory, then run: 
    
    $ ./configure && make

Install: 
    
    $ sudo make install

And finally:

    $ sudo pip install pyaudio

Check the version of pyaudio, it should be 0.2.9
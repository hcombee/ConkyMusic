# ConkyMusic

Script to take currently playing track information from your mediaplayer by using dbus.
This script works for me with Clementine and Spotify. It requires the python3 dbus and mpris2 modules to be installed.
The coverimage is either downloaded from for example Spotify or copied from Clementine which puts the album art in a file named "/tmp/clementine-art-xxxxxx.jpg"

It takes the following command line arguments:

-a      Artist

-t      Track title

-A      Album

-c      Cover file location

-r      Album Artist


Conky example:

${image /tmp/cover.jpg -p 0,0 -s 220x220 -n}

${execi 5 python3 /home/hans/conky/scripts/ConkyMusic.py -a}

${execi 5 python3 /home/hans/conky/scripts/ConkyMusic.py -t}

${execi 5 python3 /home/hans/conky/scripts/ConkyMusic.py -A}





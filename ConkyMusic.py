#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# ConkyMusic.py
# Retrieves playing media information from dBus
# Tested on Ubuntu with Clemetine and Spotify
# Depends on python3 dbus and mpris2 for Python3
#  

import dbus
import os
import shutil
import urllib.request
import filecmp
from mpris2 import Player, get_players_uri

cover_file = '/tmp/cover.jpg'

def main(args):
	artist = ''
	title = ''
	album = ''
	img_name = ''
	arturl = ''

	try:
		player_uri = next(get_players_uri())
		player = Player(dbus_interface_info={'dbus_uri': player_uri})
		for x in player.Metadata:
#			for debugging, uncomment next line
#			print(x,' - ',player.Metadata[x])
			if 'albumArtist' in x:
				albumArtist = player.Metadata[x][0]
			elif 'artist' in x:
				artist = player.Metadata[x][0]
			elif 'title' in x:
				title = player.Metadata[x]
			elif 'album' in x:
				album = player.Metadata[x]
			elif 'artUrl' in x:
				arturl = player.Metadata[x]
				if 'http' in arturl:
					img_name = "/tmp/"+arturl.rsplit('/',1)[1]+".jpg"
					exists = os.path.isfile(img_name)
					if not exists:
						urllib.request.urlretrieve(arturl,img_name)
						shutil.copyfile(img_name,cover_file)
				elif 'file' in arturl:
					img_name = arturl[7:]
					exists = os.path.isfile(img_name)
					same = filecmp.cmp(img_name,cover_file,shallow=True)
					if exists and not same:
						shutil.copyfile(img_name,cover_file)
		if '-a' in args:
			print(artist)
		elif '-t' in args:
			print(title)
		elif '-A' in args:
			print(album)
		elif '-c' in args:
			print(img_name)	
			print("(Is copied to",cover_file,"on each run if they are not equal)")
		elif '-r' in args:
			print(albumArtist)
		else:
			print("No arguments given")
			print(" ")
			print("-a	Song Artist")
			print("-t	Track title")
			print("-A	Album")
			print("-c	Cover file location")
			print("-r	Album Artist")
			
	except StopIteration:
#		print("no player")
		exists = os.path.isfile(cover_file)
#		print(exists)
		if exists:
			os.remove(cover_file)
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
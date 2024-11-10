import subprocess
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dirsync import sync


debug = 1

extention = ".mp3"

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKBLUE + "                    __                           " + bcolors.ENDC)
print(bcolors.OKBLUE + ".-----.--.--.---.-.|  |_.--.--.-----.-----.-----." + bcolors.ENDC)
print(bcolors.OKBLUE + "|     |  |  |  _  ||   _|  |  |     |  -__|__ --|" + bcolors.ENDC)
print(bcolors.OKBLUE + "|__|__|___  |___._||____|_____|__|__|_____|_____|" + bcolors.ENDC)
print(bcolors.OKBLUE + "      |_____|                                    " + bcolors.ENDC)
print()
print(bcolors.OKBLUE + "Enter a media link or leave empty to choose media to sync" + bcolors.ENDC)
print(bcolors.OKBLUE + "URL:" + bcolors.ENDC)
url = str(input())


if "playlist" in url:
    urltype = "playlist"
    coname = sp.playlist(url)
    print(bcolors.OKBLUE+"Downloading "+bcolors.BOLD +coname["name"]+bcolors.ENDC+ bcolors.OKBLUE +" by "+bcolors.BOLD +coname["owner"] ["display_name"]+bcolors.ENDC)
if "track" in url:
    urltype = "track"
    coname = sp.track(url)
    print(bcolors.OKBLUE+"Downloading "+bcolors.BOLD +coname["name"]+bcolors.ENDC+ bcolors.OKBLUE +" by "+bcolors.BOLD +coname["artists"] [0] ["name"]+bcolors.ENDC)
    if debug == 1:
        print("paths:")
        print(bcolors.WARNING+coname["artists"] [0] ["name"]+"/"+coname["album"] ["name"]+"/"+ coname["name"] + extention +bcolors.ENDC)
if "album" in url:
    urltype = "album"
    coname = sp.album(url)
    print(bcolors.OKBLUE+"Downloading "+bcolors.BOLD +coname["name"]+bcolors.ENDC+ bcolors.OKBLUE +" by "+bcolors.BOLD +coname["artists"] [0] ["name"]+bcolors.ENDC)
    if debug == 1:
        print("paths:")
        print(bcolors.WARNING+coname["artists"] [0] ["name"]+"/"+coname["name"]+"/"+ bcolors.ENDC)


if urltype == "playlist":
    subprocess.run(['spotdl', 'download', url, '--output', '{artist}/{album}/{artist} - {title}', '--m3u', '{list[0]}' ])
else:
    subprocess.run(['spotdl', 'download', url, '--output', '{artist}/{album}/{artist} - {title}'])

print(bcolors.OKBLUE + "Sync to: " + bcolors.ENDC)
print(bcolors.BOLD + "    1) mnux's iPhone" + bcolors.ENDC)
print(bcolors.OKBLUE + "    r) refresh list " + bcolors.ENDC)
print(bcolors.OKBLUE + "    s) skip sync " + bcolors.ENDC)
print(bcolors.OKBLUE + "    d) debug folder " + bcolors.ENDC)
path = str(input())

if path == d:
    print(bcolors.WARNING+"uploading downloaded media to /test/"+ bcolors.ENDC)





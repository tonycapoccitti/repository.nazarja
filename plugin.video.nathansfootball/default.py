# -*- coding: utf-8 -*-
#----------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Nathans Football
# Author: Nazarja

#----------------------------------------------------------------

import os           # access operating system commands
import xbmc         # the base xbmc functions, pretty much every add-on is going to need at least one function from here
import xbmcaddon    # pull addon specific information such as settings, id, fanart etc.
import xbmcplugin   # contains functions required for creating directory structure style add-ons (plugins)



from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File

#------------------------------------------------------------

debug        = Addon_Setting(setting='debug')       # Grab the setting of our debug mode in add-on settings
addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id


# Set the base plugin url you want to hook into
BASE = "plugin://plugin.video.youtube/user/"
BASE2 = "plugin://plugin.video.youtube/channel/"
BASE3  = "plugin://plugin.video.youtube/playlist/"

# Set each of your YouTube playlist id's
YOUTUBE_USER_ID_1 = "fcbarcelona"
YOUTUBE_USER_ID_2 = "ArsenalTour"
YOUTUBE_USER_ID_3 = "TheFootballDaily"
YOUTUBE_USER_ID_4 = "laliga"
YOUTUBE_USER_ID_5 = "MessiMagicHD"
YOUTUBE_USER_ID_6 = "talkSPORTmagazine"
YOUTUBE_CHANNEL_ID_1 = "UCRZWRoz1qWWtJLxb9VA4RPA"
YOUTUBE_CHANNEL_ID_2 = "UCmL2k3-xrYZkEkbYOlq-uaA"
YOUTUBE_CHANNEL_ID_3 = "UCpFzEPRtO9-ZwhkpdyTq3jg"
YOUTUBE_PLAYLIST_ID_1 = "PLkksCTsYZQhFI3Niv9mtpEiRX6XZDy6El"
YOUTUBE_PLAYLIST_ID_2 = "PLFVMnSsi_04LeBlsoCHPJABo_79NiYOGq"
YOUTUBE_PLAYLIST_ID_3 = "PLN51oDuC-EcxQw6jb7vgrslB4pp42xwVu"


#----------------------------------------------------------------
# This is the main menu we open into
@route(mode='main_menu')
def Main_Menu():

# If debug mode is enabled show the koding tutorials
    if debug == 'true':
        Add_Dir ( '[COLOR=lime]Koding Tutorials[/COLOR]', '', "tutorials", True, '', '', '' )

    Add_Dir( 
        name="FC Barcelona Videos and Playlists", url=BASE+YOUTUBE_USER_ID_1+"/", folder=True,
        icon="https://yt3.ggpht.com/-cbuwcRBtVFE/AAAAAAAAAAI/AAAAAAAAAAA/Cd4EmB0AO6E/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")       
    
    Add_Dir( 
        name="Arsenal FC Videos and Playlists", url=BASE+YOUTUBE_USER_ID_2+"/", folder=True,
        icon="https://yt3.ggpht.com/-dZ2LhrpNpxs/AAAAAAAAAAI/AAAAAAAAAAA/L0Wl0cFKYhE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")       
    
    Add_Dir( 
        name="Football Daily", url=BASE+YOUTUBE_USER_ID_3+"/", folder=True,
        icon="https://yt3.ggpht.com/-enmySwhRKW4/AAAAAAAAAAI/AAAAAAAAAAA/XyJeO8eB-4E/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")       
    
    Add_Dir( 
        name="talkSport", url=BASE+YOUTUBE_USER_ID_6+"/", folder=True,
        icon="https://yt3.ggpht.com/-y8bzAKL35T0/AAAAAAAAAAI/AAAAAAAAAAA/5Y9Nx0IZm_4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")       
    
    Add_Dir( 
        name="Barca TV", url=BASE2+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://yt3.ggpht.com/-0sSC2cBnFjc/AAAAAAAAAAI/AAAAAAAAAAA/mLhCPlaX-qg/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="La Liga", url=BASE+YOUTUBE_USER_ID_4+"/", folder=True,
        icon="https://yt3.ggpht.com/-y0T08L7H6No/AAAAAAAAAAI/AAAAAAAAAAA/hSqnWXZcSeM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg") 

    Add_Dir( 
        name="Messi Time", url=BASE3+YOUTUBE_PLAYLIST_ID_1+"/", folder=True,
        icon="https://yt3.ggpht.com/-AIp4oqRB-_E/AAAAAAAAAAI/AAAAAAAAAAA/f_3gNqqETLA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")
    
    Add_Dir( 
        name="Messi Magic", url=BASE+YOUTUBE_USER_ID_5+"/", folder=True,
        icon="https://yt3.ggpht.com/-AIp4oqRB-_E/AAAAAAAAAAI/AAAAAAAAAAA/f_3gNqqETLA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg") 

    Add_Dir( 
        name="Best Football Skills and Goals", url=BASE2+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="https://yt3.ggpht.com/-_KzayPk6poM/AAAAAAAAAAI/AAAAAAAAAAA/lDm_-MQfEQk/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Top 10s", url=BASE3+YOUTUBE_PLAYLIST_ID_3+"/", folder=True,
        icon="https://yt3.ggpht.com/-enmySwhRKW4/AAAAAAAAAAI/AAAAAAAAAAA/XyJeO8eB-4E/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Football Stadiums", url=BASE3+YOUTUBE_PLAYLIST_ID_2+"/", folder=True,
        icon="https://yt3.ggpht.com/-y8bzAKL35T0/AAAAAAAAAAI/AAAAAAAAAAA/5Y9Nx0IZm_4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")
    
    Add_Dir( 
        name="Lego Football Replays", url=BASE2+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://yt3.ggpht.com/-TrGnj4kNdVI/AAAAAAAAAAI/AAAAAAAAAAA/20P_iT-Gm3k/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")             


#----------------------------------------------------------------        
# A basic OK Dialog
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()
#----------------------------------------------------------------
# A basic OK Dialog
@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)
#----------------------------------------------------------------

if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
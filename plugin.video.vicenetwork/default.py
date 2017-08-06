# -*- coding: utf-8 -*-

# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Vice Network
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
BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"
BASE3 = "plugin://plugin.video.youtube/user/"

# Set each of your YouTube playlist id's
YOUTUBE_USER_ID_1 = "vice"
YOUTUBE_CHANNEL_ID_1 = "UCWF0PiUvUi3Jma2oFgaiX2w"
YOUTUBE_CHANNEL_ID_2 = "UCZaT_X_mc0BI-djXOlfhqWQ"
YOUTUBE_CHANNEL_ID_3 = "UCB6PV0cvJpzlcXRG7nz6PpQ"
YOUTUBE_CHANNEL_ID_4 = "UC8C8WuWSsFjWFaTHcUQeQxA"
YOUTUBE_CHANNEL_ID_5 = "UC0iwHRFpv2_fpojZgQhElEQ"
YOUTUBE_CHANNEL_ID_6 = "UCroeDtD1dtd1leuxUHDMTXQ"
YOUTUBE_CHANNEL_ID_7 = "UC9ISPZsMaBi5mutsgX6LC1g"
YOUTUBE_CHANNEL_ID_8 = "UCfQDD-pbllOCXHYwiXxjJxA"
YOUTUBE_CHANNEL_ID_9 = "UC_NaA2HkWDT6dliWVcvnkuQ"
YOUTUBE_CHANNEL_ID_10 = "UCflb1gG-X1dy1Ru5JIk5sPw"
#
YOUTUBE_PLAYLIST_ID_1 = "PLDbSvEZka6GFsIZeqpGYqRazEOZh6wyBI"
YOUTUBE_PLAYLIST_ID_2 = "PLDbSvEZka6GE6wL8MtEvaZzs1ghK4CGZC"
YOUTUBE_PLAYLIST_ID_3 = "PLDbSvEZka6GEZPMAxNvcWMW8OvuzNaN8J"
YOUTUBE_PLAYLIST_ID_4 = "PLDbSvEZka6GFgiht08dyfC9NL2Zpqo-ZJ"
#  
YOUTUBE_PLAYLIST_ID_5 = "PLDbSvEZka6GH4tRANwOVNVNF2-QYni3Li"
YOUTUBE_PLAYLIST_ID_6 = "PLDbSvEZka6GHGz-IfXpmA8kUEI09JWTtV"
YOUTUBE_PLAYLIST_ID_7 = "PLDbSvEZka6GEM_JJp1glNxb0q-HCYUT9J"
YOUTUBE_PLAYLIST_ID_8 = "PLDbSvEZka6GEYVMGmuNgLul8JIyvrZ6rW"
YOUTUBE_PLAYLIST_ID_9 = "PLDbSvEZka6GHpX29GZyLD-zr_tgJ5STPQ"
YOUTUBE_PLAYLIST_ID_10 = "PLDbSvEZka6GGCY5p84vKfk0w4rT4gIVlL"
YOUTUBE_PLAYLIST_ID_11 = "PLDbSvEZka6GEfFh_z6vmXFV2bMQ3ISERa"
YOUTUBE_PLAYLIST_ID_12 = "PLDbSvEZka6GGxs-Ml4i49XioSrY9JlpH8"
YOUTUBE_PLAYLIST_ID_13 = "PLDbSvEZka6GE1EWtD6Boug7bFB_OcGsgf"
YOUTUBE_PLAYLIST_ID_14 = "PLDbSvEZka6GEF5kRloeUpkMa5EOkqDcat"
YOUTUBE_PLAYLIST_ID_15 = "PLDbSvEZka6GHw2WVn5U1sRJq7nYujjbsL"
YOUTUBE_PLAYLIST_ID_16 = "PLDbSvEZka6GFoj2G9WAaZnVOMyo_VSH72"


#----------------------------------------------------------------
# This is the main menu we open into
@route(mode='main_menu')
def Main_Menu():

# If debug mode is enabled show the koding tutorials
    if debug == 'true':
        Add_Dir ( '[COLOR=lime]Koding Tutorials[/COLOR]', '', "tutorials", True, '', '', '' )

    Add_Dir( 
        name="Vice", url=BASE3+YOUTUBE_USER_ID_1+"/", folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")       
    
    Add_Dir( 
        name="Viceland", url=BASE2+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://yt3.ggpht.com/-eHn3-vaOb3Y/AAAAAAAAAAI/AAAAAAAAAAA/2y3py4kCs5A/s88-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Vice News", url=BASE2+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://yt3.ggpht.com/-eHn3-vaOb3Y/AAAAAAAAAAI/AAAAAAAAAAA/2y3py4kCs5A/s88-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Motherboard", url=BASE2+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="https://yt3.ggpht.com/-Sm4Dnmn9Tkc/AAAAAAAAAAI/AAAAAAAAAAA/CMWV65I3zYc/s88-c-k-no-mo-rj-c0xffffff/photo.jpg") 

    Add_Dir( 
        name="Tonic", url=BASE2+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="https://yt3.ggpht.com/-AQVM5irGLcU/AAAAAAAAAAI/AAAAAAAAAAA/6tu0ra3_8fI/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")     

    Add_Dir( 
        name="i-D", url=BASE2+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="https://yt3.ggpht.com/-9EJeOQQJlhE/AAAAAAAAAAI/AAAAAAAAAAA/2aB2l5TePIU/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")     

    Add_Dir( 
        name="Creators", url=BASE2+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="https://yt3.ggpht.com/-NYksU6l52Zw/AAAAAAAAAAI/AAAAAAAAAAA/LZgr22RG8sM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg") 

    Add_Dir( 
        name="Broadly", url=BASE2+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="https://yt3.ggpht.com/-vxsNK4Vcxtc/AAAAAAAAAAI/AAAAAAAAAAA/8Vzv_2qP1a4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg") 

    Add_Dir( 
        name="Amuse", url=BASE2+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
        icon="https://yt3.ggpht.com/-guodNVD9aW8/AAAAAAAAAAI/AAAAAAAAAAA/mkTd5YCydYk/s100-c-k-no-mo-rj-c0xffffff/photo.jpg") 


    Add_Dir( 
        name="Noisy", url=BASE2+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="https://yt3.ggpht.com/-WHdsTGMMGoo/AAAAAAAAAAI/AAAAAAAAAAA/YG6V1iqrJUg/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")   

    Add_Dir( 
        name="Vice Sports", url=BASE2+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="https://yt3.ggpht.com/-XXtelFSvSUM/AAAAAAAAAAI/AAAAAAAAAAA/2xGLKIKkONw/s100-c-k-no-mo-rj-c0xffffff/photo.jpg") 

    Add_Dir( 
        name="VICE on HBO", mode='subViceOnHBO', folder=True,
        icon="http://cdn.hbowatch.com/wp-content/uploads/2016/01/VICEonHBO.jpg")   

    Add_Dir( 
        name="VICE Shows", mode='subViceShows', folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")            

#----------------------------------------------------------------
#  Start of Sub Mnenu Lists
@route(mode='subViceOnHBO')
def ViceOnHBO():

    Add_Dir( 
        name="Vice on HBO (Season 1)", url=BASE+YOUTUBE_PLAYLIST_ID_1+"/", folder=True,
        icon="http://cdn.hbowatch.com/wp-content/uploads/2016/01/VICEonHBO.jpg")

    Add_Dir( 
        name="Vice on HBO (Season 2)", url=BASE+YOUTUBE_PLAYLIST_ID_2+"/", folder=True,
        icon="http://cdn.hbowatch.com/wp-content/uploads/2016/01/VICEonHBO.jpg")

    Add_Dir( 
        name="Vice on HBO (Season 3)", url=BASE+YOUTUBE_PLAYLIST_ID_3+"/", folder=True,
        icon="http://cdn.hbowatch.com/wp-content/uploads/2016/01/VICEonHBO.jpg")

    Add_Dir( 
        name="Vice on HBO (Season 4)", url=BASE+YOUTUBE_PLAYLIST_ID_4+"/", folder=True,
        icon="http://cdn.hbowatch.com/wp-content/uploads/2016/01/VICEonHBO.jpg")    

#----------------------------------------------------------------   
@route(mode='subViceShows')
def ViceShows():

    Add_Dir( 
        name="Vice Reports", url=BASE+YOUTUBE_PLAYLIST_ID_16+"/", folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")    

    Add_Dir( 
        name="Vice International", url=BASE+YOUTUBE_PLAYLIST_ID_12+"/", folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")    

    Add_Dir( 
        name="Profiles by Vice", url=BASE+YOUTUBE_PLAYLIST_ID_13+"/", folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")    
   
    Add_Dir( 
        name="Vice Meets", url=BASE+YOUTUBE_PLAYLIST_ID_11+"/", folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")    

    Add_Dir( 
        name="Fringes", url=BASE+YOUTUBE_PLAYLIST_ID_14+"/", folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")    

    Add_Dir( 
        name="The Vice Guide to Travel", url=BASE+YOUTUBE_PLAYLIST_ID_9+"/", folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")    
    
    Add_Dir( 
        name="Slutever", url=BASE+YOUTUBE_PLAYLIST_ID_15+"/", folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")    

    Add_Dir( 
        name="Love Industries", url=BASE+YOUTUBE_PLAYLIST_ID_7+"/", folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Vice Talks Film", url=BASE+YOUTUBE_PLAYLIST_ID_5+"/", folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="The Chosen Ones", url=BASE+YOUTUBE_PLAYLIST_ID_8+"/", folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")    
   
    Add_Dir( 
        name="Weediquette", url=BASE+YOUTUBE_PLAYLIST_ID_10+"/", folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")    

    Add_Dir( 
        name="Outsider", url=BASE+YOUTUBE_PLAYLIST_ID_6+"/", folder=True,
        icon="https://yt3.ggpht.com/-SuohYAOTZvs/AAAAAAAAAAI/AAAAAAAAAAA/JHg2bUQ0Gjc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")

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
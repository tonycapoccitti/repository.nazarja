# -*- coding: utf-8 -*-

""" ^ SECTION 1:
    This should be at the top of your code to declare the type of text
    format you're using. Without this you may find some text editors save
    it in an incompatible format and this can make bug tracking extremely
    confusing! More info here: https://www.python.org/dev/peps/pep-0263/
"""

#----------------------------------------------------------------

"""
    SECTION 2:
    This is where you'd put your license details, the GPL3 license 
    is the most common to use as it makes it easy for others to fork
    and improve upon your code. If you're re-using others code ALWAYS
    check the license first, removal of licenses is NOT allowed and you
    generally have to keep to the same license used in the original work
    (check license details as some do differ).

    Although not all licenses require it (some do, some don't),
    you should always give credit to the original author(s). Someone may have spent
    months if not years on the code so really it's the very least you can do if
    you choose to use their work as a base for your own.
"""
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Add-on: My Playlist Add-on
# Author: Add your name here

#----------------------------------------------------------------

"""
    SECTION 3:
    This is your global imports, any modules you need to import code from
    are added here. You'll see a handful of the more common imports below.
"""
import os           # access operating system commands
import xbmc         # the base xbmc functions, pretty much every add-on is going to need at least one function from here
import xbmcaddon    # pull addon specific information such as settings, id, fanart etc.
import xbmcplugin   # contains functions required for creating directory structure style add-ons (plugins)

# The following are often used, we are not using them in this particular file so they are commented out

# import re           # allows use of regex commands, if you're intending on scraping you'll need this
# import xbmcgui      # gui based functions, contains things like creating dialog pop-up windows

from koding import route, Add_Dir, Addon_Setting, Data_Type, Find_In_Text
from koding import Open_URL, OK_Dialog, Open_Settings, Play_Video, Run, Text_File

#----------------------------------------------------------------
"""
    SECTION 4:
    These are our global variables, anything we set here can be accessed by any of
    our functions later on. Please bare in mind though that if you change the value
    of a global variable from inside a function the value will revert back to the
    value set here once that function has completed.
"""
debug        = Addon_Setting(setting='debug')       # Grab the setting of our debug mode in add-on settings
addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id
home         = xbmc.translatePath('special://home') # Set the path of the home Kodi folder

# Our master XML we want to load up
main_xml     = 'http://totalrevolution.tv/xmls/main_menu.xml'

# Alternatively you could set a local XML but online obviously means less add-on updates to push
# main_xml     = os.path.join(home,'addons',addon_id,'resources','video.xml')

#----------------------------------------------------------------

"""
    SECTION 5:
    Add our custom functions in here, it's VERY important these go in this section
    as the code in section 6 relies on these functions. If that code tries to run
    before these functions are declared the add-on will fail.

    You'll notice each function in here has a decorator above it (an @route() line of code),
    this assigns a mode to the function so it can be called with Add_Dir and it also tells
    the code what paramaters to send through. For example you'll notice the Start() function
    we've assigned to the mode "start" - this means if we ever want to get Add_Dir to open that
    function we just use the mode "start". This particular function does not require any extra
    params to be sent through but if you look at the Simple_Dialog() function you'll see we send through
    2 different paramaters (title and msg). If you look at the commented out section (lines 105-109)
    you'll see we send these params through as a dictionary. Using that same format you can send through
    as many different params as you wish.
"""

#----------------------------------------------------------------
@route(mode='start')
def Start():
    Main_Menu(main_xml)
#----------------------------------------------------------------
@route(mode='main_menu',args=['url'])
def Main_Menu(url=main_xml):

# If debug mode is enabled show the koding tutorials
    if debug == 'true':
        Add_Dir ( '[COLOR=lime]Koding Tutorials[/COLOR]', '', "tutorials", True, '', '', '' )

#############################################################
# COMMENT OUT THE FOLLOWING 2 LINES WHEN READY FOR RELEASE!!!
    else:
        Add_Dir ( '[COLOR=lime]Enable debug mode for some cool dev tools![/COLOR]', '', "koding_settings", False, '', '', '' )
#############################################################

# An optional example title/message, however in our example we're going to do one via our online xml so we've commented this out
    # my_message= "{'title' : 'Support & Suggestions', 'msg' : \"If you come across any online content you'd like to get added please use the support thread at noobsandnerds.com and I'll be happy to look into it for you.\"}"
    # Add_Dir(
    #     name="Support/Suggestions", url=my_message, mode="simple_dialog", folder=False,
    #     icon="https://cdn2.iconfinder.com/data/icons/picons-basic-2/57/basic2-087_info-512.png")

# Read the contents of our file into memory
    if url.startswith('http'):
        contents  = Open_URL(url)
    else:
        contents  = Text_File(url,'r')

# This isn't essential but we'll replace all linebreaks (\n) and tabs (\t) with an empty string.
# This removes them and just makes it a smaller file to work with and easier to debug.
    contents = contents.replace('\n','').replace('\t','')

# Split the contents up into sections - we're finding every instance of <item> and </item> and everything inbetween
    raw_links = Find_In_Text(content=contents, start='<item>', end=r'</item>')
    xbmc.log(repr(raw_links),2)
    counter = 1
# Now loop through each of those matches and pull out the relevant data
    for item in raw_links:
        xbmc.log('# Checking link %s'%counter,2)
        counter += 1
        title  = Find_In_Text(content=item, start='<title>', end=r'</title>')
        title  = title[0] if (title!=None) else 'Unknown Video'
        thumb  = Find_In_Text(content=item, start='<thumbnail>', end=r'</thumbnail>')
        thumb  = thumb[0] if (thumb!=None) else ''
        fanart = Find_In_Text(content=item, start='<thumbnail>', end=r'</thumbnail>')
        fanart = fanart[0] if (fanart!=None) else ''

    # If this contains sublinks grab all of them
        if not '<sublink>' in item:
            links  = Find_In_Text(content=item, start='<link>', end=r'</link>')

    # Otherwise just grab the link tag
        else:
            links  = Find_In_Text(content=item, start='<sublink>', end=r'</sublink>')

    # If it's an xml file then we set the link to the xml path rather than a list of links
        if links[0].endswith('.xml') or links[0]=='none' or links[0] == '' or links[0].startswith('msg~'):
            links = links[0]

    # If link is none we presume it's a folder
        if links == 'none' or links == '':
            Add_Dir( name=title, url='', mode='', folder=False, icon=thumb, fanart=fanart )

    # If link is a string it's either another menu or a message
        elif Data_Type(links)=='str':

        # If it's a message clean up the string and load up the simple_dialog function
            if links.startswith('msg~'):
                links = links.replace('msg~','')
                Add_Dir( name=title, url="{%s}"%links, mode='simple_dialog', folder=False, icon=thumb, fanart=fanart )

        # Otherwise we presume it's a menu
            else:
                Add_Dir( name=title, url=links, mode='main_menu', folder=True, icon=thumb, fanart=fanart )

    # Otherwise send through our list of links to the Play_Link function
        else:
            Add_Dir( name=title, url="{'url':%s}"%links, mode='play_link', folder=False, icon=thumb, fanart=fanart )
#----------------------------------------------------------------
# Simple function to check playback, it will return true or false if playback successful
@route(mode='play_link',args=['url'])
def Play_Link(url):
# If only one item in the list we try and play automatically
    if len(url)==1:
        if not Play_Video(url[0]):
            OK_Dialog( 'PLAYBACK FAILED','This stream is currently offline.' )

# If more than one link then we give a choice of which link to play
    elif len(url)>1:
        link_list   = []
        counter     = 1
        for item in url:
            link_list.append( 'Link '+str(counter) )
            counter += 1
        choice = Select_Dialog( 'CHOOSE STREAM', link_list )
        if choice >= 0:
            if not Play_Video( url[choice] ):
                OK_Dialog( 'PLAYBACK FAILED','This stream is currently offline.' )
                Play_Link(url)
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

"""
    SECTION 6:
    Essential if creating list items, this tells kodi we're done creating our list items.
    The list will not populate without this. In the run command you need to set default to
    whatever route you want to open into, in this example the 'start' route which opens the
    Start() function up at the top.
"""
if __name__ == "__main__":
    Run(default='start')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
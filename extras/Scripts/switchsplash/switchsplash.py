# Switch splash.png script by Asteron 
# v1.0 - 2007/02/21 
# http://asteron.projects.googlepages.com/

import os, shutil, traceback
import xbmc, xbmcgui

def main():
	splashfile = 'Q:\\media\\splash.png'
	skinname = xbmc.getSkinDir()
	trimmedname = ''.join(skinname.lower().split())
	customsplash = 'Q:\\skin\\' + skinname + '\\extras\\splash.png'
	splashbackup = 'Q:\\media\\splash.png.'+trimmedname
	if not os.path.exists(customsplash):
		xbmcgui.Dialog().ok('ERROR', 'Custom splash.png not found', customsplash)
		return
	
	if os.path.exists(splashbackup):
		os.remove(splashfile)
		shutil.move(splashbackup, splashfile)
		xbmc.executebuiltin('Skin.SetBool(customSplash)')
		xbmc.executebuiltin('Skin.ToggleSetting(customSplash)') #make sure its off		
	else:
		shutil.move(splashfile, splashbackup)
		shutil.copy(customsplash, splashfile)
		xbmc.executebuiltin('Skin.SetBool(customsplash)')		
try:
	main()
except:
	traceback.print_exc()
# -*- coding: cp1252 -*-
      ##########################
      #                        #                      
      #   ResumeX (V.0.4)      #         
      #     By Stanley87       #         
      #                        #
#######                        #######             
#                                    #
#                                    #
#   An Auto Resume script for XBMC   #
#                                    #
######################################

import xbmcgui, xbmc
import string, time, re, os
Root_Dir = os.getcwd().replace(";","")+"\\"
   
SETTINGFILE = Root_Dir + "lib\settings.xml"


class main:
    def gui(self):
        self.passme = 0
        dialog = xbmcgui.Dialog()
        if dialog.yesno("ResumeX","Enable ResumeX?"):
            self.enable = "yes"          
        else:
            self.enable = "no"
            self.winresume = "-"
            self.passme = 1
            dialog = xbmcgui.DialogProgress()
            dialog.create("ResumeX Disabled - OK!")
            time.sleep(2)
            dialog.close()
        if self.passme !=1:
            if dialog.yesno("ResumeX","Enable window resume?"):
                self.winresume = "yes"
            else:
                self.winresume = "no"
            dialog = xbmcgui.DialogProgress()
            dialog.create("ResumeX Enabled - OK!")
            time.sleep(2)
            dialog.close()
        self.writesettings()

            

    def writesettings(self):
        f = open(SETTINGFILE, "wb")
        f.write("<settings>\n")
        f.write("\t<ENABLED>"+self.enable+"</ENABLED>\n")
        f.write("\t<WINRESUME>"+self.winresume+"</WINRESUME>\n")
        f.write("</settings>\n")
        f.close()
        
m = main()
m.gui()
xbmc.executescript('Q:\scripts\ResumeX\lib\engine.py')
del m

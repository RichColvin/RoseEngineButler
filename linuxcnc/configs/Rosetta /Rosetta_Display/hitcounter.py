#######################################################################
#                                                                     #
#   RRRRRR     OOOOOO   SSSSSS  EEEEEEEE TTTTTTTT TTTTTTTT   AAAA     #
#   RR   RR   OO    OO SS    SS EE          TT       TT     AA  AA    #
#   RR    RR  OO    OO SS       EE          TT       TT    AA    AA   #
#   RR   RR   OO    OO  SS      EE          TT       TT    AA    AA   #
#   RRRRRR    OO    OO   SSSS   EEEEEE      TT       TT    AA    AA   #
#   RR   RR   OO    OO      SS  EE          TT       TT    AAAAAAAA   #
#   RR    RR  OO    OO       SS EE          TT       TT    AA    AA   #
#   RR    RR  OO    OO SS    SS EE          TT       TT    AA    AA   #
#   RR    RR   OOOOOO   SSSSSS  EEEEEEEE    TT       TT    AA    AA   #
#                                                                     #
#######################################################################
#                                                                     #
# LinuxCNC configuration for use with a Rose Engine                   #
#                                                                     #
# File:                                                               #
#   hitcounter.py                                                     #
#                                                                     #
# Purpose:                                                            #
#   This is used to handle buttons used in panels developed for       #
#   Rosetta's use on LinuxCNC.                                        #
#                                                                     #
# End User Customisation:                                             #
#   The end user of the Rosetta system may modify this file to        #
#   accommodate their local configuration.  It is recommended that    #
#   a copy of this file be saved before changes are made.             #
#                                                                     #
#   Changes to this file are not supported by Colvin Tools nor        #
#   Brainwave Embedded.                                               #
#                                                                     #
# Version                                                             #
#   1.0 - 30 July 2025, R. Colvin                                     #
#                                                                     #
# Copyright (c) 2025 Colvin Tools and Brainwave Embedded.             #
#                                                                     #
# The following MIT/X Consortium License applies to the Rosetta       #
# system. Use of this system constitutes consent to the terms         #
# outlined below.                                                     #
#                                                                     #
# Permission is hereby granted, free of charge, to any person         #
# obtaining a copy of this software and associated documentation      #
# files (the "Software"), to deal in the Software without             #
# restriction, including without limitation the rights to use, copy,  #
# modify, merge, publish, distribute, sublicense, and/or sell copies  #
# of the Software, and to permit persons to whom the Software is      #
# furnished to do so, subject to the following conditions:            #
#                                                                     #
#       The above copyright notice and this permission notice shall   #
#       be included in all copies or substantial portions of the      #
#       Software.                                                     #
#                                                                     #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,     #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF  #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND               #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN  #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN   #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE    #
# SOFTWARE.                                                           #
#                                                                     #
# Except as contained in this notice, the name of COPYRIGHT HOLDERS   #
# shall not be used in advertising or otherwise to promote the sale,  #
# use or other dealings in this Software without prior written        #
# authorization from COPYRIGHT HOLDERS.                               #
#######################################################################

import hal
import glib
import time
import linuxcnc

# Establish connection to command and status channels
c = linuxcnc.command()
s = linuxcnc.stat()

class HandlerClass:
    '''
    class with gladevcp callback handlers
    '''

    def on_button_press(self,widget,data=None):
        '''
        a callback method
        parameters are:
            the generating object instance, likte a GtkButton instance
            user data passed if any - this is currently unused but
            the convention should be retained just in case
        '''
        print ("on_button_press called")
        self.nhits += 1
        self.builder.get_object('hits').set_label("Hits: %d" % (self.nhits))

#######################################################################
# B_Idx_change_value                                                  #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: B_Idx (on setting the value)                              #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the rotational distance (degrees) for the     #
#   B axis.                                                           #
#######################################################################
    def B_Idx_change_value(self,widget):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.BIdx = widget.get_value()

#######################################################################
# Sp0_CCW_on_button_press                                             #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: Sp0_CCW (on click)                                        #
#                                                                     #
# Purpose:                                                            #
#   This is used to start the spindles rotating counter-clockwise.    #
#   Note:  this starts both Sp0 and Sp1.                              #
#######################################################################
    def Sp0_CCW_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to start spindles rotating.
        c.mdi("M3 $-1")

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_CW_on_button_press                                              #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: Sp0_CW (on click)                                         #
#                                                                     #
# Purpose:                                                            #
#   This is used to start the spindles rotating clockwise.            #
#   Note:  this starts both Sp0 and Sp1.                              #
#######################################################################
    def Sp0_CW_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to start spindles rotating.
        c.mdi("M4 $-1")

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Idx_change_value                                                #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: Sp0_Idx (on setting the value)                            #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the rotational distance (degrees) for the     #
#   Sp0 spindle.                                                      #
#######################################################################
    def Sp0_Idx_change_value(self,widget):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.Sp0Idx = widget.get_value()

#######################################################################
# Sp0_Idx_CCW_on_button_press                                         #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: Sp0_Idx_CCW (on click)                                    #
#                                                                     #
# Purpose:                                                            #
#   This is used to index the Sp0 spindle in a counter-clockwise      #
#   direction.                                                        #
#######################################################################
    def Sp0_Idx_CCW_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to start spindles rotating.
        sSp0Spd = "M19 R" + str(self.Sp0Idx) + " P1 $0"
        c.mdi(sSp0Spd)

        c.mdi("M3 $-1")

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Spd_change_value                                                #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: Spd_Bar (on change)                                       #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the spee for the spindle.                     #
#######################################################################
    def Sp0_Spd_change_value(self,widget):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        Sp0Spd = widget.get_value()
        Sp1Spd = self.Sp1Pct * Sp0Spd / 100

        # Send an MDI command to set the spindles' speed.
        sSp0Spd = "S" + str(Sp0Spd) + " $0"
        sSp1Spd = "S" + str(Sp1Spd) + " $1"

        c.mdi(sSp0Spd)
        c.mdi(sSp1Spd)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Stop_on_button_press                                            #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: Sp0_Stop (on click)                                       #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def Sp0_Stop_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to stop the spindles from rotating.
        c.mdi("M5")

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp1_Idx_change_value                                                #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: Sp1_Idx (on setting the value)                            #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the rotational distance (degrees) for the     #
#   Sp1 spindle (the rosette phaser/multiplier).                      #
#######################################################################
    def Sp1_Idx_change_value(self,widget):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.Sp1Idx = widget.get_value()

#######################################################################
# Sp1_Pct_of_Sp0                                                      #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: Sp1_Pct (on change)                                       #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the speed for the Sp1 spindle (rosette        #
#   phaser/multiplier) as a percentage of the spindle speed.          #
#######################################################################
    def Sp1_Pct_of_Sp0(self,widget):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.Sp1Pct = widget.get_value()



#######################################################################
# U_Idx_change_value                                                  #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Linear                                        #
#   Button: U_Idx (on setting the value)                              #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement distance for the Z axis.         #
#######################################################################
    def U_Idx_change_value(self,widget):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.UIdx = widget.get_value()

#######################################################################
# U_Minus_on_button_press                                             #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: U_Idx_Minus (on click)                                    #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def U_Minus_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 U-" + str(self.UIdx)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# U_Plus_on_button_press                                              #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: U_Idx_Plus (on click)                                     #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def U_Plus_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 U" + str(self.UIdx)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# V_Idx_change_value                                                  #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Linear                                        #
#   Button: V_Idx (on setting the value)                              #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement distance for the Z axis.         #
#######################################################################
    def V_Idx_change_value(self,widget):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.VIdx = widget.get_value()

#######################################################################
# V_Minus_on_button_press                                             #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: V_Idx_Minus (on click)                                    #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def V_Minus_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 V-" + str(self.VIdx)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# V_Plus_on_button_press                                              #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: V_Idx_Plus (on click)                                     #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def V_Plus_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 V" + str(self.VIdx)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# X_Idx_change_value                                                  #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Linear                                        #
#   Button: X_Idx (on setting the value)                              #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement distance for the Z axis.         #
#######################################################################
    def X_Idx_change_value(self,widget):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.XIdx = widget.get_value()

#######################################################################
# X_Minus_on_button_press                                             #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: X_Idx_Minus (on click)                                    #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def X_Minus_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 X-" + str(self.XIdx)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# X_Plus_on_button_press                                              #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: X_Idx_Plus (on click)                                     #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def X_Plus_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 X" + str(self.XIdx)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Y_Idx_change_value                                                  #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Linear                                        #
#   Button: Y_Idx (on setting the value)                              #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement distance for the Z axis.         #
#######################################################################
    def Y_Idx_change_value(self,widget):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.YIdx = widget.get_value()

#######################################################################
# Y_Minus_on_button_press                                             #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: Y_Idx_Minus (on click)                                    #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def Y_Minus_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 Y-" + str(self.YIdx)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Y_Plus_on_button_press                                              #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: Y_Idx_Plus (on click)                                     #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def Y_Plus_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 Y" + str(self.YIdx)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Z_Idx_change_value                                                  #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Linear                                        #
#   Button: Z_Idx (on setting the value)                              #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement distance for the Z axis.         #
#######################################################################
    def Z_Idx_change_value(self,widget):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.ZIdx = widget.get_value()

#######################################################################
# Z_Minus_on_button_press                                             #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: Z_Idx_Minus (on click)                                    #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def Z_Minus_on_button_press(self,widget,data):

        print("Starting Z_Minus_on_button_press")
        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 Z-" + str(self.ZIdx)
        c.mdi(Gcode)
        print(Gcode)

        # Wait for the command to complete
        c.wait_complete()
        print("Ending Z_Minus_on_button_press")

#######################################################################
# Z_Plus_on_button_press                                              #
#                                                                     #
# Called from:                                                        #
#   Panel:  Rosetta_Tab_Rotary                                        #
#   Button: Z_Idx_Plus (on click)                                     #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def Z_Plus_on_button_press(self,widget,data):

        print("Starting Z_Plus_on_button_press")
        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 Z" + str(self.ZIdx)
        c.mdi(Gcode)
        print(Gcode)

        # Wait for the command to complete
        c.wait_complete()
        print("Ending Z_Plus_on_button_press")

#######################################################################
# __init__                                                            #
#                                                                     #
# Purpose:                                                            #
#   This is used to initialize everything.                            #
#######################################################################
    def __init__(self, halcomp,builder,useropts):
        '''
        Handler classes are instantiated in the following state:
        - the widget tree is created, but not yet realized (no toplevel window.show() executed yet)
        - the halcomp HAL component is set up and the widhget tree's HAL pins have already been added to it
        - it is safe to add more hal pins because halcomp.ready() has not yet been called at this point.

        after all handlers are instantiated in command line and get_handlers() order, callbacks will be
        connected with connect_signals()/signal_autoconnect()

        The builder may be either of libglade or GtkBuilder type depending on the glade file format.
        '''

        self.halcomp    = halcomp
        self.builder    = builder
        self.nhits      = 0

        ###############################################################
        # Global variables - declare and set initial value.           #
        ###############################################################

        self.BIdx       = 90.0      # B axis index degrees

        self.Sp0Idx     = 90.0      # Sp0 index degrees

        self.Sp1Idx     = 90.0      # Sp1 index degrees
        self.Sp1Pct     = 100.0     # Sp1 speed percentage of Sp0 speed

        self.UIdx       = 0.0       # U axis index distance

        self.VIdx       = 0.0       # V axis index distance

        self.XIdx       = 0.0       # X axis index distance

        self.YIdx       = 0.0       # Y axis index distance

        self.ZIdx       = 0.0       # Z axis index distance

def get_handlers(halcomp,builder,useropts):
    '''
    this function is called by gladevcp at import time (when this module is passed with '-u <modname>.py')

    return a list of object instances whose methods should be connected as callback handlers
    any method whose name does not begin with an underscore ('_') is a  callback candidate

    the 'get_handlers' name is reserved - gladevcp expects it, so do not change
    '''
    return [HandlerClass(halcomp,builder,useropts)]

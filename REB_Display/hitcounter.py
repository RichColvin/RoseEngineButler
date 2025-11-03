#######################################################################
#                    RRRRRR    EEEEEEEE  BBBBBBB                      #
#                    RR   RR   EE        BB    BB                     #
#                    RR   RR   EE        BB    BB                     #
#                    RRRRRR    EEEEEE    BBBBBBB                      #
#                    RR   RR   EE        BB    BB                     #
#                    RR    RR  EE        BB    BB                     #
#                    RR    RR  EEEEEEEE  BBBBBBB                      #
#                                                                     #
# Rose Engine Butler                                                  #
#######################################################################
#                                                                     #
# LinuxCNC configuration for use with a Rose Engine                   #
#                                                                     #
# File:                                                               #
#   hitcounter.py                                                     #
#                                                                     #
# Purpose:                                                            #
#   This is used to handle buttons used in panels developed for       #
#   Rose Engine Butler's use on LinuxCNC.                             #
#                                                                     #
# End User Customisation:                                             #
#   THE END USER OF THE ROSE ENGINE BUTLER SYSTEM SHOULD NOT MODIFY   #
#   THIS FILE.                                                        #
#                                                                     #
#   Changes to this file are not supported by Colvin Tools nor        #
#   Brainwave Embedded.                                               #
#                                                                     #
# Version                                                             #
#   1.0 - 05 August 2025, R. Colvin                                   #
#                                                                     #
# Copyright (c) 2025 Colvin Tools and Brainwave Embedded.             #
#                                                                     #
# The following MIT/X Consortium License applies to the Rose Engine   #
# Butler system. Use of this system constitutes consent to the terms  #
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
# B_Idx_Deg_Sel
#
# Called from:
#   Panel:  REB_Tab_Rotary
#   Button: B_Idx_Deg  (HAL_RadioButton)
#
# Data Values
#   Read:   (none)
#   Used:   BIdxDist - Distance set by user
#   Sets:   BIdxDeg - Degrees to index during movement
#           BIdxDegDiv - type of distance measurement (Deg or Div)
#   Writes: (none)
#
# Purpose:
#   This is used to set the rotational distance measurement as
#   degrees for the B axis.
#######################################################################
    def B_Idx_Deg_Sel(self,widget,data):

        print("=================================================")
        print("FUNCTION B_Idx_Deg_Sel")

        self.BIdxDeg = self.BIdxDist
        self.BIdxDegDiv = "Deg"

        Prt1 = "BIdxDegDiv = " + self.BIdxDegDiv
        print(Prt1)
        Prt2 = "BIdxDeg = " + str(self.BIdxDeg) + " deg"
        print(Prt2)


#######################################################################
# B_Idx_Div_Sel
#
# Called from:
#   Panel:  REB_Tab_Rotary
#   Button: B_Idx_Div  (HAL_RadioButton)
#
# Data Values
#   Read:   (none)
#   Used:   BIdxDist - Distance set by user
#   Sets:   BIdxDeg - Degrees to index during movement
#           BIdxDegDiv - type of distance measurement (Deg or Div)
#   Writes: (none)
#
# Purpose:
#   This is used to set the rotational distance measurement as
#   divisions of a circle for the B axis (deg = 360/div).
#######################################################################
    def B_Idx_Div_Sel(self,widget,data):

        print("=================================================")
        print("FUNCTION B_Idx_Div_Sel")

        self.BIdxDeg = 360 / self.BIdxDist

        self.BIdxDegDiv = "Div"

        Prt1 = "BIdxDegDiv = " + self.BIdxDegDiv
        print(Prt1)
        Prt2 = "BIdxDeg = " + str(self.BIdxDeg) + " deg"
        print(Prt2)


#######################################################################
# B_Idx_Dist
#
# Called from:
#   Panel:  REB_Tab_Rotary
#   Button: B_Idx_Dist  (HAL_SpinButton)
#
# Data Values
#   Read:   BIdxDist - Distance set by user
#   Used:   BIdxDegDiv - type of distance measurement (Deg or Div)
#   Sets:   BIdxDeg - Degrees to index during movement
#           BIdxDist - Distance set by user
#   Writes: (none)
#
# Purpose:
#   This is used to set the rotational distance (degrees or
#   divisions of a circle) for the B axis.
#######################################################################
    def B_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION B_Idx_Dist")

        self.BIdxDist = widget.get_value()

        if self.BIdxDegDiv == "Deg":
                self.BIdxDeg = self.BIdxDist
        else:
                self.BIdxDeg = 360 / self.BIdxDist

        Prt1 = "BIdxDegDiv = " + self.BIdxDegDiv
        print(Prt1)
        Prt2 = "BIdxDeg = " + str(self.BIdxDeg) + " deg"
        print(Prt2)

#######################################################################
# B_Idx_Feed
#
# Called from:
#   Panel:  REB_Tab_Rotary    (HAL_SpinButton)
#   Button: B_Feed
#
# Data Values
#   Read:   BFeed - Feed rate set by user
#   Used:   (none)
#   Sets:   BFeed
#   Writes: (none)
#
# Purpose:
#   This is used to set the movement speed for the B axis.
#######################################################################
    def B_Idx_Feed(self,widget):

        print("=================================================")
        print("FUNCTION B_Idx_Feed")

        self.BFeed = widget.get_value()

        Prt1 = "BFeed = " + str(self.BFeed)
        print(Prt1)

#######################################################################
# B_Idx_Fwd
#
# Called from:
#   Panel:  REB_Tab_Rotary
#   Button: B_Idx_Fwd  (Hal_Button)
#
# Data Values
#   Read:   (none)
#   Used:   (none)
#   Sets:   BIdxQty - the quantity of indexes so far.  Forward
#           increases this value.
#   Writes: BIdxQty to BIdxQty
#
# Purpose:
#   This is used to run the B axis forward using the G0 Gcode.
#######################################################################
    def B_Idx_Fwd(self,widget,data):

        print("=================================================")
        print("FUNCTION B_Idx_Fwd")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 B" + str(self.BIdxDeg) + " F" + str(self.BFeed)

        print(Gcode)
        c.mdi(Gcode)

        self.BIdxQty = self.BIdxQty + 1
        Prt1 = "BIdxQty = " + str(self.BIdxQty)
        print(Prt1)

        # BIdxQtystr = str(self.BIdxQty)
        # widget.set_label(BIdxQty, BIdxQtystr)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# B_Idx_Rev
#
# Called from:
#   Panel:  REB_Tab_Rotary
#   Button: B_Idx_Rev  (Hal_Button)
#
# Data Values
#   Read:   (none)
#   Used:   (none)
#   Sets:   BIdxQty - the quantity of indexes so far.  Reverse
#           decreases this value.
#   Writes: BIdxQty to BIdxQty
#
# Purpose:
#   This is used to run the B axis in reverse using the G0 Gcode.
#######################################################################
    def B_Idx_Rev(self,widget,data):

        print("=================================================")
        print("FUNCTION B_Idx_Rev")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 B-" + str(self.BIdxDeg) + " F" + str(self.BFeed)

        print(Gcode)
        c.mdi(Gcode)

        self.BIdxQty = self.BIdxQty - 1
        Prt1 = "BIdxQty = " + str(self.BIdxQty)
        print(Prt1)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Fwd
# 
# Called from:
#   Panel:  REB_Tab_Base
#   Button: Sp0_Fwd  (Hal_Button)
#	Signal:	GtkButton/pressed
#			GtkWidget/button-press-event
#
# Data Values
#   Read:   (none)
#   Used:   (S Gcode sets speed)
#   Sets:   (none)
#   Writes: self.Sp0Spd to the S Gcode (Sspd $0)
#   		Sp1Spd to the S Gcode (Sspd $1)
#
# Purpose:
#   This is used to start the spindles rotating forward.
#   Note:  this starts both Sp0 and Sp1.
#######################################################################
    def Sp0_Fwd(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Fwd")

        # Ensure the system is in MDI mode
        c.mode(linuxcnc.MODE_MDI)
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # In case the values had not already been written to the 
        # Gcode S values, write them.  
        Sp1Spd = self.Sp1Pct * self.Sp0Spd / 100

        # Send an MDI command to set the spindles' speed.
        sSp0Spd = "S" + str(self.Sp0Spd) + " $0"
        sSp1Spd = "S" + str(Sp1Spd) + " $1"

        print(sSp0Spd)
        c.mdi(sSp0Spd)

        print(sSp1Spd)
        c.mdi(sSp1Spd)

        # Send an MDI command to start spindles rotating.
        Gcode = "M3 $-1"

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Idx_change_value                                                #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Rotary                                            #
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
#   Panel:  REB_Tab_Rotary                                            #
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

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Rev
# 
# Called from:
#   Panel:  REB_Tab_Base
#   Button: Sp0_Rev  (Hal_Button)
#	Signal:	GtkButton/pressed
#			GtkWidget/button-press-event
#
# Data Values
#   Read:   (none)
#   Used:   (S Gcode sets speed)
#   Sets:   (none)
#   Writes: self.Sp0Spd to the S Gcode (Sspd $0)
#   		Sp1Spd to the S Gcode (Sspd $1)
#
# Purpose:
#   This is used to start the spindles rotating in reverse.
#   Note:  this starts both Sp0 and Sp1.
#######################################################################
    def Sp0_Rev(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Rev")

        # Ensure the system is in MDI mode
        c.mode(linuxcnc.MODE_MDI)
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # In case the values had not already been written to the 
        # Gcode S values, write them.  
        Sp1Spd = self.Sp1Pct * self.Sp0Spd / 100

        # Send an MDI command to set the spindles' speed.
        sSp0Spd = "S" + str(self.Sp0Spd) + " $0"
        sSp1Spd = "S" + str(Sp1Spd) + " $1"

        print(sSp0Spd)
        c.mdi(sSp0Spd)

        print(sSp1Spd)
        c.mdi(sSp1Spd)

        # Send an MDI command to start spindles rotating.
        Gcode = "M4 $-1"

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Spd
#
# Called from:
#   Panel:  REB_Tab_Base
#   Button: Sp0_Spd  (Hal_SpinButton)
#	Signal:	GtkSpinButton/value-changed
#
# Data Values
#   Read:   Sp0Spd from Sp0_Spd
#   Used:   Sp1Pct
#   Sets:   self.Sp0Spd - the speed for the spindle (Sp0)
#   	   	Sp1Spd - the speed for the rosette phaser multiplier (Sp1)
#   Writes: self.Sp0Spd to the S Gcode (Sspd $0)
#   		Sp1Spd to the S Gcode (Sspd $1)
#
# Purpose:
#   This is used to set the speed for the spindle (Sp0) & the 
#	rosette phaser multiplier (Sp1).
#######################################################################
    def Sp0_Spd(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Spd")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.Sp0Spd = widget.get_value()
        Sp1Spd = self.Sp1Pct * self.Sp0Spd / 100

        # Send an MDI command to set the spindles' speed.
        sSp0Spd = "S" + str(self.Sp0Spd) + " $0"
        sSp1Spd = "S" + str(Sp1Spd) + " $1"

        print(sSp0Spd)
        c.mdi(sSp0Spd)

        print(sSp1Spd)
        c.mdi(sSp1Spd)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Stop
# 
# Called from:
#   Panel:  REB_Tab_Base
#   Button: Sp0_Stop  (Hal_Button)
#	Signal:	GtkButton/pressed
#			GtkWidget/button-press-event
#
# Data Values
#   Read:   (none)
#   Used:   (none)
#   Sets:   (none)
#   Writes: (none)
#
# Purpose:
#   This is used to stop the spindles rotating.
#   Note:  this stops both Sp0 and Sp1.
#######################################################################
    def Sp0_Stop(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Stop")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to stop the spindles from rotating.
        Gcode = "M5"

        print(Gcode)
        c.mdi(Gcode)

        c.mdi("M5")

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp1_Idx_change_value                                                #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Rotary                                            #
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
# Sp1_Pct
#
# Called from:
#   Panel:  REB_Tab_Base
#   Button: Sp1_Pct  (Hal_SpinButton)
#	Signal:	GtkSpinButton/value-changed
#
# Data Values
#   Read:   Sp1Pct from Sp1_Pct
#   Used:   Sp0Spd
#   Sets:   (none)
#   Writes: Sp1Spd to the S Gcode (Sspd $1)
#
# Purpose:
#   This is used to set the speed for the rosette phaser / multiplier
#   (Sp0) as a percentage of the spindle speed.
#######################################################################
    def Sp1_Pct(self,widget):

        print("=================================================")
        print("FUNCTION Sp1_Pct")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.Sp1Pct = widget.get_value()
        Sp1Spd = self.Sp0Spd * self.Sp1Pct / 100

        # Send an MDI command to set the spindles' speed.
        sSp1Spd = "S" + str(Sp1Spd) + " $1"

        print(sSp1Spd)
        c.mdi(sSp1Spd)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# U_Feed_chg_value                                                    #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Linear                                            #
#   Button: U_Feed (on setting the value)                             #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement speed for the U axis.            #
#######################################################################
    def U_Feed_chg_value(self,widget):

        self.UFeed = widget.get_value()

        print("U_Feed_chg_value =")
        print(self.UFeed)

#######################################################################
# U_Idx_change_value                                                  #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Linear                                            #
#   Button: U_Idx (on setting the value)                              #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement distance for the Z axis.         #
#######################################################################
    def U_Idx_change_value(self,widget):

        self.UIdx = widget.get_value()

        print("U_Idx_chg_value =")
        print(self.UIdx)

#######################################################################
# U_Minus_on_button_press                                             #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Rotary                                            #
#   Button: U_Idx_Minus (on click)                                    #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def U_Minus_on_button_press(self,widget,data):

        print ("U_Minus_on_button_press called")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 U-" + str(self.UIdx) + " F" + str(self.UFeed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# U_Plus_on_button_press                                              #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Rotary                                            #
#   Button: U_Idx_Plus (on click)                                     #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def U_Plus_on_button_press(self,widget,data):

        print ("U_Plus_on_button_press called")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 U" + str(self.UIdx) + " F" + str(self.UFeed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# V_Feed_chg_value                                                    #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Linear                                            #
#   Button: V_Feed (on setting the value)                             #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement speed for the V axis.            #
#######################################################################
    def V_Feed_chg_value(self,widget):

        self.VFeed = widget.get_value()

        print("V_Feed_chg_value =")
        print(self.VFeed)

#######################################################################
# V_Idx_change_value                                                  #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Linear                                            #
#   Button: V_Idx (on setting the value)                              #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement distance for the Z axis.         #
#######################################################################
    def V_Idx_change_value(self,widget):

        self.VIdx = widget.get_value()

        print("V_Idx_chg_value =")
        print(self.VIdx)

#######################################################################
# V_Minus_on_button_press                                             #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Rotary                                            #
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
        Gcode = "G0 V-" + str(self.VIdx) + " F" + str(self.VFeed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# V_Plus_on_button_press                                              #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Rotary                                            #
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
        Gcode = "G0 V" + str(self.VIdx) + " F" + str(self.VFeed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# X_Feed_chg_value                                                    #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Linear                                            #
#   Button: X_Feed (on setting the value)                             #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement speed for the X axis.            #
#######################################################################
    def X_Feed_chg_value(self,widget):

        self.XFeed = widget.get_value()

        print("X_Feed_chg_value =")
        print(self.XFeed)

#######################################################################
# X_Idx_change_value                                                  #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Linear                                            #
#   Button: X_Idx (on setting the value)                              #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement distance for the Z axis.         #
#######################################################################
    def X_Idx_chg_value(self,widget):

        self.XIdx = widget.get_value()

        print("X_Idx_chg_value =")
        print(self.XIdx)

#######################################################################
# X_Minus_on_button_press                                             #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Rotary                                            #
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
        Gcode = "G0 X-" + str(self.XIdx) + " F" + str(self.XFeed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# X_Plus_on_button_press                                              #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Rotary                                            #
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
        Gcode = "G0 X" + str(self.XIdx) + " F" + str(self.XFeed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Y_Feed_chg_value                                                    #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Linear                                            #
#   Button: Y_Feed (on setting the value)                             #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement speed for the Y axis.            #
#######################################################################
    def Y_Feed_chg_value(self,widget):

        self.YFeed = widget.get_value()

        print("Y_Feed_chg_value =")
        print(self.YFeed)

#######################################################################
# Y_Idx_change_value                                                  #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Linear                                            #
#   Button: Y_Idx (on setting the value)                              #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement distance for the Z axis.         #
#######################################################################
    def Y_Idx_change_value(self,widget):

        self.YIdx = widget.get_value()

        print("Y_Idx_chg_value =")
        print(self.YIdx)

#######################################################################
# Y_Minus_on_button_press                                             #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Rotary                                            #
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
        Gcode = "G0 Y-" + str(self.YIdx) + " F" + str(self.YFeed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Y_Plus_on_button_press                                              #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Rotary                                            #
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
        Gcode = "G0 Y" + str(self.YIdx) + " F" + str(self.YFeed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Z_Feed_chg_value                                                    #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Linear                                            #
#   Button: Z_Feed (on setting the value)                             #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement speed for the Z axis.            #
#######################################################################
    def Z_Feed_chg_value(self,widget):

        self.ZFeed = widget.get_value()

        print("Z_Feed_chg_value =")
        print(self.ZFeed)

#######################################################################
# Z_Idx_change_value                                                  #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Linear                                            #
#   Button: Z_Idx (on setting the value)                              #
#                                                                     #
# Purpose:                                                            #
#   This is used to set the movement distance for the Z axis.         #
#######################################################################
    def Z_Idx_change_value(self,widget):

        self.ZIdx = widget.get_value()

        print("Z_Idx_chg_value =")
        print(self.ZIdx)

#######################################################################
# Z_Minus_on_button_press                                             #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Rotary                                            #
#   Button: Z_Idx_Minus (on click)                                    #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def Z_Minus_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 Z-" + str(self.ZIdx) + " F" + str(self.ZFeed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Z_Plus_on_button_press                                              #
#                                                                     #
# Called from:                                                        #
#   Panel:  REB_Tab_Rotary                                            #
#   Button: Z_Idx_Plus (on click)                                     #
#                                                                     #
# Purpose:                                                            #
#   This is used to stop the spindles.                                #
#######################################################################
    def Z_Plus_on_button_press(self,widget,data):

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 Z" + str(self.ZIdx) + " F" + str(self.ZFeed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

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

        self.halcomp        = halcomp
        self.builder        = builder
        self.nhits          = 0

        ###############################################################
        # Global variables - declare and set initial value.           #
        ###############################################################

        self.BFeed          = 10.0      # B axis feed rate
        self.BIdxDeg        = 90.0      # B axis index degrees
        self.BIdxDist       = 90.0      # B axis index distance
        self.BIdxDegDiv     = "Deg"     # B axis index by degrees or divisions
        self.BIdxQty        = 0         # B axis index amount

        self.Sp0Idx         = 90.0      # Sp0 index degrees
        self.Sp0Spd          = 1.0       # Sp0 Speed

        self.Sp1Idx         = 90.0      # Sp1 index degrees
        self.Sp1Pct         = 100.0     # Sp1 speed percentage of Sp0 speed

        self.UFeed          = 1.0       # U axis feed rate
        self.UIdx           = 0.0       # U axis index distance

        self.VFeed          = 1.0       # V axis feed rate
        self.VIdx           = 0.0       # V axis index distance

        self.XFeed          = 1.0       # X axis feed rate
        self.XIdx           = 0.0       # X axis index distance

        self.YFeed          = 1.0       # Y axis feed rate
        self.YIdx           = 0.0       # Y axis index distance

        self.ZFeed          = 1.0       # Z axis feed rate
        self.ZIdx           = 0.0       # Z axis index distance


def get_handlers(halcomp,builder,useropts):
    '''
    this function is called by gladevcp at import time (when this module is passed with '-u <modname>.py')

    return a list of object instances whose methods should be connected as callback handlers
    any method whose name does not begin with an underscore ('_') is a  callback candidate

    the 'get_handlers' name is reserved - gladevcp expects it, so do not change
    '''
    return [HandlerClass(halcomp,builder,useropts)]

#

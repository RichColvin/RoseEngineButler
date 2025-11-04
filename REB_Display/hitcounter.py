#######################################################################
#                    RRRRRR    EEEEEEEE  BBBBBBB                      #
#                    RR   RR   EE        BB    BB                     #
#                    RR   RR   EE        BB    BB                     #
#                    RRRRRR    EEEEEE    BBBBBBB                      #
#                    RR   RR   EE        BB    BB                     #
#                    RR    RR  EE        BB    BB                     #
#                    RR    RR  EEEEEEEE  BBBBBBB                      #
#                                                                     #
#                         Rose Engine Butler                          #
#######################################################################
# 
# LinuxCNC configuration for use with a Rose Engine
# 
# File:
#   hitcounter.py
#
# Purpose:  This is used to handle buttons used in panels developed
#   for Rose Engine Butler's use on LinuxCNC.
#
# End User Customisation:
#   THE END USER OF THE ROSE ENGINE BUTLER SYSTEM SHOULD NOT MODIFY
#   THIS FILE.
#
#   Changes to this file are not supported by Colvin Tools nor
#   Brainwave Embedded.
#
# Version
#   1.0 - 03 November 2025, R. Colvin
#
# Copyright (c) 2025 Colvin Tools and Brainwave Embedded.
#
# The following MIT/X Consortium License applies to the Rose Engine
# Butler system. Use of this system constitutes consent to the terms
# outlined below.
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
#       The above copyright notice and this permission notice shall be
#       included in all copies or substantial portions of the
#       Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Except as contained in this notice, the name of COPYRIGHT HOLDERS
# shall not be used in advertising or otherwise to promote the sale,
# use or other dealings in this Software without prior written
# authorization from COPYRIGHT HOLDERS.
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
# Axis B                                                              #
#######################################################################

#######################################################################
# B_Move_Idx_Fwd
# Purpose:              This is used to run the B axis forward using
#                       the G0 Gcode.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             B_Move_Idx_Fwd  (Hal_Button)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       BFeed - Feed rate set by user
#   Program Variables
#       Referenced:     (none)
#       Set:            BIdxQty - the quantity of indexes so far. 
#                           Forward increases this value.
#   Written to UI:      BIdxQty - the quantity of indexes so far. 
#                           Forward increases this value.
# ---------------------------------------------------------------------
# Gcodes Called:    (none)
#######################################################################
    def B_Move_Idx_Fwd(self,widget,data):

        print("=================================================")
        print("FUNCTION B_Move_Idx_Fwd")

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
# B_Move_Idx_Rev
# Purpose:              This is used to run the B axis in reverse using
#                       the G0 Gcode.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             B_Move_Idx_Rev  (Hal_Button)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       BFeed - Feed rate set by user
#   Program Variables
#       Referenced:     (none)
#       Set:            BIdxQty - the quantity of indexes so far. Reverse
#                           decreases this value.
#   Written to UI:      BIdxQty - the quantity of indexes so far. Reverse
#                           decreases this value.
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def B_Move_Idx_Rev(self,widget,data):

        print("=================================================")
        print("FUNCTION B_Move_Idx_Rev")

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
# B_Set_Idx_by_Deg
# Purpose:              This is used to set the rotational distance
#                       measurement as degrees for the B axis.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             B_Move_Idx_Deg  (HAL_RadioButton)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     BIdxDist - Distance set by user
#       Set:            BIdxDeg - Degrees to index during movement
#                       BIdxDegDiv - type of distance measurement 
#                           (Deg or Div)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def B_Set_Idx_by_Deg(self,widget,data):

        print("=================================================")
        print("FUNCTION B_Set_Idx_by_Deg")

        self.BIdxDeg = self.BIdxDist
        self.BIdxDegDiv = "Deg"

        Prt1 = "BIdxDegDiv = " + self.BIdxDegDiv
        print(Prt1)
        Prt2 = "BIdxDeg = " + str(self.BIdxDeg) + " deg"
        print(Prt2)


#######################################################################
# B_Set_Idx_by_Div
# Purpose:              This is used to set the rotational distance
#                       measurement as divisions of a circle for the B
#                       axis (deg = 360/div).
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             B_Move_Idx_Div  (HAL_RadioButton)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     BIdxDist - Distance set by user
#       Set:            BIdxDeg - Degrees to index during movement
#                       BIdxDegDiv - type of distance measurement
#                           (Deg or Div)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def B_Set_Idx_by_Div(self,widget,data):

        print("=================================================")
        print("FUNCTION B_Set_Idx_by_Div")

        self.BIdxDeg = 360 / self.BIdxDist

        self.BIdxDegDiv = "Div"

        Prt1 = "BIdxDegDiv = " + self.BIdxDegDiv
        print(Prt1)
        Prt2 = "BIdxDeg = " + str(self.BIdxDeg) + " deg"
        print(Prt2)


#######################################################################
# B_Set_Idx_Dist
# Purpose:              This is used to set the rotational distance 
#                       (degrees or divisions of a circle) for the B
#                       axis.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             B_Set_Idx_Dist  (HAL_SpinButton)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       B_Set_Idx_Dist
#   Program Variables
#       Referenced:     BIdxDist - Distance set by user
#       Set:            BIdxDeg - Degrees to index during movement
#                       BIdxDegDiv - type of distance measurement 
#                           (Deg or Div)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def B_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION B_Set_Idx_Dist")

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
# B_Set_Idx_Feed
# Purpose:              This is used to set the movement speed for the
#                       B axis.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary    (HAL_SpinButton)
#   Button:             B_Feed
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       BFeed - Feed rate set by user
#   Program Variables
#       Referenced: 
#       Set:            BFeed
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def B_Set_Idx_Feed(self,widget):

        print("=================================================")
        print("FUNCTION B_Set_Idx_Feed")

        self.BFeed = widget.get_value()

        Prt1 = "BFeed = " + str(self.BFeed)
        print(Prt1)


#######################################################################
# Spindle 0                                                           #
#######################################################################

#######################################################################
# Sp0_Move_Fwd
# Purpose:              This is used to start the spindles rotating 
#                       forward.
#                       Note:  this starts both Sp0 and Sp1.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Base
#   Button:             Sp0_Move_Fwd  (Hal_Button)
#	Signal:	            GtkButton/pressed
#			            GtkWidget/button-press-event
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            Sp0_Feed
#                       Sp1_Feed
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        S, M3
#######################################################################
    def Sp0_Move_Fwd(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Move_Fwd")

        # Ensure the system is in MDI mode
        c.mode(linuxcnc.MODE_MDI)
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Set the feed rates
        Sp1_Feed = self.Sp1Pct * self.Sp0_Feed / 100

        # Send an MDI command to set the spindles' speed.
        sSp0_Feed = "S" + str(self.Sp0_Feed) + " $0"
        sSp1_Feed = "S" + str(Sp1_Feed) + " $1"

        print(sSp0_Feed)
        c.mdi(sSp0_Feed)

        print(sSp1_Feed)
        c.mdi(sSp1_Feed)

        # Send an MDI command to start spindles rotating.
        Gcode = "M3 $-1"

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Move_Idx_Fwd
# Purpose:              This is used to index the Sp0 spindle in a 
#                           counter-clockwise direction.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button: S           p0_Idx_CCW
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Sp0Idx
#       Set:            (none)
#   Written to UI:      BIdxQty - the quantity of indexes so far. 
#                           Forward increases this value.
# ---------------------------------------------------------------------
# Gcodes Called:        M19
#######################################################################
    def Sp0_Move_Idx_Fwd(self,widget,data):

        print("=================================================")
        print("FUNCTION Sp0_Move_Idx_Fwd")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to start spindles rotating.
        sSp0_Feed = "M19 R" + str(self.Sp0Idx) + " P1 $0"
        c.mdi(sSp0_Feed)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Move_Rev
# Purpose:              This is used to start the spindles rotating in
#                           reverse.
#                       Note:  this starts both Sp0 and Sp1.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Base
#   Button:             Sp0_Move_Rev  (Hal_Button)
#	Signal:	            GtkButton/pressed
#			            GtkWidget/button-press-event
# ---------------------------------------------------------------------
# Data
#   Read from UI:       BFeed - Feed rate set by user
#   Program Variables
#       Referenced:     self.Sp0_Feed
#                       self.Sp1Pct
#       Set:            (none)
#   Written to UI:      BIdxQty - the quantity of indexes so far. 
#                           Forward increases this value.
# ---------------------------------------------------------------------
# Gcodes Called:    S, M4
#######################################################################
    def Sp0_Move_Rev(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Move_Rev")

        # Ensure the system is in MDI mode
        c.mode(linuxcnc.MODE_MDI)
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # In case the values had not already been written to the 
        # Gcode S values, write them.  
        Sp1_Feed = self.Sp1Pct * self.Sp0_Feed / 100

        # Send an MDI command to set the spindles' speed.
        sSp0_Feed = "S" + str(self.Sp0_Feed) + " $0"
        sSp1_Feed = "S" + str(Sp1_Feed) + " $1"

        print(sSp0_Feed)
        c.mdi(sSp0_Feed)

        print(sSp1_Feed)
        c.mdi(sSp1_Feed)

        # Send an MDI command to start spindles rotating.
        Gcode = "M4 $-1"

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Move_Stop
# Purpose:              This is used to stop the spindles rotating.
#                       Note:  this stops both Sp0 and Sp1.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Base
#   Button:             Sp0_Move_Stop  (Hal_Button)
#	Signal:	            GtkButton/pressed
#			            GtkWidget/button-press-event
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        M5
#######################################################################
    def Sp0_Move_Stop(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Move_Stop")

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
# Sp0_Set_Feed
# Purpose:                  This is used to set the speed for the 
#                               spindle (Sp0) & the rosette phaser 
#                               multiplier (Sp1).
# Updated:                  ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                     REB_Tab_Base
#   Button:                 Sp0_Set_Feed  (Hal_SpinButton)
#	Signal:	                GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:           Sp0_Feed from Sp0_Set_Feed
#   Program Variables
#       Referenced:         Sp1Pct
#       Set:                self.Sp0_Feed - the speed for the spindle
#                               (Sp0)
#   	   	                 Sp1_Feed - the speed for the rosette
#                               phaser multiplier (Sp1)
#   Written to UI:          (none)
# ---------------------------------------------------------------------
# Gcodes Called:            S
#######################################################################
    def Sp0_Set_Feed(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Set_Feed")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.Sp0_Feed = widget.get_value()
        Sp1_Feed = self.Sp1Pct * self.Sp0_Feed / 100

        # Send an MDI command to set the spindles' speed.
        sSp0_Feed = "S" + str(self.Sp0_Feed) + " $0"
        sSp1_Feed = "S" + str(Sp1_Feed) + " $1"

        print(sSp0_Feed)
        c.mdi(sSp0_Feed)

        print(sSp1_Feed)
        c.mdi(sSp1_Feed)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Set_Idx_Dist
# Purpose:              This is used to set the rotational distance
#                           (degrees) for the Sp0 spindle.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Sp0_Idx (on setting the value)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Sp0_Idx
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Sp0Idx
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        S
#######################################################################
    def Sp0_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Set_Idx_Dist")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.Sp0Idx = widget.get_value()


#######################################################################
# Spindle 1                                                           #
#######################################################################

#######################################################################
# Sp1_Set_Idx_Dist
# Purpose:              This is used to set the rotational distance 
#                           (degrees) for the Sp1 spindle (the 
#                           rosette phaser/multiplier).
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Sp1_Idx (on setting the value)
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Sp1_Idx
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Sp1Idx
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def Sp1_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION Sp1_Set_Idx_Dist")

        self.Sp1Idx = widget.get_value()

#######################################################################
# Sp1_Set_Move_Pct
# Purpose:              This is used to set the speed for the rosette 
#                           phaser / multiplier (Sp0) as a percentage 
#                           of the spindle speed.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Base
#   Button:             Sp1_Set_Move_Pct  (Hal_SpinButton)
#	Signal:	            GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Sp0_Feed
#       Set:            self.Sp1Pct
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        S
#######################################################################
    def Sp1_Set_Move_Pct(self,widget):

        print("=================================================")
        print("FUNCTION Sp1_Set_Move_Pct")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        self.Sp1Pct = widget.get_value()
        Sp1_Feed = self.Sp0_Feed * self.Sp1Pct / 100

        # Send an MDI command to set the spindles' speed.
        sSp1_Feed = "S" + str(Sp1_Feed) + " $1"

        print(sSp1_Feed)
        c.mdi(sSp1_Feed)

        # Wait for the command to complete
        c.wait_complete()


#######################################################################
# Axis U                                                              #
#######################################################################

#######################################################################
# U_Move_Minus
# Purpose:              This is used to index the U axis in the 
#                           minus direction.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             U_Idx_Minus
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.UFeed
#                       self.UIdx
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def U_Move_Minus(self,widget,data):

        print("=================================================")
        print("FUNCTION U_Move_Minus")

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
# U_Move_Plus
# Purpose:              This is used to index the U axis in the 
#                           plus direction.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             U_Idx_Plus
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.UFeed
#                       self.UIdx
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def U_Move_Plus(self,widget,data):

        print("=================================================")
        print("FUNCTION U_Move_Plus")

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
# U_Set_Feed
# Purpose:              This is used to set the movement speed for the
#                           U axis.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             U_Feed (on setting the value)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       U_Feed
#   Program Variables
#       Referenced:     (none)
#       Set:            self.UFeed
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def U_Set_Feed(self,widget):

        print("=================================================")
        print("FUNCTION BU_Set_Feed")

        self.UFeed = widget.get_value()

        print("U_Set_Feed =")
        print(self.UFeed)

#######################################################################
# U_Set_Idx_Dist
# Purpose:              This is used to set the movement distance for
#                           the U axis.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             U_Idx (on setting the value)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       U_Idx
#   Program Variables
#       Referenced:     (none)
#       Set:            self.UIdx
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def U_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION U_Set_Idx_Dist")

        self.UIdx = widget.get_value()

        print("U_Idx_chg_value =")
        print(self.UIdx)


#######################################################################
# Axis V                                                              #
#######################################################################

#######################################################################
# V_Move_Minus
# Purpose:              This is used to index the V axis in the 
#                           minus direction.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             V_Idx_Minus
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.VFeed
#                       self.VIdx
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def V_Move_Minus(self,widget,data):

        print("=================================================")
        print("FUNCTION V_Move_Minus")

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
# V_Move_Plus
# Purpose:              This is used to index the V axis in the 
#                           plus direction.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             V_Idx_Plus
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.VFeed
#                       self.VIdx
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def V_Move_Plus(self,widget,data):

        print("=================================================")
        print("FUNCTION V_Move_Plus")

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
# V_Set_Feed
# Purpose:              This is used to set the movement speed for the
#                           V axis.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             V_Feed (on setting the value)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       V_Feed
#   Program Variables
#       Referenced:     (none)
#       Set:            self.VFeed
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def V_Set_Feed(self,widget):

        print("=================================================")
        print("FUNCTION V_Set_Feed")

        self.VFeed = widget.get_value()

        print("V_Set_Feed =")
        print(self.VFeed)

#######################################################################
# V_Set_Idx_Dist
# Purpose:              This is used to set the movement distance for
#                           the V axis.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             V_Idx (on setting the value)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       V_Idx
#   Program Variables
#       Referenced:     (none)
#       Set:            self.VIdx
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def V_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION V_Set_Idx_Dist")

        self.VIdx = widget.get_value()

        print("V_Idx_chg_value =")
        print(self.VIdx)


#######################################################################
# Axis X                                                              #
#######################################################################

#######################################################################
# X_Move_Minus
# Purpose:              This is used to index the X axis in the 
#                           minus direction.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             X_Idx_Minus
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.XFeed
#                       self.XIdx
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def X_Move_Minus(self,widget,data):

        print("=================================================")
        print("FUNCTION X_Move_Minus")

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
# X_Move_Plus
# Purpose:              This is used to index the X axis in the 
#                           plus direction.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             X_Idx_Plus
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.XFeed
#                       self.XIdx
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def X_Move_Plus(self,widget,data):

        print("=================================================")
        print("FUNCTION _Move_Plus")

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
# X_Set_Feed
# Purpose:              This is used to set the movement speed for the
#                           X axis.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             X_Feed (on setting the value)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       X_Feed
#   Program Variables
#       Referenced:     (none)
#       Set:            self.XFeed
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def X_Set_Feed(self,widget):

        print("=================================================")
        print("FUNCTION X_Set_Feed")

        self.XFeed = widget.get_value()

        print("X_Set_Feed =")
        print(self.XFeed)

#######################################################################
# X_Set_Idx_Dist
# Purpose:              This is used to set the movement distance for
#                           the X axis.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             X_Idx (on setting the value)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       X_Idx
#   Program Variables
#       Referenced:     (none)
#       Set:            self.XIdx
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def X_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION X_Set_Idx_Dist")

        self.XIdx = widget.get_value()

        print("X_Idx_chg_value =")
        print(self.XIdx)


#######################################################################
# Axis Y                                                              #
#######################################################################

#######################################################################
# Y_Move_Minus
# Purpose:              This is used to index the Y axis in the 
#                           minus direction.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Y_Idx_Minus
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.YFeed
#                       self.YIdx
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def Y_Move_Minus(self,widget,data):

        print("=================================================")
        print("FUNCTION Y_Move_Minus")

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
# Y_Move_Plus
# Purpose:              This is used to index the Y axis in the 
#                           plus direction.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Y_Idx_Plus
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.YFeed
#                       self.YIdx
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def Y_Move_Plus(self,widget,data):

        print("=================================================")
        print("FUNCTION Y_Move_Plus")

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
# Y_Set_Feed
# Purpose:              This is used to set the movement speed for the
#                           Y axis.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             Y_Feed (on setting the value)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Y_Feed
#   Program Variables
#       Referenced:     (none)
#       Set:            self.YFeed
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        M5
#######################################################################
    def Y_Set_Feed(self,widget):

        print("=================================================")
        print("FUNCTION Y_Set_Feed")

        self.YFeed = widget.get_value()

        print("Y_Set_Feed =")
        print(self.YFeed)

#######################################################################
# Y_Set_Idx_Dist
# Purpose:              This is used to set the movement distance for 
#                           the Y axis.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             Y_Idx (on setting the value)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Y_Idx
#   Program Variables
#       Referenced:     self.YIdx
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        M5
#######################################################################
    def Y_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION B_Set_Idx_Dist_by_Deg")

        self.YIdx = widget.get_value()

        print("Y_Idx_chg_value =")
        print(self.YIdx)


#######################################################################
# Axis Z                                                              #
#######################################################################

#######################################################################
# Z_Move_Minus
# Purpose:              This is used to index the Z axis in the 
#                           minus direction.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Z_Idx_Minus
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.ZFeed
#                       self.ZIdx
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def Z_Move_Minus(self,widget,data):

        print("=================================================")
        print("FUNCTION Z_Move_Minus")

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
# Z_Move_Plus
# Purpose:              This is used to index the Z axis in the 
#                           plus direction.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Z_Idx_Plus
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.ZFeed
#                       self.ZIdx
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def Z_Move_Plus(self,widget,data):

        print("=================================================")
        print("FUNCTION Z_Move_Plus")

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
# Z_Set_Feed
# Purpose:              This is used to set the movement speed for the
#                           Z axis.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             Z_Feed (on setting the value)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Z_Feed
#   Program Variables
#       Referenced:     (none)
#       Set:            self.ZFeed
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        M5
#######################################################################
    def Z_Set_Feed(self,widget):

        print("=================================================")
        print("FUNCTION Z_Set_Feed")

        self.ZFeed = widget.get_value()

        print("Z_Set_Feed =")
        print(self.ZFeed)

#######################################################################
# Z_Set_Idx_Dist
# Purpose:              This is used to set the movement distance for 
#                           the Z axis.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             Z_Idx (on setting the value)
#	Signal:	
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Z_Idx
#   Program Variables
#       Referenced:     (none)
#       Set:            self.ZIdx
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        M5
#######################################################################
    def Z_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION Z_Set_Idx_Dist")

        self.ZIdx = widget.get_value()

        print("Z_Idx_chg_value =")
        print(self.ZIdx)

#######################################################################
# __init__
# Purpose:              This is used to initialize everything.
# Updated:              ver 1.0, 03 November 2025, R. Colvin
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
        # Global Program Variables - declare and set initial value.
        ###############################################################

        self.BFeed          = 10.0      # B axis feed rate
        self.BIdxDeg        = 90.0      # B axis index degrees
        self.BIdxDist       = 90.0      # B axis index distance
        self.BIdxDegDiv     = "Deg"     # B axis index by degrees or divisions
        self.BIdxQty        = 0         # B axis index amount

        self.Sp0Idx         = 90.0      # Sp0 index degrees
        self.Sp0_Feed          = 1.0       # Sp0 Speed

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

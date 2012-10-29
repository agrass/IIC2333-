import subprocess
import shlex
import sys

#!/usr/bin/env python

# example textview-basic.py

import pygtk
pygtk.require('2.0')
import gtk

class TextViewExample:
    def toggle_editable(self, checkbutton, textview):
        textview.set_editable(checkbutton.get_active())

    def toggle_cursor_visible(self, checkbutton, textview):
        textview.set_cursor_visible(checkbutton.get_active())

    def toggle_left_margin(self, checkbutton, textview):
        if checkbutton.get_active():
            textview.set_left_margin(50)
        else:
            textview.set_left_margin(0)

    def toggle_right_margin(self, checkbutton, textview):
        if checkbutton.get_active():
            textview.set_right_margin(50)
        else:
            textview.set_right_margin(0)

    def new_wrap_mode(self, radiobutton, textview, val):
        if radiobutton.get_active():
            textview.set_wrap_mode(val)

    def new_justification(self, radiobutton, textview, val):
        if radiobutton.get_active():
            textview.set_justification(val)

    def close_application(self, widget):
        gtk.main_quit()

    def insert(self, text):
        """ Insert text, apply tag, and scroll to end iter """
        buff = self.textbuffer
        end_iter = buff.get_end_iter()
        buff.insert(end_iter, "%s" % text)
        #while Gtk.events_pending():
        #    Gtk.main_iteration()

    def run(self, command):
        """ Run a command inserting output into the gtk.TextView """
        self.insert("Running: ")
        self.insert("%s\n" % command)
        args = shlex.split(command)
        output = None

        process = subprocess.Popen(args, 0, 
                                   shell=False, 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE)
        output = process.communicate()

        if output[0]:
            self.insert(output[0])
            self._last_output = output[0]
        if output[1]:
            self.insert(output[1], 'error')
        
        self.insert("\nExit: ", 'info')
        self.insert("%s\n\n" % process.returncode, 'bold')
        
        if output[1] and process.returncode <> 0:
            raise Exception(output[1])

    def runKernel(self, widget):
    	self.run("python main.py")

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_resizable(True)  
        window.connect("destroy", self.close_application)
        window.set_title("TextView Widget Basic Example")
        window.set_border_width(0)

        box1 = gtk.VBox(False, 0)
        window.add(box1)
        box1.show()

        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, True, True, 0)
        box2.show()

        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview = gtk.TextView()
        self.textbuffer = textview.get_buffer()
        sw.add(textview)
        sw.show()
        textview.show()

        box2.pack_start(sw)

        hbox = gtk.HButtonBox()
        box2.pack_start(hbox, False, False, 0)
        hbox.show()

        vbox = gtk.VBox()
        vbox.show()
        hbox.pack_start(vbox, False, False, 0)
        # check button to toggle editable mode
        check = gtk.CheckButton("Editable")
        vbox.pack_start(check, False, False, 0)
        check.connect("toggled", self.toggle_editable, textview)
        check.set_active(True)
        check.show()
        # check button to toggle cursor visiblity
        check = gtk.CheckButton("Cursor Visible")
        vbox.pack_start(check, False, False, 0)
        check.connect("toggled", self.toggle_cursor_visible, textview)
        check.set_active(True)
        check.show()
        # check button to toggle left margin
        check = gtk.CheckButton("Left Margin")
        vbox.pack_start(check, False, False, 0)
        check.connect("toggled", self.toggle_left_margin, textview)
        check.set_active(False)
        check.show()
        # check button to toggle right margin
        check = gtk.CheckButton("Right Margin")
        vbox.pack_start(check, False, False, 0)
        check.connect("toggled", self.toggle_right_margin, textview)
        check.set_active(False)
        check.show()
        # radio buttons to specify wrap mode
        vbox = gtk.VBox()
        vbox.show()
        hbox.pack_start(vbox, False, False, 0)
        radio = gtk.RadioButton(None, "WRAP__NONE")
        vbox.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.new_wrap_mode, textview, gtk.WRAP_NONE)
        radio.set_active(True)
        radio.show()
        radio = gtk.RadioButton(radio, "WRAP__CHAR")
        vbox.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.new_wrap_mode, textview, gtk.WRAP_CHAR)
        radio.show()
        radio = gtk.RadioButton(radio, "WRAP__WORD")
        vbox.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.new_wrap_mode, textview, gtk.WRAP_WORD)
        radio.show()

        # radio buttons to specify justification
        vbox = gtk.VBox()
        vbox.show()
        hbox.pack_start(vbox, False, False, 0)
        radio = gtk.RadioButton(None, "JUSTIFY__LEFT")
        vbox.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.new_justification, textview,
                      gtk.JUSTIFY_LEFT)
        radio.set_active(True)
        radio.show()
        radio = gtk.RadioButton(radio, "JUSTIFY__RIGHT")
        vbox.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.new_justification, textview,
                      gtk.JUSTIFY_RIGHT)
        radio.show()
        radio = gtk.RadioButton(radio, "JUSTIFY__CENTER")
        vbox.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.new_justification, textview,
                      gtk.JUSTIFY_CENTER)
        radio.show()

        separator = gtk.HSeparator()
        box1.pack_start(separator, False, True, 0)
        separator.show()

        box2 = gtk.VBox(False, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, False, True, 0)
        box2.show()

        button = gtk.Button("close")
        button.connect("clicked", self.close_application)
        box2.pack_start(button, True, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()

        button2 = gtk.Button("run")
        button2.connect("clicked", self.runKernel)
        box2.pack_start(button2, True, True, 0)
        button2.set_flags(gtk.CAN_DEFAULT)
        button2.grab_default()
        button2.show()

        window.show()



def main():
    gtk.main()
    return 0       

if __name__ == "__main__":
    TextViewExample()
    main()
#!/usr/bin/env python2

import pygtk
pygtk.require('2.0')
import gtk

from resize import resize

class Resizer(gtk.Window):

    def _destroy_cb(self, widget, *data):
        gtk.main_quit()

    def checkFields(self):
        ready = True

        if not self.inDirEntry.get_text():
            ready = False
        if not self.outDirEntry.get_text():
            ready = False
        if not self.xResEntry.get_text():
            ready = False
        if not self.yResEntry.get_text():
            ready = False

        self.procBtn.set_sensitive(ready)

    def __init__(self):
        
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        self.connect("destroy", self._destroy_cb)
        
        # Sets the border width of the window.
        #self.set_border_width(10)
    
        self.inDirBtn = gtk.Button("...")
        self.inDirBtn.connect("clicked", self._onInDirBtn)
        self.inDirEntry = gtk.Entry()
        self.inDirEntry.set_width_chars(40)
        self.inDirEntry.set_property("editable", False)
        self.inDirEntry.unset_flags(gtk.CAN_FOCUS)

        self.outDirBtn = gtk.Button("...")
        self.outDirBtn.connect("clicked", self._onOutDirBtn)
        self.outDirEntry = gtk.Entry()
        self.outDirEntry.set_width_chars(40)
        self.outDirEntry.set_property("editable", False)
        self.outDirEntry.unset_flags(gtk.CAN_FOCUS)

        self.xResEntry = gtk.Entry()
        self.xResEntry.set_width_chars(4)
        self.xResEntry.set_text("800")
        self.yResEntry = gtk.Entry()
        self.yResEntry.set_width_chars(4)
        self.yResEntry.set_text("600")

        self.procBtn = gtk.Button("Proced")
        self.procBtn.connect("clicked", self._onProcBtn)

        vbox = gtk.VBox()
        hbox = gtk.HBox()
        label = gtk.Label("Input Path:")
        label.set_justify(gtk.JUSTIFY_LEFT)
        label.set_width_chars(10)
        hbox.pack_start(label, False, False)
        hbox.pack_start(self.inDirEntry, False, False)
        hbox.pack_start(self.inDirBtn, False, False)
        vbox.pack_start(hbox, False, False)

        hbox2 = gtk.HBox()
        label = gtk.Label("Output Path:")
        label.set_justify(gtk.JUSTIFY_LEFT)
        label.set_width_chars(10)
        hbox2.pack_start(label, False, False)
        hbox2.pack_start(self.outDirEntry, False, False)
        hbox2.pack_start(self.outDirBtn, False, False)
        vbox.pack_start(hbox2, False, False)

        hbox3 = gtk.HBox()
        label = gtk.Label("Resolution:")
        label.set_justify(gtk.JUSTIFY_LEFT)
        label.set_width_chars(10)
        hbox3.pack_start(label, False, False)
        hbox3.pack_start(self.xResEntry, False, False)
        hbox3.pack_start(gtk.Label("x"), False, False)
        hbox3.pack_start(self.yResEntry, False, False)
        vbox.pack_start(hbox3, False, False)

        vbox.pack_start(self.procBtn, False, False)


        self.add(vbox)
    
        #self.button.connect("clicked", self.hello, None)
        self.checkFields()
        self.show_all()

    def _onInDirBtn(self, widget, *data):
        dialog = gtk.FileChooserDialog("Select input directory",
                                       None,
                                       gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
                                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                        gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)

        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            self.inDirEntry.set_text(dialog.get_filename())
        
        dialog.destroy()
        self.checkFields()


    def _onOutDirBtn(self, widget, *data):
        dialog = gtk.FileChooserDialog("Select output directory",
                                       None,
                                       gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
                                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                        gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)

        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            self.outDirEntry.set_text(dialog.get_filename())

        dialog.destroy()
        self.checkFields()

    def _onProcBtn(self, widget, *data):
        inDir = self.inDirEntry.get_text()
        outDir = self.outDirEntry.get_text()
        resX = self.xResEntry.get_text()
        resY = self.yResEntry.get_text()

        self.procBtn.set_sensitive(False)
        resize(inDir, outDir, resX, resY)
        self.procBtn.set_sensitive(True)


    def main(self):
        gtk.main()



if __name__ == "__main__":
    resizer = Resizer()
    resizer.main() 

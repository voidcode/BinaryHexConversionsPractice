#!/usr/bin/python3
from gi.repository import Gtk, Gdk
import os
from random import randint

class EventHandler():
	global binaryArray
	global labelDecimal
	global labelBinary
	global labelHex
	global r
	def __init__(self, builder):
		self.hexArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

		self.labelDecimal = builder.get_object('label_decimal')
		self.labelBinary = builder.get_object('label_binary')
		self.labelHex = builder.get_object('label_hex')

		self.r = randint(0,15)
		self.labelDecimal.set_text(str(self.r))
	def onShowNumbers(self, widget):
		self.labelDecimal.set_text(str(self.r))
		self.labelBinary.set_text(str(bin(self.r)[2:]))
		self.labelHex.set_text(self.hexArray[self.r])
	def onBtnNext(self, widget):
		self.r = randint(0,15)
		self.labelDecimal.set_text(str(self.r))
		self.labelBinary.set_text("?")
		self.labelHex.set_text("?")
class BinaryHexConversionsPractice:
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file(os.getcwd()+'/ui/viewer.glade')
		#self.bgColor = Gdk.RGBA.from_color(Gdk.color_parse('#4b4943'))

		self.window = builder.get_object('window_main')
		self.btnNext = builder.get_object('btn_next')

		eh = EventHandler(builder)

		self.labelBinary = builder.get_object('btn_next')
		self.btnShow = builder.get_object('btn_show')

		self.btnNext.connect('clicked', eh.onBtnNext)
		self.btnShow.connect('clicked', eh.onShowNumbers)

		self.window.set_title('Binary / Hex ConversionsPractice')
		self.window.set_icon_from_file(os.getcwd()+'/images/logo.png')
		#self.window.override_background_color(0, self.bgColor)
		self.window.connect('delete-event', Gtk.main_quit)
		self.window.show_all()
if __name__ == '__main__':
	mainWindow = BinaryHexConversionsPractice()
	Gtk.main()

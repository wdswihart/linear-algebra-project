# Gui represents a GUI object, for a Linear Algebra Project on fractal compression,
# using Python 2.7.
#
# William Swihart, Nick Phillips
# University of Central Arkansas
# Summer 2017

import sys
import os
import ctypes # Used to get screen resolution, to calc frame size
import wx # wxPython 3.0 amd-64 (made for Python 2.7)

frameWidth = ctypes.windll.user32.GetSystemMetrics(0) / 1.5 # Frame width will be 1/1.5 screen width,
frameHeight = ctypes.windll.user32.GetSystemMetrics(1) / 1.5 # 	and height will be 1/1.5 screen height

class Gui(wx.Frame):
	# FIELDS
	
	imgPath = '../../res/Lena.jpg' # Default image path

	# INITIALIZERS
	
	def initUI(self):
		# Add the status bar.
		self.CreateStatusBar()
		
		# Add the menu bar.
		self.menuBar = wx.MenuBar()
		
		# 	Add the File menu.
		self.fileMenu = wx.Menu()
		exitItem = self.fileMenu.Append(wx.ID_EXIT, 'Exit', 'Exit to Desktop')
		self.Bind(wx.EVT_MENU, self.onExit, exitItem) # Event binding for 'Exit to Desktop' File menu item.
		self.menuBar.Append(self.fileMenu, 'File')
		
		
		# 	Add the Help menu.
		self.helpMenu = wx.Menu()
		aboutItem = self.helpMenu.Append(wx.ID_ABOUT, 'About', 'About this program')
		self.Bind(wx.EVT_MENU, self.onAbout, aboutItem) # Event binding for 'About' File menu item.
		self.menuBar.Append(self.helpMenu, 'Help')
		
		# 	Add other menus (?).
		#TO-DO
		
		self.SetMenuBar(self.menuBar)
		
		# Add a container panel and horizontal box sizer.
		panel = wx.Panel(self)
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		
		# Add the image view.
		img = wx.Image(self.imgPath, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		hbox.Add(wx.StaticBitmap(self, -1, img, (10, 5), (img.GetWidth(), img.GetHeight()))
, 0, wx.ALIGN_CENTER)
		
		# Add the buttons in a vertical box sizer.
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		self.testBtn = wx.Button(panel, -1, "TEST")
		vbox.Add(self.testBtn, 0, wx.ALIGN_CENTER)
		self.testBtn.Bind(wx.EVT_BUTTON, self.onPress)
		
		hbox.Add(vbox, 1, wx.ALIGN_CENTER)
		
		# Set sizers.
		panel.SetSizer(hbox)
		
		# Set the size and orientation, and show the GUI.
		self.SetSize((frameWidth, frameHeight))
		self.Centre()
		self.Show(True)
		
	def _init_(self, parent, title):
		# super()
		wx.Frame._init_(self, parent, title=title, size=(frameWidth,frameHeight))
		
	# METHODS
	
	# onAbout is the behavior associated with the 'About' File menu option.
	# 	IN: self, event
	#	OUT: void
	def onAbout(self, evt):
		dlg = wx.MessageDialog(self, 'A fractal compression demonstration', 'About LA&M Project')
		dlg.ShowModal()
		dlg.Destroy()
		
	# onPress is the handler for button presses
	# 	IN: self, event
	# 	OUT: void
	def onPress(self, evt):
		print 'Label = ', evt.GetEventObject().GetLabel()
	
	# onQuit is the behavior associated with the 'Exit to Desktop' File menu option.
	# 	IN: self, event
	# 	OUT: void
	def onExit(self, evt):
		self.Close(True)
		
app = wx.App(False)
sys.stdout.write('Initializing GUI... ')
gui = Gui(None, wx.ID_ANY, 'LA&M Project')
gui.initUI()
print 'Done!'
print 'Running main loop...'
app.MainLoop()
print 'Done! Exiting now...'
	

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
from FractalEncoder import FractalEncoder # Custom fractal encoder
from FractalDecoder import FractalDecoder # Custom fractal decoder

# VARIABLE DECLARATION:

frameWidth = ctypes.windll.user32.GetSystemMetrics(0) / 1.5 # Frame width will be 1/1.5 screen width,
frameHeight = ctypes.windll.user32.GetSystemMetrics(1) / 1.5 # 	and height will be 1/1.5 screen height

# CLASSES:

class Gui(wx.Frame):
	"""
	Gui represents the GUI for the fractal compression demonstation.
	"""
	# Gui FIELDS:
	
	panel = None # Container for image view and buttons
	imgVBox = wx.BoxSizer(wx.VERTICAL) # Vertical BoxSizer for holding the image
	defaultImgPath = '../../res/Lena.jpg' # Default image path

	# Gui INITIALIZERS:
	
	def initUI(self):
		"""
		initUI initializes UI components, because we couldn't get it to work in the initializer.
			IN: self
			OUT: void
		"""
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
		self.panel = wx.Panel(self)
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		
		# Add the image view, in a vertical box sizer.
		self.draw(self.defaultImgPath)
		hbox.Add(self.imgVBox, 0, wx.ALIGN_CENTER)
		
		# Add the buttons, in a vertical box sizer.
		btnVBox = wx.BoxSizer(wx.VERTICAL)
		
		ubuntuBtn = wx.Button(self.panel, -1, "UBUNTU") # (ubuntuBtn because the pictures is a joke on Ubuntu Touch)
		ubuntuBtn.Bind(wx.EVT_BUTTON, self.onPress)
		btnVBox.Add(ubuntuBtn, 0, wx.ALIGN_CENTER)
		
		fernBtn = wx.Button(self.panel, -1, 'FERN')
		fernBtn.Bind(wx.EVT_BUTTON, self.onPress)
		btnVBox.Add(fernBtn, 1, wx.ALIGN_CENTER)
		
		defaultBtn = wx.Button(self.panel, -1, 'DEFAULT')
		defaultBtn.Bind(wx.EVT_BUTTON, self.onPress)
		btnVBox.Add(defaultBtn, 2, wx.ALIGN_CENTER)
		
		hbox.Add(btnVBox, 1, wx.ALIGN_CENTER)
		
		# Set sizers.
		self.panel.SetSizer(hbox)
		
		# Set the size and orientation, and show the GUI.
		self.SetSize((frameWidth, frameHeight))
		self.Centre()
		self.Show(True)
		
	def _init_(self, parent, title):
		# super()
		wx.Frame._init_(self, parent, title=title, size=(frameWidth,frameHeight))
		
	# Gui METHODS:
	
	def draw(self, path):
		""" 
		draw redraws the image view with the given image path.
			IN: self
			OUT: void 
		"""
		self.imgVBox.Clear(True)
		img = wx.Image(path, wx.BITMAP_TYPE_ANY)
		scale = (frameWidth / img.GetWidth()) / 2.5
		img = img.Scale(img.GetWidth() * scale, img.GetHeight() * scale, 1).ConvertToBitmap()
		self.imgVBox.Add(wx.StaticBitmap(self.panel, -1, img, (0,0), (img.GetWidth(), img.GetHeight())), 0, wx.ALIGN_CENTER)
	
	# Gui HANDLERS:
	
	def onAbout(self, evt):
		"""
		onAbout is the behavior associated with the 'About' File menu option.
			IN: self, event
			OUT: void
		"""
		dlg = wx.MessageDialog(self, 'A fractal compression demonstration', 'About LA&M Project')
		dlg.ShowModal()
		dlg.Destroy()
		
	def onPress(self, evt):
		"""
		onPress is the handler for button presses
			IN: self, event
			OUT: void
		"""
		# Get the label of the event sender.
		label = evt.GetEventObject().GetLabel()
		
		# Check the label:
		if label == 'UBUNTU':
			self.draw('../../res/linuxandroid.png') # ('Ubuntu Touch'-related picture)
		elif label == 'FERN':
			self.draw('../../res/fractal_fern.png')
		if label == 'DEFAULT':
			self.draw(self.defaultImgPath)
		print evt.GetEventObject().GetLabel(), ' event handled.'
	
	def onExit(self, evt):
		"""
		onQuit is the behavior associated with the 'Exit to Desktop' File menu option.
			IN: self, event
			OUT: void
		"""
		self.Close(True)
		
# MAIN:

app = wx.App(False)
sys.stdout.write('Initializing GUI... ')
gui = Gui(None, wx.ID_ANY, 'LA&M Project')
gui.initUI()
print 'Done!'
print 'Running main loop...'
app.MainLoop()
print 'Done! Exiting now...'
	

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
resPath = '../../res/'
defaultImg = 'Lena.jpg'
ubuntuImg = 'Ubuntu.png'
fernImg = 'Fern.png'

# CLASSES:

class Gui(wx.Frame):
	"""
	Gui represents the GUI for the fractal compression demonstation.
	"""
	# Gui FIELDS:
	
	statusBar = None # Status bar at the bottom of the frame
	panel = None # Container for image view and buttons
	hbox = wx.BoxSizer(wx.HORIZONTAL) # Sizer for panel (above)
	leftVBox = wx.BoxSizer(wx.VERTICAL) # Sizer for left side of frame
	rightVBox = wx.BoxSizer(wx.VERTICAL) # Sizer for right side of frame
	leftImgVBox = wx.BoxSizer(wx.VERTICAL) # Vertical BoxSizer for holding the image (ImageView)
	rightImgVBox = wx.BoxSizer(wx.VERTICAL) # Vertical BoxSizer for holding images on the right

	# Gui INITIALIZERS:
	
	def addButtons(self):
		ubuntuBtn = wx.Button(self.panel, -1, 'Ubuntu')
		ubuntuBtn.Bind(wx.EVT_BUTTON, self.onPress)
		self.rightVBox.Add(ubuntuBtn, 0, wx.ALIGN_CENTER)
		
		fernBtn = wx.Button(self.panel, -1, 'Fern')
		fernBtn.Bind(wx.EVT_BUTTON, self.onPress)
		self.rightVBox.Add(fernBtn, 1, wx.ALIGN_CENTER)
		
		defaultBtn = wx.Button(self.panel, -1, 'Default')
		defaultBtn.Bind(wx.EVT_BUTTON, self.onPress)
		self.rightVBox.Add(defaultBtn, 2, wx.ALIGN_CENTER)
	
	def initUI(self):
		"""
		initUI initializes UI components, because we couldn't get it to work in the initializer.
			IN: self
			OUT: void
		"""
		# Add the status bar.
		self.statusBar = self.CreateStatusBar()
		
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
		
		# Init the container panel and horizontal box sizer.
		self.panel = wx.Panel(self)
		
		# Init the image view, in the left vertical box sizer.
		path = resPath + defaultImg
		self.leftImgVBox = self.draw(path)
		self.leftVBox.Add(self.leftImgVBox, 0, wx.ALIGN_CENTER)
		
		# Add the 'Fractalize' button on the left vertical box sizer.
		fractalBtn = wx.Button(self.panel, -1, 'Fractalize!')
		fractalBtn.Bind(wx.EVT_BUTTON, self.onPress)
		self.leftVBox.Add(fractalBtn, 1, wx.ALIGN_CENTER)
		
		self.hbox.Add(self.leftVBox, 0, wx.ALIGN_CENTER)
		
		# Add the buttons, in the right vertical box sizer.
		self.addButtons()
		self.hbox.Add(self.rightVBox, 1, wx.ALIGN_CENTER)
		
		# Set sizer.
		self.panel.SetSizer(self.hbox)
		
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
		draw updates imgVBox (the image view) with a new filepath.
			IN: self
			OUT: void 
		"""
		imgVBox = wx.BoxSizer(wx.VERTICAL)
		img = wx.Image(path, wx.BITMAP_TYPE_ANY)
		scale = (frameWidth / img.GetWidth()) / 2.5
		img = img.Scale(img.GetWidth() * scale, img.GetHeight() * scale, 1).ConvertToBitmap()
		bmp = wx.StaticBitmap(self.panel, -1, img, (0,0), (img.GetWidth(), img.GetHeight()))
		imgVBox.Add(bmp, 0, wx.ALIGN_CENTER)
		return imgVBox
		
	
	# Gui HANDLERS:
	
	def onAbout(self, evt):
		"""
		onAbout is the handler associated with the 'About' File menu option.
			IN: self, event
			OUT: void
		"""
		dlg = wx.MessageDialog(self, 'A fractal compression demonstration', 'About LA&M Project')
		dlg.ShowModal()
		dlg.Destroy()
		
	def onMouseOver(self, evt):
		"""
		onMouseOver is the handler for mouse over events.
		"""
		# Display the filename in the status bar.
		
		
	def onPress(self, evt):
		"""
		onPress is the handler for button presses
			IN: self, event
			OUT: void
		"""
		# Get the label of the event sender.
		label = evt.GetEventObject().GetLabel()
		
		# Check the label:
		if label == 'Ubuntu':
			self.leftImgVBox.Clear(True)
			sys.stdout.write('Drawing ' + ubuntuImg + '... ')
			path = resPath + ubuntuImg
			self.leftImgVBox = self.draw(path)
		elif label == 'Fern':
			self.leftImgVBox.Clear(True)
			sys.stdout.write('Drawing ' + fernImg + '... ')
			path = resPath + fernImg
			self.leftImgVBox = self.draw(path)
		elif label == 'Default':
			self.leftImgVBox.Clear(True)
			sys.stdout.write('Drawing ' + defaultImg + '... ')
			path = resPath + defaultImg
			self.leftImgVBox = self.draw(path)
		elif label == 'Fractalize!':
			self.rightVBox.Clear(True)
			sys.stdout.write('Handling ' + evt.GetEventObject().GetLabel() + ' event... ')
			self.rightVBox.Add(self.leftImgVBox, 0, wx.ALIGN_CENTER)
			backBtn = wx.Button(self.panel, -1, '<-- Back')
			backBtn.Bind(wx.EVT_BUTTON, self.onPress)
			self.rightVBox.Add(backBtn, 1, wx.ALIGN_CENTER)
			self.hbox.Add(self.rightVBox, 1, wx.ALIGN_CENTER)
			
		print 'Done!'
	
	def onExit(self, evt):
		"""
		onQuit is the behavior associated with the 'Exit to Desktop' File menu option.
			IN: self, event
			OUT: void
		"""
		sys.stdout.write('Closing now...')
		self.Close()
		
# MAIN:

app = wx.App()
sys.stdout.write('Initializing GUI... ')
gui = Gui(None, wx.ID_ANY, 'LA&M Project')
gui.initUI()
print 'Done!'
print 'Running main loop...'
app.MainLoop()
print 'Done!'
	

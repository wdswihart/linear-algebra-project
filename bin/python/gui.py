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
#from FractalEncoder import FractalEncoder # Custom fractal encoder
#from FractalDecoder import FractalDecoder # Custom fractal decoder

# VARIABLE DECLARATION:

frameWidth = ctypes.windll.user32.GetSystemMetrics(0) / 1.5 # Frame width will be 1/1.5 screen width,
frameHeight = ctypes.windll.user32.GetSystemMetrics(1) / 1.5 # 	and height will be 1/1.5 screen height
resPath = '../../res/'
defaultImg = 'Default.jpg'
ubuntuImg = 'Ubuntu.png'
fernImg = 'Fern.png'

# CLASSES:

class Gui(wx.Frame):
	"""
	Gui represents the GUI for the fractal compression demonstation.
	"""
	
	# Gui FIELDS:

	statusBar = None # Status bar at the bottom of the frame
	panel = None # Container for left and right vboxes
	
	menuBar = None
	fileMenu = None
	exitItem = None
	helpMenu = None
	aboutItem = None
	
	fractalBtn = None
	defaultBtn = None
	fernBtn = None
	ubuntuBtn = None
	backBtn = None
	
	hbox = wx.BoxSizer(wx.HORIZONTAL) # Sizer for panel (above)
	leftVBox = wx.BoxSizer(wx.VERTICAL) # Sizer for left side of frame
	rightVBox = wx.BoxSizer(wx.VERTICAL) # Sizer for right side of frame
<<<<<<< HEAD
	leftImgView = wx.BoxSizer(wx.VERTICAL) # Vertical BoxSizer for holding the image (ImageView)
	rightImgView = wx.BoxSizer(wx.VERTICAL) # Vertical BoxSizer for holding images on the right

	# Gui INITIALIZERS:
	
	def reset(self):
		"""
		reset resets the GUI, which is then suitable for redrawing.
			IN: self
			OUT: void
		"""
		self.hbox = None
		self.panel = None
		self.leftVBox = None
		self.rightVBox = None
		self.rightImgView = None
		self.leftImgView = None
		
		self.fractalBtn = None
		self.defaultBtn = None
		self.fernBtn = None
		self.ubuntuBtn = None
		self.backBtn = None
	
	def draw(self):
=======
	imgVBox = wx.BoxSizer(wx.VERTICAL) # Vertical BoxSizer for holding the image (ImageView)
	defaultImgPath = '../../res/Lena.jpg' # Default image path
	
	# Gui INITIALIZERS:

	def initUI(self):
>>>>>>> will-edit
		"""
		draw adds the left and right vboxes into the hbox, and adds it to the panel.
			IN: self
			OUT: void
		"""
<<<<<<< HEAD
		align = wx.EXPAND
		
		self.hbox = wx.BoxSizer(wx.HORIZONTAL)
		
		self.hbox.Add(self.leftVBox, 0, align)
		self.hbox.Add(self.rightVBox, 1, align)
		
		# Set the sizer.
		self.panel.SetSizer(self.hbox)
	
	def drawImageView(self):
		"""
		drawImageView draws the image view and 'Fractalize!' button.
			IN: self
			OUT: void
		"""
		align = wx.EXPAND # Alignment for left-side items
		
		# Store right side, and reset.
		rightTemps = (self.rightVBox, self.rightImgView)
		self.reset()
		
		# Draw image view.
		self.panel = wx.Panel(self) # Init panel.
		self.leftVBox = wx.BoxSizer(wx.HORIZONTAL) # Init left vbox.
		self.leftImgView = wx.BoxSizer(wx.VERTICAL) # Init left image view.
		
		path = resPath + defaultImg # Default path
		self.leftImgView.Add(self.getImgView(path), 0, align)
		self.leftVBox.Add(self.leftImgView, 0, align)
		
		# Draw 'Fractalize!' button.
		self.fractalBtn = wx.Button(self.panel, -1, 'Fractalize!')
		self.fractalBtn.Bind(wx.EVT_BUTTON, self.onPress)
		self.leftVBox.Add(self.fractalBtn, 1, align)
		
		# Add the stored right side back in and draw the panel.
		self.rightVBox = rightTemps[0]
		self.rightImgView = rightTemps[1]
		self.draw()
		
	def drawButtons(self):
		"""
		drawButtons draws the buttons for the right vbox.
			IN: self
			OUT: void
		"""
		align = wx.EXPAND # Align for right-side items.
		
		# Store left side and reset.
		leftTemps = (self.leftVBox, self.leftImgView)
		self.reset()
		
		# Add the buttons.
		self.panel = wx.Panel(self) # Init panel.
		self.rightVBox = wx.BoxSizer(wx.VERTICAL) # Init right vbox.
		
		self.ubuntuBtn = wx.Button(self.panel, -1, 'Ubuntu')
		self.ubuntuBtn.Bind(wx.EVT_BUTTON, self.onPress)
		self.rightVBox.Add(self.ubuntuBtn, 0, align)
		
		self.fernBtn = wx.Button(self.panel, -1, 'Fern')
		self.fernBtn.Bind(wx.EVT_BUTTON, self.onPress)
		self.rightVBox.Add(self.fernBtn, 1, align)
		
		self.defaultBtn = wx.Button(self.panel, -1, 'Default')
		self.defaultBtn.Bind(wx.EVT_BUTTON, self.onPress)
		self.rightVBox.Add(self.defaultBtn, 2, align)
		
		# Add the left temps back in and draw the panel.
		self.leftVBox = leftTemps[0]
		self.leftImgView = leftTemps[1]
		self.draw()
	
	def drawMenuBar(self):
		# Add menu bar.
=======
		# Add the status bar.
		self.statusBar = self.CreateStatusBar()

		# Add the menu bar.
>>>>>>> will-edit
		self.menuBar = wx.MenuBar()
		
		# 	Add File menu.
		self.fileMenu = wx.Menu()
		self.exitItem = self.fileMenu.Append(wx.ID_EXIT, 'Exit', 'Exit to Desktop')
		self.Bind(wx.EVT_MENU, self.onExit, self.exitItem)
		self.menuBar.Append(self.fileMenu, 'File')
		
		# 	Add Help menu, then set the menu bar.
		self.helpMenu = wx.Menu()
		self.aboutItem = self.helpMenu.Append(wx.ID_ABOUT, 'About', 'About this program')
		self.Bind(wx.EVT_MENU, self.onAbout, self.aboutItem)
		self.menuBar.Append(self.helpMenu, 'Help')
<<<<<<< HEAD
		
		self.SetMenuBar(self.menuBar)
	
	def initUI(self):
		"""
		initUI initializes UI components, because we couldn't get it to work in the initializer.
			IN: self
			OUT: void
		"""
		# Set size.
		self.SetSize((frameWidth, frameHeight))
		
		# Add status bar.
		self.statusBar = self.CreateStatusBar()
		
		# Add menu bar.
		self.drawMenuBar()
		
		# Init left-side panel; init image view, and add 'Fractalize!' button.
		self.drawImageView()
		
		# Init right-side panel; init the buttons.
		self.drawButtons()
		
		# Set orientation and show GUI.
		self.Centre()
		self.Show()
		
=======

		# 	Add other menus (?)
		#TO-DO

		self.SetMenuBar(self.menuBar)

		# Init the container panel and horizontal box sizer.
		self.panel = wx.Panel(self)

		# Init the image view, in the left vertical box sizer.
		self.setImgView(self.defaultImgPath)
		self.leftVBox.Add(self.imgVBox, 0, wx.ALIGN_CENTER)

		# Add the 'Fractalize' button on the left vertical box sizer.
		fractalBtn = wx.Button(self.panel, -1, 'Fractalize!')
		fractalBtn.Bind(wx.EVT_BUTTON, self.onPress)
		self.leftVBox.Add(fractalBtn, 1, wx.ALIGN_CENTER)
		self.hbox.Add(self.leftVBox, 0, wx.ALIGN_CENTER)

		# Add the buttons, in the right vertical box sizer.
		self.rightVBox = wx.BoxSizer(wx.VERTICAL)
		ubuntuBtn = wx.Button(self.panel, -1, 'Ubuntu')
		ubuntuBtn.Bind(wx.EVT_BUTTON, self.onPress)
		self.rightVBox.Add(ubuntuBtn, 0, wx.ALIGN_CENTER)
		fernBtn = wx.Button(self.panel, -1, 'Fern')
		fernBtn.Bind(wx.EVT_BUTTON, self.onPress)
		self.rightVBox.Add(fernBtn, 1, wx.ALIGN_CENTER)
		defaultBtn = wx.Button(self.panel, -1, 'Default')
		defaultBtn.Bind(wx.EVT_BUTTON, self.onPress)
		self.rightVBox.Add(defaultBtn, 2, wx.ALIGN_CENTER)
		self.hbox.Add(self.rightVBox, 1, wx.ALIGN_CENTER)

		# Set sizer.
		self.panel.SetSizer(self.hbox)

		# Set the size and orientation, and show the GUI.
		self.SetSize((frameWidth, frameHeight))
		self.Centre()
		self.Show(True)

>>>>>>> will-edit
	def _init_(self, parent, title):
		# super()
		wx.Frame._init_(self, parent, title=title, size=(frameWidth,frameHeight))

	# Gui METHODS:
<<<<<<< HEAD
	
	def getImgView(self, path):
=======

	def setImgView(self, path):
>>>>>>> will-edit
		""" 
		draw updates imgVBox (the image view) with a new filepath.
			IN: self
			OUT: the image view that was created 
		"""
<<<<<<< HEAD
		imgView = wx.BoxSizer(wx.VERTICAL)
		img = wx.Image(path, wx.BITMAP_TYPE_ANY)
		scale = (frameWidth / img.GetWidth()) / 2.5
		bmp = img.Scale(img.GetWidth() * scale, img.GetHeight() * scale, 1).ConvertToBitmap()
		bmp = wx.StaticBitmap(self.panel, -1, bmp, (5,10), (img.GetWidth(), img.GetHeight()))
		imgView = wx.BoxSizer(wx.VERTICAL)
		imgView.Add(bmp, 0, wx.EXPAND)
		return imgView
	
=======
		self.imgVBox.Clear(True)
		img = wx.Image(path, wx.BITMAP_TYPE_ANY)
		scale = (frameWidth / img.GetWidth()) / 2.5
		img = img.Scale(img.GetWidth() * scale, img.GetHeight() * scale, 1).ConvertToBitmap()
		bmp = wx.StaticBitmap(self.panel, -1, img, (0,0), (img.GetWidth(), img.GetHeight()))
		self.imgVBox.Add(bmp, 0, wx.ALIGN_CENTER)
		
>>>>>>> will-edit
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
<<<<<<< HEAD
			self.leftVBox.Clear()
			sys.stdout.write('Drawing ' + ubuntuImg + '... ')
			path = resPath + ubuntuImg
			self.leftImgVBox.Add(self.draw(path), 0, wx.ALIGN_CENTER)
			self.leftVBox.Add(self.leftImgVBox, 0, wx.ALIGN_CENTER)
		elif label == 'Fern':
			self.leftVBox.Clear()
			sys.stdout.write('Drawing ' + fernImg + '... ')
			path = resPath + fernImg
			self.leftImgVBox.Add(self.draw(path), 0, wx.ALIGN_CENTER)
			self.leftVBox.Add(self.leftImgVBox, 0, wx.ALIGN_CENTER)
		elif label == 'Default':
			self.leftVBox.Clear()
			sys.stdout.write('Drawing ' + defaultImg + '... ')
			path = resPath + defaultImg
			self.leftImgVBox.Add(self.draw(path), 0, wx.ALIGN_CENTER)
			self.leftVBox.Add(self.leftImgVBox, 0, wx.ALIGN_CENTER)
		elif label == 'Fractalize!':
			self.rightVBox.Clear()
			sys.stdout.write('Handling ' + evt.GetEventObject().GetLabel() + ' event... ')
			self.rightVBox.Add(self.leftImgVBox, 0, wx.ALIGN_CENTER)
			backBtn = wx.Button(self.panel, -1, '<-- Back')
			backBtn.Bind(wx.EVT_BUTTON, self.onPress)
			self.rightVBox.Add(backBtn, 1, wx.ALIGN_CENTER)
=======
			sys.stdout.write('Drawing ' + ubuntuImg + '... ')
			self.setImgView(resPath + ubuntuImg)
		elif label == 'Fern':
			sys.stdout.write('Drawing ' + '... ')
			self.setImgView(resPath + fernImg)
		elif label == 'Default':
			sys.stdout.write('Drawing ' + defaultImg + '... ')
			self.setImgView(resPath + defaultImg)
		elif label == 'Fractalize!':
			sys.stdout.write('Handling ' + evt.GetEventObject().GetLabel() + ' event... ')
>>>>>>> will-edit
			
		print 'Done!'
	
	def onExit(self, evt):
		"""
		onQuit is the behavior associated with the 'Exit to Desktop' File menu option.
			IN: self, event
			OUT: void
		"""
<<<<<<< HEAD
		self.statusBar.SetStatusMessage('Exiting...')
=======
		sys.stdout.write('Closing now... ')
>>>>>>> will-edit
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

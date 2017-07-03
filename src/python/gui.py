# Gui represents a GUI object, for a Linear Algebra Project on fractal compression,
# using Python 2.7.
#
# William Swihart, Nick Phillips
# University of Central Arkansas
# Summer 2017

import wx # wxPython 3.0 amd-64 (made for Python 2.7)

class Gui(wx.Frame):
	# INITIALIZERS
	
	def initUI(self):
		menuBar = wx.MenuBar()
		
		fileMenu = wx.Menu()
		exitItem = fileMenu.Append(wx.ID_EXIT, 'Exit', 'Exit to Desktop')
		menuBar.Append(fileMenu, 'File')
		self.SetMenuBar(menuBar)
		
		self.Bind(wx.EVT_MENU, self.OnQuit, exitItem)
		
		self.SetSize(800, 400)
		self.SetTitle('Fractal Compression')
		self.Centre()
		self.Show()
	
	def _init_(self, parent, title):
		super(Gui, self)._init_(parent, title)
		self.initUI()
		
	# METHODS
		
	def OnQuit(self, e):
		self.Close()

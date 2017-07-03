# gui is the GUI implementation for the project in Linear Algebra,
# using Python 2.7.
#
# William Swihart
# University of Central Arkansas
# Summer 2017

import wx # wxPython 3.0 amd-64 (made for Python 2.7)

def initComponents():
	app = wx.App()
	frame = wx.Frame(None, -1, 'Fractal Compression')
	frame.Show()
	return app, frame

app, frame = initComponents()

app.MainLoop()

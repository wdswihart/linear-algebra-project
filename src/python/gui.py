# gui is the GUI implementation for the project in Linear Algebra,
# using Python 2.7.
#
# William Swihart, Nick Phillips
# University of Central Arkansas
# Summer 2017

import wx # wxPython 3.0 amd-64 (made for Python 2.7)

# FUNCTIONS

# initComponents initializes the frame.
#	IN: void
#	OUT: the app and the frame
def initComponents():
	app = wx.App()
	frame = wx.Frame(None, -1, 'Fractal Compression')
	frame.Show()
	return app, frame

# MAIN

# Create the app and the frame.
app, frame = initComponents()

# Start the main loop.
app.MainLoop()

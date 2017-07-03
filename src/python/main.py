# main contains the implementation of a fractal compression program for a Linear Algebra class,
# using Python 2.7.
#
# William Swihart, Nick Phillips
# University of Central Arkansas
# Summer 2017

from Gui import Gui
import wx # wxPython 3.0 amd-64 (made for Python 2.7)

# Create the app.
app = wx.App()

# Create the GUI.
print 'Initializing GUI...'
gui = Gui(None, -1, 'Fractal Compression')
gui.Show()
print 'Done!'

# Start the main loop.
print 'Running MainLoop...'
app.MainLoop()

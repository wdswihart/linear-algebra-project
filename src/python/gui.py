# gui is the GUI implementation for the project in Linear Algebra.
#
# William Swihart
# University of Central Arkansas
# Summer 2017

import wx # wxPython 3.0 amd-64

app = wx.App()

frame = wx.Frame(None, -1, 'Fractal Compression')
frame.Show()

app.MainLoop()

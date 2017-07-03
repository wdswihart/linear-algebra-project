# gui contains the GUI implementation for the Linear Algebra project on fractal compression.
#
# William Swihart
# University of Central Arkansas
# June-July 2017

import wx

app = wx.App()

frame = wx.Frame(None, -1, 'Fractal Compression')
frame.Show()

app.MainLoop()

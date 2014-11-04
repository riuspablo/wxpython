#! /usr/bin/env python
#coding=utf-8

import wx

# Create an application class instance
app = wx.App()

for space in [0, 5, 10]:
    frame = wx.Frame(None, -1, 'Test', style=wx.CAPTION|wx.RESIZE_BORDER|wx.CLOSE_BOX)
    child = wx.Button(frame, -1, 'Button')
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(child, 0, wx.ALL, space)
    frame.SetSizerAndFit(sizer)

    # Show the frame on screen
    frame.Show()

# Enter the application main loop
app.MainLoop()

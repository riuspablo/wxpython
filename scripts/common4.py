#! /usr/bin/env python
#coding=utf-8

import wx

# Create an application class instance
app = wx.App()

frame = wx.Frame(None, -1, 'Test')
panel = wx.Panel(frame)
sizer = wx.BoxSizer(wx.HORIZONTAL)

button1 = wx.Button(panel, -1, 'OK') 
sizer.Add(button1, 1, wx.ALL, 10)

button2 = wx.Button(panel, -1, 'OK') 
sizer.Add(button2, 0, wx.TOP|wx.BOTTOM, 10)

button3 = wx.Button(panel, -1, 'OK') 
sizer.Add(button3, 0, wx.ALL, 10)

panel.SetSizer(sizer)
sizer.SetSizeHints(panel)
frame.Fit()
# Show the frame on screen
frame.Show()

# Enter the application main loop
app.MainLoop()

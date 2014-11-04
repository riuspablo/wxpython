#! /usr/bin/env python
#coding=utf-8

import wx

# Create an application class instance
app = wx.App()

# Create a frame (i.e., a floating top-level window)
frame = wx.Frame(None, -1, 'Hello world')

# Show the frame on screen
frame.Show()

# Enter the application main loop
app.MainLoop()

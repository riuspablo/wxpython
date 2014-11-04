#! /usr/bin/env python
#coding=utf-8

import wx

class MainWindow(wx.Frame):

    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, title=title)

        # Bind a "paint" event for the frame to the
        # "OnPaint" method
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Show()


    def OnPaint(self, event):

        dc = wx.PaintDC(self)        

app = wx.App(False)
frame = MainWindow(None, 'DC exercise')
app.MainLoop()

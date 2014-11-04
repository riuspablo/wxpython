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

        # Use a big font for the text...
        font = wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD)
        # Inform the DC we want to use that font
        dc.SetFont(font)

        # Draw our text onto the DC
        dc.DrawText('Hello World', 10, 10)
        

app = wx.App(False)
frame = MainWindow(None, 'Paint events')
app.MainLoop()

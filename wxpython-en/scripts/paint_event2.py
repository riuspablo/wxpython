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

        # Set a white background
        dc.SetBackground(wx.WHITE_BRUSH)
        dc.Clear()
        
        # Use a red pen to draw the points
        dc.SetPen(wx.Pen('RED'))

        # Get the size of the area inside the main window
        w, h = self.GetClientSize()
        # Draw a sequence of points along the mid line
        for x in range(1, w, 3):
            dc.DrawPoint(x, h/2)
        

app = wx.App(False)
frame = MainWindow(None, 'Paint events')
app.MainLoop()

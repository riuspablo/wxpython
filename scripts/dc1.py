#! /usr/bin/env python
#coding=utf-8

import wx
import random

class Exercise1(wx.Frame):

    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, title=title)

        # Bind a "paint" event for the frame to the
        # "OnPaint" method
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Show()


    def OnPaint(self, event):

        dc = wx.PaintDC(self)        
        w, h = self.GetClientSize()

        # Use a blue pen, for example...

        dc.SetPen(wx.Pen('BLUE'))
        
        # Remember the signature of wx.DC.DrawLine:
        # DrawLine(x1, y1, x2, y2)
        
        for i in range(100):
            x1 = random.randint(1, w-1)
            y1 = random.randint(1, h-1)
            x2 = random.randint(1, w-1)
            y2 = random.randint(1, h-1)
            dc.DrawLine(x1, y1, x2, y2)


class Exercise2(wx.Frame):

    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, title=title)

        # Bind a "paint" event for the frame to the
        # "OnPaint" method
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Show()


    def OnPaint(self, event):

        dc = wx.PaintDC(self)        
        w, h = self.GetClientSize()

        # Use a blue pen, for example...

        # Use a big font for the text...
        font = wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD)
        # Inform the DC we want to use that font
        dc.SetFont(font)

        # Define the string we want to draw
        my_string = 'Hello world'
        
        text_width, text_height, d1, d2 = dc.GetFullTextExtent(my_string)

        # Find the centered position
        xpos = (w - text_width)/2
        ypos = (h - text_height)/2
        
        # Draw our text onto the DC
        dc.DrawText(my_string, xpos, ypos)


app = wx.App(False)
frame = Exercise2(None, 'DC exercise')
app.MainLoop()

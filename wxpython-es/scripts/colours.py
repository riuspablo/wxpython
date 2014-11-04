#! /usr/bin/env python
#coding=utf-8

import wx
import wx.lib.colourdb
import random

class ColourFrame(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, title='Colour database')
        
        # Show the selected colour in this panel
        panel = wx.Panel(self)

        wx.lib.colourdb.updateColourDB()
        # Create a colour list from the colourdb database
        colour_list = wx.lib.colourdb.getColourList()

        # Get one random colour between those 600 available
        random_colour = random.choice(colour_list)
        panel.SetBackgroundColour(random_colour)


app = wx.App(0)
frame = ColourFrame(None)
frame.Show()
# Enter the application main loop
app.MainLoop()

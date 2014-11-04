#! /usr/bin/env python
#coding=utf-8

import wx

def MakeButton(parent):

    return wx.Button(parent, -1, 'OK')


def MakeListBox(parent):

    sample_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']

    return wx.ListBox(parent, -1, choices=sample_list)


# Create an application class instance
app = wx.App()

frame = wx.Frame(None, -1, 'Test')
panel = wx.Panel(frame)
sizer = wx.BoxSizer(wx.HORIZONTAL)

listbox = MakeListBox(panel)
sizer.Add(listbox)

for alignment in [wx.ALIGN_CENTER_VERTICAL, wx.ALIGN_TOP, wx.ALIGN_BOTTOM]:
    button = MakeButton(panel)
    sizer.Add(button, 0, alignment)

panel.SetSizer(sizer)
sizer.SetSizeHints(panel)
frame.Fit()
# Show the frame on screen
frame.Show()

# Enter the application main loop
app.MainLoop()

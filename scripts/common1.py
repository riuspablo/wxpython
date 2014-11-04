#! /usr/bin/env python
#coding=utf-8

import wx

def MakeCheckBox(parent):

    return wx.CheckBox(parent, -1, 'wx.CheckBox')


def MakeListBox(parent):

    sample_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']

    return wx.ListBox(parent, -1, choices=sample_list, style=wx.LB_SINGLE)


def MakeTextCtrl(parent):

    return wx.TextCtrl(parent, -1, 'wx.TextCtrl')


# Create an application class instance
app = wx.App()

for function in [MakeCheckBox, MakeListBox, MakeTextCtrl]:
    frame = wx.Frame(None, -1, 'Test', style=wx.CAPTION|wx.RESIZE_BORDER|wx.CLOSE_BOX)
    panel = wx.Panel(frame)
    child = function(panel)
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(child)
    panel.SetSizer(sizer)
    frame.Fit()

    # Show the frame on screen
    frame.Show()

# Enter the application main loop
app.MainLoop()

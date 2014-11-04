#! /usr/bin/env python
#coding=utf-8

import wx

class BoxSizerFrame(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, title='BoxSizer5')

        sizer = wx.BoxSizer(wx.VERTICAL)
        # Border size effects
        sizer.Add(wx.Button(self, -1, "An extremely long button text"), 0, 0, 0)
        sizer.Add(wx.Button(self, -1, "Small Button"), 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 20)
        sizer.SetSizeHints(self)
        self.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.App(0)
    frame = BoxSizerFrame(None)
    frame.Show()
    app.MainLoop()

    
#! /usr/bin/env python
#coding=utf-8

import wx

class BoxSizerFrame(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, title='BoxSizer3')

        sizer = wx.BoxSizer(wx.VERTICAL)
        # Second button is three times as tall as first button
        sizer.Add(wx.Button(self, -1, "An extremely long button text"), 1, 0, 0)
        sizer.Add(wx.Button(self, -1, "Small Button"), 3, 0, 0)
        sizer.SetSizeHints(self)
        self.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.App(0)
    frame = BoxSizerFrame(None)
    frame.Show()
    app.MainLoop()
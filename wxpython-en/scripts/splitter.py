#! /usr/bin/env python
#coding=utf-8

import wx

class SplitterFrame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, title='wx.SplitterWindow')

        splitter = wx.SplitterWindow(self, -1)
        panel1 = wx.Panel(splitter, -1)

        static = wx.StaticText(panel1, -1, 'Hello World', pos=(100, 100))
        panel1.SetBackgroundColour(wx.LIGHT_GREY)

        panel2 = wx.Panel(splitter, -1)
        panel2.SetBackgroundColour(wx.WHITE)

        splitter.SplitVertically(panel1, panel2)
        self.Centre()


if __name__ == '__main__':
    app = wx.App(0)
    frame = SplitterFrame()
    frame.Show()
    app.MainLoop()


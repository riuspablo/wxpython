#! /usr/bin/env python
#coding=utf-8

import wx

class SplitterFrame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, title='wx.SplitterWindow')

        splitter = wx.SplitterWindow(self, -1, style=wx.SP_LIVE_UPDATE)
        panel1 = wx.Panel(splitter, -1)

        static = wx.StaticText(panel1, -1, 'Hello World', pos=(10, 100))
        panel1.SetBackgroundColour(wx.WHITE)

        splitter2 = wx.SplitterWindow(splitter, -1, style=wx.SP_LIVE_UPDATE)
        
        panel2 = wx.Panel(splitter2, -1)
        panel2.SetBackgroundColour(wx.BLUE)

        panel3 = wx.Panel(splitter2, -1)
        panel3.SetBackgroundColour(wx.RED)

        splitter2.SplitHorizontally(panel2, panel3)
        splitter.SplitVertically(panel1, splitter2)
        self.Centre()


if __name__ == '__main__':
    app = wx.App(0)
    frame = SplitterFrame()
    frame.Show()
    app.MainLoop()


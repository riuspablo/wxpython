#! /usr/bin/env python
#coding=utf-8

import wx

class SizersSample(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, title='Sizers sample')

        panel = wx.Panel(self)

        # Widgets creation
        static_text = wx.StaticText(panel, -1, 'StaticText')
        button = wx.Button(panel, -1, 'Button')
        text_ctrl = wx.TextCtrl(panel, -1, 'I am a text control', style=wx.TE_MULTILINE)

        # Starts of sizers section
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(static_text, 0, wx.ALL, 10)
        sizer.Add(button, 0, wx.LEFT, 10)
        sizer.Add(text_ctrl, 1, wx.EXPAND|wx.ALL, 10)
        sizer.SetSizeHints(panel)
        panel.SetSizer(sizer)
        

if __name__ == '__main__':
    app = wx.App(0)
    frame = SizersSample(None)
    frame.Show()
    app.MainLoop()
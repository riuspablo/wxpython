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
        sizer.Add(static_text)
        sizer.Add(button)
        sizer.Add(text_ctrl)
        sizer.SetSizeHints(panel)
        panel.SetSizer(sizer)
        

if __name__ == '__main__':
    app = wx.App(0)
    frame = SizersSample(None)
    frame.Show()
    app.MainLoop()
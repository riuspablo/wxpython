#! /usr/bin/env python
#coding=utf-8

import wx

def Exercise1():

    # Create an application class instance
    app = wx.App()

    # Create two frames and show them
    for i in range(2):
        frame = wx.Frame(None, -1, 'Hello world %d'%(i+1))

        # Show the frame on screen
        frame.Show()

    # Enter the application main loop
    app.MainLoop()


def Exercise2():

    # Create an application class instance
    app = wx.App()

    frame1 = wx.Frame(None, -1, 'Hello world parent')
    # frame2 is a child of frame 1
    frame2 = wx.Frame(frame1, -1, 'Hello world child')

    # Show the frames on screen
    frame1.Show()
    frame2.Show()

    # Enter the application main loop
    app.MainLoop()


if __name__ == '__main__':
    Exercise1()


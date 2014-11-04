#! /usr/bin/env python
#coding=utf-8

import wx

class TreeFrame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, title='wx.TreeCtrl')

        tree_ctrl = wx.TreeCtrl(self, -1, style=wx.TR_DEFAULT_STYLE)

        # Add the tree root
        root = tree_ctrl.AddRoot('Root item')

        for i in range(10):
            tree_ctrl.AppendItem(root, 'Item %d'%(i+1))

        tree_ctrl.ExpandAll()
        self.Centre()


if __name__ == '__main__':
    app = wx.App(0)
    frame = TreeFrame()
    frame.Show()
    app.MainLoop()


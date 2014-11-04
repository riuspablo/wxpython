#! /usr/bin/env python
#coding=utf-8

import wx
import datetime

class MainWindow(wx.Frame):

    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, title=title)

        # A Statusbar in the bottom of the window
        # Set it up so it has two fields
        self.CreateStatusBar(2)

        # Set the second field to be double in width wrt the first
        self.SetStatusWidths([-1, -2])

        # Get today's date via datetime
        today = datetime.datetime.today()
        today = today.strftime('%d-%b-%Y')

        # Set today's date in the second field
        self.SetStatusText(today, 1)

        # Setting up the menu
        file_menu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        file_menu.Append(wx.ID_ABOUT, '&About', 'Information about this application')
        file_menu.AppendSeparator()
        file_menu.Append(wx.ID_EXIT, 'E&xit', 'Exit the application')

        # Create the "Edit" top menu
        edit_menu = wx.Menu()

        # wx.ID_CUT, wx.ID_COPY and wx.ID_PASTE are standard IDs provided by wxWidgets.
        edit_menu.Append(wx.ID_CUT, 'C&ut', 'Cut the current selection')
        edit_menu.Append(wx.ID_COPY, '&Copy', 'Copy the current selection')
        edit_menu.AppendSeparator()
        edit_menu.Append(wx.ID_PASTE, '&Paste', 'Paste text from clipboard')

        # Creating the menubar
        menu_bar = wx.MenuBar()

        # Adding the 'file_menu' to the menu bar
        menu_bar.Append(file_menu, '&File')
        menu_bar.Append(edit_menu, '&Edit')

        # Adding the menu bar to the frame content
        self.SetMenuBar(menu_bar)
        self.Show()

app = wx.App(False)
frame = MainWindow(None, 'Sample application')
app.MainLoop()

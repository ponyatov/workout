## @file

import config

import os, sys, re
import datetime as dt
import threading

import wx


import wx.adv

class TrayIcon(wx.adv.TaskBarIcon):
    def __init__(self):
        super().__init__()
        self.icon = wx.Icon('static/logo.png', wx.BITMAP_TYPE_PNG)
        self.SetIcon(self.icon, tooltip=str(sys.argv))
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)
        self.init_popup_menu()

    def init_popup_menu(self):
        def create_menu_item(menu, label, func):
            item = wx.MenuItem(menu, -1, label)
            menu.Bind(wx.EVT_MENU, func, id=item.GetId())
            menu.Append(item)
            return item
        self.menu = wx.Menu()
        create_menu_item(self.menu, 'Say Hello', self.on_hello)
        self.menu.AppendSeparator()
        create_menu_item(self.menu, 'Exit', self.on_exit)
        return self.menu

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)

    def on_hello(self, event):
        print([self, 'on_hello', event])

    def on_click(self, event):
        print([self, 'on_click', event])

    def on_left_down(self, event):
        print('Tray icon was left-clicked.')


if __name__ == '__main__':
    # https://stackoverflow.com/questions/34172003/tray-icon-application-in-python-icon-is-gone
    app = wx.App()
    tray = TrayIcon()
    app.MainLoop()
    # threading.Thread(target=app.MainLoop, args=[]).start()

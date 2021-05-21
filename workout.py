## @file

import config

import os, sys, time, re
import datetime as dt
import threading

import wx

import wx.adv

class TrayIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.icon = wx.Icon('static/logo.png', wx.BITMAP_TYPE_ANY)
        self.SetIcon(self.icon, tooltip=str(sys.argv))
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_click)
        self.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, self.on_right_click)
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

    def on_left_click(self, event):
        print(['on_left_click', event, self])
        self.frame.Hide()

        def timer():
            time.sleep(2)
            self.frame.Show()
        threading.Thread(target=timer).start()

    def on_right_click(self, event):
        print(['on_right_click', event, self])
        self.frame.Hide()

# https://stackoverflow.com/questions/35542551/how-to-create-a-taskbaricon-only-application-in-wxpython
class mainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, str(sys.argv))
        self.Hide()
        self.tray = TrayIcon(self)


if __name__ == '__main__':
    app = wx.App()
    mainFrame()
    threading.Thread(target=app.MainLoop, args=[]).start()

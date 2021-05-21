#!./bin/python3

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
        self.icon = wx.Icon('static/logo.png', wx.BITMAP_TYPE_PNG)
        self.SetIcon(self.icon, tooltip=str(sys.argv))
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_click)
        self.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, self.on_right_click)

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)

    def on_hello(self, event):
        print([self, 'on_hello', event])

    def on_click(self, event):
        print([self, 'on_click', event])

    def on_left_click(self, event):
        print(['on_left_click', event, self])
        self.frame.Hide()
        if not self.frame.timer.IsRunning():
            self.frame.timer.StartOnce(15 * 60 * 1000)

    def on_right_click(self, event):
        print(['on_right_click', event, self])
        self.frame.Hide()
        self.frame.timer.Stop()


class mainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, str(sys.argv))
        self.Hide()
        self.tray = TrayIcon(self)
        self.init_timer()

    def init_timer(self):
        class T(wx.Timer):
            def __init__(self, frame):
                super().__init__()
                self.frame = frame

            def Notify(self):
                self.frame.Maximize(True)
                self.frame.Show()
        self.timer = T(self)


if __name__ == '__main__':
    app = wx.App()
    mainFrame()
    # app.MainLoop()
    threading.Thread(target=app.MainLoop, args=[]).start()

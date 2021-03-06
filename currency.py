#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.5 on Thu Nov 28 12:44:35 2013

import wx
from threading import Thread
import time
import requests

# begin wxGlade: extracode
# load values from last update
config={}
execfile("rates.conf",config)
EUR_USD = config["EUR_USD"]
EUR_GBP = config["EUR_GBP"]
USD_GBP = config["USD_GBP"]
def myfunc(i):
    global EUR_USD
    global EUR_GBP
    global USD_GBP
    url = 'http://rate-exchange.appspot.com/currency?from=EUR&to=USD&q=1'
    r = requests.get(url)
    try:
        EUR_USD = r.json()['v']
    except:
        print "Error!"
    time.sleep(2)
    url = 'http://rate-exchange.appspot.com/currency?from=EUR&to=GBP&q=1'
    r = requests.get(url)
    try:
        EUR_GBP = r.json()['v']
    except:
        print "Error!"
    time.sleep(2)
    url = 'http://rate-exchange.appspot.com/currency?from=USD&to=GBP&q=1'
    r = requests.get(url)
    try:
        USD_GBP = r.json()['v']
    except:
        print "Error!"

t = Thread(target=myfunc,args=(1,))
t.start()
# end wxGlade

class MyFrame1(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame1.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP
        wx.Frame.__init__(self, *args, **kwds)
        self.EUR = wx.StaticText(self, wx.ID_ANY, "EUR")
        self.tc_EUR = wx.TextCtrl(self, wx.ID_ANY, "")
        self.USD = wx.StaticText(self, wx.ID_ANY, "USD")
        self.tc_USD = wx.TextCtrl(self, wx.ID_ANY, "")
        self.GBP = wx.StaticText(self, wx.ID_ANY, "GBP")
        self.tc_GBP = wx.TextCtrl(self, wx.ID_ANY, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.eh_EUR, self.tc_EUR)
        self.Bind(wx.EVT_TEXT, self.eh_USD, self.tc_USD)
        self.Bind(wx.EVT_TEXT, self.eh_GBP, self.tc_GBP)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame1.__set_properties
        self.SetTitle("CurrencyPy")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame1.__do_layout
        grid_sizer_1 = wx.GridSizer(3, 2, 2, 2)
        grid_sizer_1.Add(self.EUR, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.tc_EUR, 0, 0, 0)
        grid_sizer_1.Add(self.USD, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.tc_USD, 0, 0, 0)
        grid_sizer_1.Add(self.GBP, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.tc_GBP, 0, 0, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def eh_EUR(self, event):  # wxGlade: MyFrame1.<event_handler>
        if self.tc_EUR.GetValue() != '':
            self.tc_USD.ChangeValue(str(round(float(self.tc_EUR.GetValue())*EUR_USD,2)))
            self.tc_GBP.ChangeValue(str(round(float(self.tc_EUR.GetValue())*EUR_GBP,2)))
            event.Skip()
    def eh_USD(self, event):  # wxGlade: MyFrame1.<event_handler>
        if self.tc_USD.GetValue() != '':
            self.tc_EUR.ChangeValue(str(round(float(self.tc_USD.GetValue())/EUR_USD,2)))
            self.tc_GBP.ChangeValue(str(round(float(self.tc_USD.GetValue())*USD_GBP,2)))
            event.Skip()
    def eh_GBP(self, event):  # wxGlade: MyFrame1.<event_handler>
        if self.tc_GBP.GetValue() != '':
            self.tc_EUR.ChangeValue(str(round(float(self.tc_GBP.GetValue())/EUR_GBP,2)))
            self.tc_USD.ChangeValue(str(round(float(self.tc_GBP.GetValue())/USD_GBP,2)))
            event.Skip()
# end of class MyFrame1
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_2 = MyFrame1(None, -1, "")
    app.SetTopWindow(frame_2)
    frame_2.Show()
    app.MainLoop()

#!/usr/bin/env python3

import win32clipboard as win
import datetime


def toClipboard(text):
    win.OpenClipboard()
    win.EmptyClipboard()
    win.SetClipboardText(text, win.CF_UNICODETEXT)
    win.CloseClipboard()

### main -----------------------------------------------------------
text = "Testing #1: " + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
toClipboard(text)
print (text)
input()



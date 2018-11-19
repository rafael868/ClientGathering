import wx
from gui import GUI


if __name__ == '__main__':
    app = wx.App()
    GUI(None, 'ClientGathering', (300, 300))
    app.MainLoop()
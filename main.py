import wx
from gui import GUI


if __name__ == '__main__':
    app = wx.App()
    GUI(None, 'ClientGathering', (800, 400))
    app.MainLoop()

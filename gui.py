import wx


class GUI(wx.Frame):
    def __init__(self, parent, title, size):
        super(GUI, self).__init__(parent, title=title, size=size)
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.WHITE)

        self.AddClientButton = wx.Button(self.panel, -1, 'Add Client')
        self.AddClientButton.Bind(wx.EVT_BUTTON, self.AddClient)

    def AddClient(self, event):
        print('Add Client')





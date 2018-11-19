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

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        self.text = wx.TextCtrl(self.panel, size=(250, 25), style=wx.TE_READONLY)
        self.AddClientButton = wx.Button(self.panel, -1, 'Add Client')
        self.AddClientButton.Bind(wx.EVT_BUTTON, self.AddClient)

        hbox1.Add(self.text, proportion=1, flag=wx.ALIGN_CENTER)
        hbox2.Add(self.AddClientButton, proportion=1, flag = wx.RIGHT, border = 10)

        vbox.Add((0, 30))
        vbox.Add(hbox1, flag=wx.ALIGN_CENTER)
        vbox.Add((0, 50))
        vbox.Add(hbox2, proportion=1, flag=wx.ALIGN_CENTRE)

        self.panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)

    def AddClient(self, event):
        dlg = wx.TextEntryDialog(self, 'Enter Client Name', 'Text Entry Dialog')

        if dlg.ShowModal() == wx.ID_OK:
            self.text.SetValue(dlg.GetValue())
        dlg.Destroy()





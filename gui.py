import wx
import sys

customers = [('Customer 1', 'cust1@gmail.com', '12.09.2018', '12.09.2023', '1 year, 3 m, 12 days'),
             ('Customer 2', 'cust2@gmail.com', '12.09.2018', '12.09.2023', '3 year, 4 m, 11 days'),
             ('Customer 3', 'cust3@gmail.com', '09.09.2017', '12.09.2022', '2 year, 2 m, 2 days')]

class GUI(wx.Frame):
    def __init__(self, parent, title, size):
        super(GUI, self).__init__(parent, title=title, size=size)

        self.panel = wx.Panel(self)

        self.box = wx.BoxSizer(wx.VERTICAL)
        self.listBox = wx.BoxSizer(wx.HORIZONTAL)
        self.btnBox = wx.BoxSizer(wx.HORIZONTAL)

        self.cListCtrl = wx.ListCtrl(self.panel, -1, style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)

        self.cListCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelectItem)

        self.deleteBtn = wx.Button(self.panel, -1, 'Delete')
        self.newBtn = wx.Button(self.panel, -1, 'New')

        self.width = self.panel.GetParent().GetClientSize().width / 5

        self.selected_item = -1

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        self.cListCtrl.InsertColumn(0, 'name', width=self.width)
        self.cListCtrl.InsertColumn(1, 'email', width=self.width)
        self.cListCtrl.InsertColumn(2, 'date of test', width=self.width)
        self.cListCtrl.InsertColumn(3, 'date of expire', width=self.width)
        self.cListCtrl.InsertColumn(4, 'time to next test', width=self.width)

        self.newBtn.Bind(wx.EVT_BUTTON, self.onClickNew)
        self.deleteBtn.Bind(wx.EVT_BUTTON, self.onClickDel)

        for i in customers:
            index = self.cListCtrl.InsertItem(sys.maxsize, i[0])
            self.cListCtrl.SetItem(index, 1, i[1])
            self.cListCtrl.SetItem(index, 2, i[2])
            self.cListCtrl.SetItem(index, 3, i[3])
            self.cListCtrl.SetItem(index, 4, i[4])

        self.btnBox.Add(self.deleteBtn, 0)
        self.btnBox.Add(self.newBtn, 0)
        self.listBox.Add(self.cListCtrl, 0, wx.EXPAND | wx.ALL)
        self.box.Add(self.btnBox, 0, wx.ALL, border=10)
        self.box.Add(self.listBox, 0, wx.EXPAND | wx.ALL)

        self.panel.SetSizer(self.box)

        self.panel.Bind(wx.EVT_SIZE, self.onResize)

    def onResize(self, event):
        event.Skip()

        width = self.panel.GetParent().GetClientSize().width / 5
        self.cListCtrl.SetColumnWidth(0, width=width)
        self.cListCtrl.SetColumnWidth(1, width=width)
        self.cListCtrl.SetColumnWidth(2, width=width)
        self.cListCtrl.SetColumnWidth(3, width=width)
        self.cListCtrl.SetColumnWidth(4, width=width)

    def onSelectItem(self, event):
        self.selected_item = event.GetIndex()

    def onClickDel(self, event):

        if self.selected_item == -1:
            return

        dial = wx.MessageDialog(None, 'Are you sure to delete {} item ?'.format(self.selected_item+1), '', wx.OK | wx.CANCEL)

        if dial.ShowModal() == wx.ID_OK:
            try:
                self.cListCtrl.DeleteItem(self.selected_item)
            except:
                print('Item not found')

    def onClickNew(self, event):
        dlg = wx.Dialog(self)

        ok_btn = dlg.CreateButtonSizer(wx.OK)

        box = wx.BoxSizer(wx.VERTICAL)
        nbox = wx.BoxSizer(wx.HORIZONTAL)
        ebox = wx.BoxSizer(wx.HORIZONTAL)
        dtbox = wx.BoxSizer(wx.HORIZONTAL)
        dnbox = wx.BoxSizer(wx.HORIZONTAL)
        btnbox = wx.BoxSizer(wx.HORIZONTAL)

        t1 = wx.StaticText(dlg, -1, "Customer name")
        t2 = wx.StaticText(dlg, -1, "Customer email")
        t3 = wx.StaticText(dlg, -1, "Date of test")
        t4 = wx.StaticText(dlg, -1, "Date of next test")

        nbox.Add(t1, 0, wx.LEFT | wx.RIGHT, 10)
        ebox.Add(t2, 0, wx.LEFT | wx.RIGHT, 10)
        dtbox.Add(t3, 0, wx.LEFT | wx.RIGHT, 10)
        dnbox.Add(t4, 0, wx.LEFT | wx.RIGHT, 10)
        btnbox.Add(ok_btn, 0, wx.LEFT | wx.RIGHT, 10)

        name = wx.TextCtrl(dlg)
        email = wx.TextCtrl(dlg)
        date_of_test = wx.TextCtrl(dlg)
        date_next = wx.TextCtrl(dlg)

        nbox.Add(name, 0, wx.LEFT, 17)
        ebox.Add(email, 0, wx.LEFT, 17)
        dtbox.Add(date_of_test, 0, wx.LEFT, 40)
        dnbox.Add(date_next, 0, wx.LEFT, 10)

        box.Add(nbox, 0, wx.ALL, border=5)
        box.Add(ebox, 0, wx.ALL, border=5)
        box.Add(dtbox, 0, wx.ALL, border=5)
        box.Add(dnbox, 0, wx.ALL, border=5)
        box.Add(btnbox, 0, wx.ALL, border=5)

        dlg.SetSizer(box)

        if dlg.ShowModal() == wx.ID_OK:
            print("name: {}".format(name.GetValue()))
            print("email: {}".format(email.GetValue()))
            print("Date of test: {}".format(date_of_test.GetValue()))
            print("Date of next test: {}".format(date_next.GetValue()))
        dlg.Destroy()



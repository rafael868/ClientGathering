import wx
import sys

from data_handler import Client, DataBase


class GUI(wx.Frame):
    def __init__(self, parent, title, size):
        super(GUI, self).__init__(parent, title=title, size=size)

        self.panel = wx.Panel(self)

        self.box = wx.BoxSizer(wx.VERTICAL)
        self.listBox = wx.BoxSizer(wx.HORIZONTAL)
        self.btnBox = wx.BoxSizer(wx.HORIZONTAL)

        self.cListCtrl = wx.ListCtrl(self.panel, -1, style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)

        self.cListCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelectItem)
        self.Bind(wx.EVT_CLOSE, self.onClose)

        self.deleteBtn = wx.Button(self.panel, -1, 'Delete')
        self.newBtn = wx.Button(self.panel, -1, 'New')

        self.width = self.panel.GetParent().GetClientSize().width / 5

        self.selected_item = -1
        self.selected_name = None

        self.InitUI()

        self.c = Client()

        self.db = DataBase('clients.db', 'cl_tab')

        try:
            self.db.InitDb()
        except:
            pass

        self.data = self.db.get_clients()
        self.updateGuiData(self.data)

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

        self.btnBox.Add(self.deleteBtn, 0)
        self.btnBox.Add(self.newBtn, 0)
        self.listBox.Add(self.cListCtrl, 0, wx.EXPAND | wx.ALL)
        self.box.Add(self.btnBox, 0, wx.ALL, border=10)
        self.box.Add(self.listBox, 0, wx.EXPAND | wx.ALL)

        self.panel.SetSizer(self.box)

        self.panel.Bind(wx.EVT_SIZE, self.onResize)

    def updateGuiData(self, data):
        for item in data:
            index = self.cListCtrl.InsertItem(sys.maxsize, item[0])
            self.cListCtrl.SetItem(index, 1, item[1])
            self.cListCtrl.SetItem(index, 2, item[2])
            self.cListCtrl.SetItem(index, 3, item[3])
            self.cListCtrl.SetItem(index, 4, '0')

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
        self.selected_name = self.cListCtrl.GetItem(self.selected_item, 0)

    def onClickDel(self, event):

        if self.selected_item == -1:
            return

        dial = wx.MessageDialog(None, 'Are you sure to delete {} item ?'.format(self.selected_item+1), '', wx.OK | wx.CANCEL)

        if dial.ShowModal() == wx.ID_OK:
            try:
                self.db.del_clinet(self.selected_name.GetText())
                self.cListCtrl.DeleteItem(self.selected_item)
            except:
                print('ERROR: Can\'t delete this item')
        self.selected_item = -1

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
            self.c.set_data(name.GetValue(), email.GetValue(), date_of_test.GetValue(), date_next.GetValue())
            self.db.add_client(self.c)
            index = self.cListCtrl.InsertItem(sys.maxsize, name.GetValue())
            self.cListCtrl.SetItem(index, 1, email.GetValue())
            self.cListCtrl.SetItem(index, 2, date_of_test.GetValue())
            self.cListCtrl.SetItem(index, 3, date_next.GetValue())
            self.cListCtrl.SetItem(index, 4, '0')
        dlg.Destroy()

    def onClose(self, event):
        self.db.close_conn()
        self.Destroy()


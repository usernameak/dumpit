# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext
import wx.stc

###########################################################################
## Class main
###########################################################################

class main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Dumpit", pos = wx.DefaultPosition, size = wx.Size( 1100,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.status = wx.richtext.RichTextCtrl( self, wx.ID_ANY, u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac libero vel massa tristique ullamcorper ac et quam. Nunc ultricies dui nibh, ac auctor augue pulvinar sit amet. Nulla malesuada, arcu eu aliquet semper, leo est tincidunt ante, id aliquet tortor leo vel ex. Suspendisse orci lorem, molestie in auctor in, lacinia a felis. Nam molestie sagittis rutrum. Pellentesque tellus mi, posuere sed bibendum quis, laoreet a dui. In vehicula feugiat est, sit amet pellentesque neque porta sit amet. Nam in elit malesuada, imperdiet dolor eu, maximus elit.\n\nDuis tincidunt ante at massa ornare, in vehicula dolor bibendum. Integer eu est interdum, malesuada ex id, rhoncus lectus. Nullam elementum orci in tellus vestibulum porttitor. Etiam vel lectus aliquet, iaculis erat ac, convallis tortor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed bibendum ultrices tempus. Cras diam felis, sodales a lacinia non, rutrum sit amet nisl. Cras dapibus, ex vitae fringilla convallis, mi lacus faucibus lorem, a aliquam ligula orci in quam. Fusce eu erat maximus, volutpat mauris quis, egestas dolor.\n\nPellentesque elementum ultrices dignissim. Integer bibendum elementum auctor. Nulla facilisi. Integer tristique bibendum facilisis. Morbi id risus molestie, tempor diam non, dignissim mauris. In sit amet orci id tellus fringilla cursus. Nam rhoncus lectus a nibh congue, at fermentum elit accumsan. Proin congue nunc velit, at tempor arcu vulputate vitae. Aenean ac diam quis neque gravida ullamcorper. Pellentesque ac erat ex.\n\nMauris lectus risus, consequat quis eros vitae, feugiat fermentum purus. Aenean risus ipsum, dignissim quis consectetur hendrerit, ultrices sed velit. Duis maximus massa tellus, at blandit elit fringilla nec. Ut luctus facilisis mi, non vehicula lorem sagittis vel. Morbi gravida lacus eu sapien condimentum gravida. Vestibulum consectetur auctor est ac efficitur. Aliquam aliquam commodo nibh. Proin ultricies porttitor arcu id accumsan. Maecenas quam eros, egestas vitae fermentum laoreet, efficitur at lacus.\n\nCurabitur id erat eu sapien volutpat ullamcorper. Nulla volutpat dignissim varius. Duis vulputate imperdiet tincidunt. Aenean in leo feugiat, rhoncus erat quis, sollicitudin sapien. Vivamus imperdiet turpis sit amet velit tristique, in dictum dolor pharetra. Duis efficitur magna nec hendrerit congue. In vel luctus purus. ", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.status.SetMinSize( wx.Size( 320,-1 ) )

		bSizer1.Add( self.status, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.tab = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dPage1 = wx.Panel( self.tab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.lInterface = wx.StaticText( self.dPage1, wx.ID_ANY, u"Interface:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lInterface.Wrap( -1 )

		bSizer6.Add( self.lInterface, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cInterfaceChoices = []
		self.cInterface = wx.Choice( self.dPage1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cInterfaceChoices, 0 )
		self.cInterface.SetSelection( 0 )
		bSizer6.Add( self.cInterface, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lSpeed = wx.StaticText( self.dPage1, wx.ID_ANY, u"Speed:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lSpeed.Wrap( -1 )

		bSizer6.Add( self.lSpeed, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nSpeed = wx.SpinCtrl( self.dPage1, wx.ID_ANY, u"1000", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 30000, 1000 )
		bSizer6.Add( self.nSpeed, 1, wx.ALL, 5 )


		bSizer5.Add( bSizer6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.lChipset = wx.StaticText( self.dPage1, wx.ID_ANY, u"Chipset:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lChipset.Wrap( -1 )

		bSizer61.Add( self.lChipset, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cChipsetChoices = []
		self.cChipset = wx.Choice( self.dPage1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cChipsetChoices, 0 )
		self.cChipset.SetSelection( 0 )
		self.cChipset.SetMaxSize( wx.Size( 150,-1 ) )

		bSizer61.Add( self.cChipset, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lTarget = wx.StaticText( self.dPage1, wx.ID_ANY, u"Target:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lTarget.Wrap( -1 )

		bSizer61.Add( self.lTarget, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cTargetChoices = []
		self.cTarget = wx.Choice( self.dPage1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cTargetChoices, 0 )
		self.cTarget.SetSelection( 0 )
		bSizer61.Add( self.cTarget, 0, wx.ALL, 5 )

		self.lTap = wx.StaticText( self.dPage1, wx.ID_ANY, u"TAP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lTap.Wrap( -1 )

		bSizer61.Add( self.lTap, 0, wx.ALL, 5 )

		cTapChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9" ]
		self.cTap = wx.Choice( self.dPage1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cTapChoices, 0 )
		self.cTap.SetSelection( 0 )
		self.cTap.Enable( False )
		self.cTap.SetMinSize( wx.Size( 100,-1 ) )

		bSizer61.Add( self.cTap, 0, wx.ALL, 5 )

		self.lIR = wx.StaticText( self.dPage1, wx.ID_ANY, u"IR:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lIR.Wrap( -1 )

		bSizer61.Add( self.lIR, 0, wx.ALL, 5 )

		self.nIR = wx.SpinCtrl( self.dPage1, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 64, 0 )
		self.nIR.SetMinSize( wx.Size( 150,-1 ) )

		bSizer61.Add( self.nIR, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer61, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer611 = wx.BoxSizer( wx.HORIZONTAL )

		self.lResetMode = wx.StaticText( self.dPage1, wx.ID_ANY, u"Reset Mode:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lResetMode.Wrap( -1 )

		bSizer611.Add( self.lResetMode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cResetModeChoices = []
		self.cResetMode = wx.Choice( self.dPage1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cResetModeChoices, 0 )
		self.cResetMode.SetSelection( 0 )
		bSizer611.Add( self.cResetMode, 1, wx.ALL, 5 )

		self.lResetDelay = wx.StaticText( self.dPage1, wx.ID_ANY, u"Reset Delay:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lResetDelay.Wrap( -1 )

		bSizer611.Add( self.lResetDelay, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.bResetDelay = wx.Button( self.dPage1, wx.ID_ANY, u"Configure", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611.Add( self.bResetDelay, 0, wx.ALL, 5 )

		self.bSkipInit = wx.CheckBox( self.dPage1, wx.ID_ANY, u"Skip Initialization", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611.Add( self.bSkipInit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( bSizer611, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer6111 = wx.BoxSizer( wx.HORIZONTAL )

		self.lStart = wx.StaticText( self.dPage1, wx.ID_ANY, u"Start:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lStart.Wrap( -1 )

		bSizer6111.Add( self.lStart, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tStart = wx.TextCtrl( self.dPage1, wx.ID_ANY, u"00000000", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6111.Add( self.tStart, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.lEnd = wx.StaticText( self.dPage1, wx.ID_ANY, u"End:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lEnd.Wrap( -1 )

		bSizer6111.Add( self.lEnd, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tEnd = wx.TextCtrl( self.dPage1, wx.ID_ANY, u"02000000", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6111.Add( self.tEnd, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.lNandSize = wx.StaticText( self.dPage1, wx.ID_ANY, u"Page Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lNandSize.Wrap( -1 )

		bSizer6111.Add( self.lNandSize, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cNandSizeChoices = [ u"512/2K (O1N)", u"2K/4K (O1N)", u"Auto" ]
		self.cNandSize = wx.Choice( self.dPage1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cNandSizeChoices, 0 )
		self.cNandSize.SetSelection( 2 )
		bSizer6111.Add( self.cNandSize, 1, wx.ALL, 5 )

		self.bECCDisable = wx.CheckBox( self.dPage1, wx.ID_ANY, u"Disable ECC", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6111.Add( self.bECCDisable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.bBadBlockinData = wx.CheckBox( self.dPage1, wx.ID_ANY, u"Bad Blocks on Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6111.Add( self.bBadBlockinData, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( bSizer6111, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer611112 = wx.BoxSizer( wx.HORIZONTAL )

		self.bConnect = wx.Button( self.dPage1, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611112.Add( self.bConnect, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.bConnectRemote = wx.Button( self.dPage1, wx.ID_ANY, u"Connect to Remote", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611112.Add( self.bConnectRemote, 0, wx.ALL, 5 )

		self.bForwardRemote = wx.Button( self.dPage1, wx.ID_ANY, u"Forward to Remote", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611112.Add( self.bForwardRemote, 0, wx.ALL, 5 )

		self.bReconnectRemote = wx.Button( self.dPage1, wx.ID_ANY, u"Reconnect to Remote", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611112.Add( self.bReconnectRemote, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer611112, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer6111121 = wx.BoxSizer( wx.HORIZONTAL )

		self.lTargetRemote = wx.StaticText( self.dPage1, wx.ID_ANY, u"Address:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lTargetRemote.Wrap( -1 )

		bSizer6111121.Add( self.lTargetRemote, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.bTargetRemote = wx.TextCtrl( self.dPage1, wx.ID_ANY, u"dumpit.ucomsite.my.id", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6111121.Add( self.bTargetRemote, 1, wx.ALL, 5 )

		self.bUseGDB = wx.CheckBox( self.dPage1, wx.ID_ANY, u"Use GDB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bUseGDB.Enable( False )

		bSizer6111121.Add( self.bUseGDB, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( bSizer6111121, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer61111 = wx.BoxSizer( wx.HORIZONTAL )

		self.bDumpFlash = wx.Button( self.dPage1, wx.ID_ANY, u"Dump Flash", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61111.Add( self.bDumpFlash, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.bDumpMemory = wx.Button( self.dPage1, wx.ID_ANY, u"Dump Memory", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61111.Add( self.bDumpMemory, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.bStop = wx.Button( self.dPage1, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bStop.Enable( False )

		bSizer61111.Add( self.bStop, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.bNandConfigure = wx.Button( self.dPage1, wx.ID_ANY, u"Configure NAND Controller", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61111.Add( self.bNandConfigure, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( bSizer61111, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer611111 = wx.BoxSizer( wx.HORIZONTAL )

		self.bGo = wx.Button( self.dPage1, wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611111.Add( self.bGo, 0, wx.ALL, 5 )

		self.bHalt = wx.Button( self.dPage1, wx.ID_ANY, u"Halt", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611111.Add( self.bHalt, 0, wx.ALL, 5 )

		self.bReset = wx.Button( self.dPage1, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611111.Add( self.bReset, 0, wx.ALL, 5 )

		self.bHardReset = wx.Button( self.dPage1, wx.ID_ANY, u"Hard Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611111.Add( self.bHardReset, 0, wx.ALL, 5 )

		self.bExecScript = wx.Button( self.dPage1, wx.ID_ANY, u"Execute Script", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611111.Add( self.bExecScript, 1, wx.ALL, 5 )

		self.bExecLoader = wx.Button( self.dPage1, wx.ID_ANY, u"Load DCC", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer611111.Add( self.bExecLoader, 1, wx.ALL, 5 )


		bSizer5.Add( bSizer611111, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer6111111 = wx.BoxSizer( wx.HORIZONTAL )

		self.bEnableMMU = wx.Button( self.dPage1, wx.ID_ANY, u"Enable MMU", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6111111.Add( self.bEnableMMU, 1, wx.ALL, 5 )

		self.bDisableMMU = wx.Button( self.dPage1, wx.ID_ANY, u"Disable MMU", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6111111.Add( self.bDisableMMU, 1, wx.ALL, 5 )

		self.bExec = wx.Button( self.dPage1, wx.ID_ANY, u"Execute Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6111111.Add( self.bExec, 1, wx.ALL, 5 )


		bSizer5.Add( bSizer6111111, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer61111111 = wx.BoxSizer( wx.VERTICAL )

		self.sInfo = wx.richtext.RichTextCtrl( self.dPage1, wx.ID_ANY, u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac libero vel massa tristique ullamcorper ac et quam. Nunc ultricies dui nibh, ac auctor augue pulvinar sit amet. Nulla malesuada, arcu eu aliquet semper, leo est tincidunt ante, id aliquet tortor leo vel ex. Suspendisse orci lorem, molestie in auctor in, lacinia a felis. Nam molestie sagittis rutrum. Pellentesque tellus mi, posuere sed bibendum quis, laoreet a dui. In vehicula feugiat est, sit amet pellentesque neque porta sit amet. Nam in elit malesuada, imperdiet dolor eu, maximus elit.\n\nDuis tincidunt ante at massa ornare, in vehicula dolor bibendum. Integer eu est interdum, malesuada ex id, rhoncus lectus. Nullam elementum orci in tellus vestibulum porttitor. Etiam vel lectus aliquet, iaculis erat ac, convallis tortor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed bibendum ultrices tempus. Cras diam felis, sodales a lacinia non, rutrum sit amet nisl. Cras dapibus, ex vitae fringilla convallis, mi lacus faucibus lorem, a aliquam ligula orci in quam. Fusce eu erat maximus, volutpat mauris quis, egestas dolor.\n\nPellentesque elementum ultrices dignissim. Integer bibendum elementum auctor. Nulla facilisi. Integer tristique bibendum facilisis. Morbi id risus molestie, tempor diam non, dignissim mauris. In sit amet orci id tellus fringilla cursus. Nam rhoncus lectus a nibh congue, at fermentum elit accumsan. Proin congue nunc velit, at tempor arcu vulputate vitae. Aenean ac diam quis neque gravida ullamcorper. Pellentesque ac erat ex.\n\nMauris lectus risus, consequat quis eros vitae, feugiat fermentum purus. Aenean risus ipsum, dignissim quis consectetur hendrerit, ultrices sed velit. Duis maximus massa tellus, at blandit elit fringilla nec. Ut luctus facilisis mi, non vehicula lorem sagittis vel. Morbi gravida lacus eu sapien condimentum gravida. Vestibulum consectetur auctor est ac efficitur. Aliquam aliquam commodo nibh. Proin ultricies porttitor arcu id accumsan. Maecenas quam eros, egestas vitae fermentum laoreet, efficitur at lacus.\n\nCurabitur id erat eu sapien volutpat ullamcorper. Nulla volutpat dignissim varius. Duis vulputate imperdiet tincidunt. Aenean in leo feugiat, rhoncus erat quis, sollicitudin sapien. Vivamus imperdiet turpis sit amet velit tristique, in dictum dolor pharetra. Duis efficitur magna nec hendrerit congue. In vel luctus purus. ", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer61111111.Add( self.sInfo, 1, wx.EXPAND |wx.ALL, 5 )

		self.lCurrentDCC = wx.StaticText( self.dPage1, wx.ID_ANY, u"DCC Loader: None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lCurrentDCC.Wrap( -1 )

		bSizer61111111.Add( self.lCurrentDCC, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer61111111, 1, wx.EXPAND, 5 )

		bSizer60 = wx.BoxSizer( wx.VERTICAL )

		self.tOCDCmd = wx.TextCtrl( self.dPage1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer60.Add( self.tOCDCmd, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( bSizer60, 0, wx.EXPAND, 5 )


		self.dPage1.SetSizer( bSizer5 )
		self.dPage1.Layout()
		bSizer5.Fit( self.dPage1 )
		self.tab.AddPage( self.dPage1, u"Dump", True )
		self.dPage2 = wx.Panel( self.tab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.pSettingsNull = wx.Panel( self.dPage2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.lNothing = wx.StaticText( self.pSettingsNull, wx.ID_ANY, u"Nothing to see here.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lNothing.Wrap( -1 )

		bSizer9.Add( self.lNothing, 0, wx.ALL, 5 )


		self.pSettingsNull.SetSizer( bSizer9 )
		self.pSettingsNull.Layout()
		bSizer9.Fit( self.pSettingsNull )
		bSizer8.Add( self.pSettingsNull, 1, wx.EXPAND|wx.ALL, 5 )

		self.pSettingsFT232R = wx.Panel( self.dPage2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pSettingsFT232R.Hide()

		bSizer91 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.lUSBID = wx.StaticText( self.pSettingsFT232R, wx.ID_ANY, u"USB ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lUSBID.Wrap( -1 )

		bSizer15.Add( self.lUSBID, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tUSBID = wx.TextCtrl( self.pSettingsFT232R, wx.ID_ANY, u"0x0403:0x6001", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.tUSBID, 1, wx.ALL, 5 )


		bSizer91.Add( bSizer15, 0, wx.EXPAND, 5 )

		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )

		self.lRestoreSerial = wx.StaticText( self.pSettingsFT232R, wx.ID_ANY, u"Restore Serial Code:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lRestoreSerial.Wrap( -1 )

		bSizer151.Add( self.lRestoreSerial, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tRestoreSerial = wx.TextCtrl( self.pSettingsFT232R, wx.ID_ANY, u"0xffff", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer151.Add( self.tRestoreSerial, 1, wx.ALL, 5 )


		bSizer91.Add( bSizer151, 0, wx.EXPAND, 5 )

		bSizer1512 = wx.BoxSizer( wx.HORIZONTAL )

		self.bConfigureLayoutFT232R = wx.Button( self.pSettingsFT232R, wx.ID_ANY, u"Configure Layout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1512.Add( self.bConfigureLayoutFT232R, 1, wx.ALL, 5 )


		bSizer91.Add( bSizer1512, 1, wx.EXPAND, 5 )


		self.pSettingsFT232R.SetSizer( bSizer91 )
		self.pSettingsFT232R.Layout()
		bSizer91.Fit( self.pSettingsFT232R )
		bSizer8.Add( self.pSettingsFT232R, 1, wx.EXPAND |wx.ALL, 5 )

		self.pSettingsGPIOD = wx.Panel( self.dPage2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pSettingsGPIOD.Hide()

		bSizer912 = wx.BoxSizer( wx.VERTICAL )

		bSizer151222 = wx.BoxSizer( wx.HORIZONTAL )

		self.lGPIODChip = wx.StaticText( self.pSettingsGPIOD, wx.ID_ANY, u"Chip:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lGPIODChip.Wrap( -1 )

		bSizer151222.Add( self.lGPIODChip, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nGPIODChip = wx.SpinCtrl( self.pSettingsGPIOD, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0 )
		self.nGPIODChip.SetMinSize( wx.Size( 200,-1 ) )

		bSizer151222.Add( self.nGPIODChip, 0, wx.ALL, 5 )


		bSizer912.Add( bSizer151222, 0, wx.EXPAND, 5 )

		bSizer15122 = wx.BoxSizer( wx.HORIZONTAL )

		self.bConfigureLayoutGPIOD = wx.Button( self.pSettingsGPIOD, wx.ID_ANY, u"Configure Layout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15122.Add( self.bConfigureLayoutGPIOD, 1, wx.ALL, 5 )


		bSizer912.Add( bSizer15122, 0, wx.EXPAND, 5 )


		self.pSettingsGPIOD.SetSizer( bSizer912 )
		self.pSettingsGPIOD.Layout()
		bSizer912.Fit( self.pSettingsGPIOD )
		bSizer8.Add( self.pSettingsGPIOD, 1, wx.EXPAND |wx.ALL, 5 )

		self.pSettingsParPort = wx.Panel( self.dPage2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pSettingsParPort.Hide()

		bSizer9121 = wx.BoxSizer( wx.VERTICAL )

		bSizer1531 = wx.BoxSizer( wx.HORIZONTAL )

		self.lParCable = wx.StaticText( self.pSettingsParPort, wx.ID_ANY, u"Cable:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lParCable.Wrap( -1 )

		bSizer1531.Add( self.lParCable, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cParCableChoices = [ u"DLC5", u"Wiggler" ]
		self.cParCable = wx.Choice( self.pSettingsParPort, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cParCableChoices, 0 )
		self.cParCable.SetSelection( 0 )
		bSizer1531.Add( self.cParCable, 1, wx.ALL, 5 )


		bSizer9121.Add( bSizer1531, 0, wx.EXPAND, 5 )

		bSizer15131 = wx.BoxSizer( wx.HORIZONTAL )

		self.lParPort = wx.StaticText( self.pSettingsParPort, wx.ID_ANY, u"Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lParPort.Wrap( -1 )

		bSizer15131.Add( self.lParPort, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tParPort = wx.TextCtrl( self.pSettingsParPort, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15131.Add( self.tParPort, 1, wx.ALL, 5 )


		bSizer9121.Add( bSizer15131, 0, wx.EXPAND, 5 )


		self.pSettingsParPort.SetSizer( bSizer9121 )
		self.pSettingsParPort.Layout()
		bSizer9121.Fit( self.pSettingsParPort )
		bSizer8.Add( self.pSettingsParPort, 1, wx.EXPAND |wx.ALL, 5 )

		self.pSettingsRemoteBitbang = wx.Panel( self.dPage2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pSettingsRemoteBitbang.Hide()

		bSizer91211 = wx.BoxSizer( wx.VERTICAL )

		bSizer15311 = wx.BoxSizer( wx.HORIZONTAL )

		self.lRBBHost = wx.StaticText( self.pSettingsRemoteBitbang, wx.ID_ANY, u"Host:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lRBBHost.Wrap( -1 )

		bSizer15311.Add( self.lRBBHost, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tRBBHost = wx.TextCtrl( self.pSettingsRemoteBitbang, wx.ID_ANY, u"127.0.0.1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15311.Add( self.tRBBHost, 1, wx.ALL, 5 )


		bSizer91211.Add( bSizer15311, 0, wx.EXPAND, 5 )

		bSizer151311 = wx.BoxSizer( wx.HORIZONTAL )

		self.lRBBPort = wx.StaticText( self.pSettingsRemoteBitbang, wx.ID_ANY, u"Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lRBBPort.Wrap( -1 )

		bSizer151311.Add( self.lRBBPort, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tRBBPort = wx.TextCtrl( self.pSettingsRemoteBitbang, wx.ID_ANY, u"3463", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer151311.Add( self.tRBBPort, 1, wx.ALL, 5 )


		bSizer91211.Add( bSizer151311, 0, wx.EXPAND, 5 )


		self.pSettingsRemoteBitbang.SetSizer( bSizer91211 )
		self.pSettingsRemoteBitbang.Layout()
		bSizer91211.Fit( self.pSettingsRemoteBitbang )
		bSizer8.Add( self.pSettingsRemoteBitbang, 1, wx.EXPAND |wx.ALL, 5 )

		self.pSettingsFT232H = wx.Panel( self.dPage2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pSettingsFT232H.Hide()

		bSizer911 = wx.BoxSizer( wx.VERTICAL )

		bSizer1521 = wx.BoxSizer( wx.HORIZONTAL )

		self.lFTAdapter = wx.StaticText( self.pSettingsFT232H, wx.ID_ANY, u"Adapter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lFTAdapter.Wrap( -1 )

		bSizer1521.Add( self.lFTAdapter, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cFTAdapterChoices = []
		self.cFTAdapter = wx.Choice( self.pSettingsFT232H, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cFTAdapterChoices, 0 )
		self.cFTAdapter.SetSelection( 0 )
		bSizer1521.Add( self.cFTAdapter, 0, wx.ALL, 5 )


		bSizer911.Add( bSizer1521, 0, wx.EXPAND, 5 )

		bSizer152 = wx.BoxSizer( wx.HORIZONTAL )

		self.lUSBID1 = wx.StaticText( self.pSettingsFT232H, wx.ID_ANY, u"USB ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lUSBID1.Wrap( -1 )

		bSizer152.Add( self.lUSBID1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tUSBID1 = wx.TextCtrl( self.pSettingsFT232H, wx.ID_ANY, u"0x0403:0x6014", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer152.Add( self.tUSBID1, 1, wx.ALL, 5 )


		bSizer911.Add( bSizer152, 0, wx.EXPAND, 5 )

		bSizer1511 = wx.BoxSizer( wx.HORIZONTAL )

		self.lChannel = wx.StaticText( self.pSettingsFT232H, wx.ID_ANY, u"Channel:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lChannel.Wrap( -1 )

		bSizer1511.Add( self.lChannel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cChannelChoices = [ u"0", u"1", u"2", u"3" ]
		self.cChannel = wx.Choice( self.pSettingsFT232H, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cChannelChoices, 0 )
		self.cChannel.SetSelection( 0 )
		bSizer1511.Add( self.cChannel, 1, wx.ALL, 5 )


		bSizer911.Add( bSizer1511, 0, wx.EXPAND, 5 )

		bSizer151111 = wx.BoxSizer( wx.HORIZONTAL )

		rSamplingEdgeChoices = [ u"TCK Rising Edge", u"TCK Falling Edge" ]
		self.rSamplingEdge = wx.RadioBox( self.pSettingsFT232H, wx.ID_ANY, u"Sampling Edge:", wx.DefaultPosition, wx.DefaultSize, rSamplingEdgeChoices, 1, wx.RA_SPECIFY_ROWS )
		self.rSamplingEdge.SetSelection( 0 )
		bSizer151111.Add( self.rSamplingEdge, 1, wx.ALL, 5 )


		bSizer911.Add( bSizer151111, 0, wx.EXPAND, 5 )

		bSizer15121 = wx.BoxSizer( wx.HORIZONTAL )

		self.bConfigureLayoutFT232H = wx.Button( self.pSettingsFT232H, wx.ID_ANY, u"Configure Layout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15121.Add( self.bConfigureLayoutFT232H, 1, wx.ALL, 5 )


		bSizer911.Add( bSizer15121, 1, wx.EXPAND, 5 )


		self.pSettingsFT232H.SetSizer( bSizer911 )
		self.pSettingsFT232H.Layout()
		bSizer911.Fit( self.pSettingsFT232H )
		bSizer8.Add( self.pSettingsFT232H, 1, wx.EXPAND |wx.ALL, 5 )


		self.dPage2.SetSizer( bSizer8 )
		self.dPage2.Layout()
		bSizer8.Fit( self.dPage2 )
		self.tab.AddPage( self.dPage2, u"Additional Settings", False )
		self.dPage3 = wx.Panel( self.tab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer56 = wx.BoxSizer( wx.VERTICAL )

		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )

		self.bDoIDCODE = wx.Button( self.dPage3, wx.ID_ANY, u"IDCODE Scan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer57.Add( self.bDoIDCODE, 0, wx.ALL, 5 )

		self.bDoBYPASS = wx.Button( self.dPage3, wx.ID_ANY, u"BYPASS Scan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer57.Add( self.bDoBYPASS, 0, wx.ALL, 5 )

		self.bDoRTCK = wx.Button( self.dPage3, wx.ID_ANY, u"RTCK Scan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer57.Add( self.bDoRTCK, 0, wx.ALL, 5 )

		self.bUseMPSSE = wx.CheckBox( self.dPage3, wx.ID_ANY, u"Use MPSSE", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer57.Add( self.bUseMPSSE, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer56.Add( bSizer57, 0, wx.EXPAND, 5 )

		self.finderStatus = wx.richtext.RichTextCtrl( self.dPage3, wx.ID_ANY, u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac libero vel massa tristique ullamcorper ac et quam. Nunc ultricies dui nibh, ac auctor augue pulvinar sit amet. Nulla malesuada, arcu eu aliquet semper, leo est tincidunt ante, id aliquet tortor leo vel ex. Suspendisse orci lorem, molestie in auctor in, lacinia a felis. Nam molestie sagittis rutrum. Pellentesque tellus mi, posuere sed bibendum quis, laoreet a dui. In vehicula feugiat est, sit amet pellentesque neque porta sit amet. Nam in elit malesuada, imperdiet dolor eu, maximus elit.\n\nDuis tincidunt ante at massa ornare, in vehicula dolor bibendum. Integer eu est interdum, malesuada ex id, rhoncus lectus. Nullam elementum orci in tellus vestibulum porttitor. Etiam vel lectus aliquet, iaculis erat ac, convallis tortor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed bibendum ultrices tempus. Cras diam felis, sodales a lacinia non, rutrum sit amet nisl. Cras dapibus, ex vitae fringilla convallis, mi lacus faucibus lorem, a aliquam ligula orci in quam. Fusce eu erat maximus, volutpat mauris quis, egestas dolor.\n\nPellentesque elementum ultrices dignissim. Integer bibendum elementum auctor. Nulla facilisi. Integer tristique bibendum facilisis. Morbi id risus molestie, tempor diam non, dignissim mauris. In sit amet orci id tellus fringilla cursus. Nam rhoncus lectus a nibh congue, at fermentum elit accumsan. Proin congue nunc velit, at tempor arcu vulputate vitae. Aenean ac diam quis neque gravida ullamcorper. Pellentesque ac erat ex.\n\nMauris lectus risus, consequat quis eros vitae, feugiat fermentum purus. Aenean risus ipsum, dignissim quis consectetur hendrerit, ultrices sed velit. Duis maximus massa tellus, at blandit elit fringilla nec. Ut luctus facilisis mi, non vehicula lorem sagittis vel. Morbi gravida lacus eu sapien condimentum gravida. Vestibulum consectetur auctor est ac efficitur. Aliquam aliquam commodo nibh. Proin ultricies porttitor arcu id accumsan. Maecenas quam eros, egestas vitae fermentum laoreet, efficitur at lacus.\n\nCurabitur id erat eu sapien volutpat ullamcorper. Nulla volutpat dignissim varius. Duis vulputate imperdiet tincidunt. Aenean in leo feugiat, rhoncus erat quis, sollicitudin sapien. Vivamus imperdiet turpis sit amet velit tristique, in dictum dolor pharetra. Duis efficitur magna nec hendrerit congue. In vel luctus purus. ", wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer56.Add( self.finderStatus, 1, wx.EXPAND |wx.ALL, 5 )


		self.dPage3.SetSizer( bSizer56 )
		self.dPage3.Layout()
		bSizer56.Fit( self.dPage3 )
		self.tab.AddPage( self.dPage3, u"JTAG Finder (FTDI only)", False )
		self.dPage4 = wx.Panel( self.tab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )

		self.bEnableAnalytics = wx.CheckBox( self.dPage4, wx.ID_ANY, u"Enable Analytics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bEnableAnalytics.SetValue(True)
		bSizer45.Add( self.bEnableAnalytics, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lUserID = wx.StaticText( self.dPage4, wx.ID_ANY, u"User ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lUserID.Wrap( -1 )

		bSizer45.Add( self.lUserID, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tUserID = wx.TextCtrl( self.dPage4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer45.Add( self.tUserID, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.bRegenUID = wx.Button( self.dPage4, wx.ID_ANY, u"Regenerate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer45.Add( self.bRegenUID, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer44.Add( bSizer45, 0, wx.EXPAND, 5 )

		self.analytics_stat = wx.richtext.RichTextCtrl( self.dPage4, wx.ID_ANY, u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac libero vel massa tristique ullamcorper ac et quam. Nunc ultricies dui nibh, ac auctor augue pulvinar sit amet. Nulla malesuada, arcu eu aliquet semper, leo est tincidunt ante, id aliquet tortor leo vel ex. Suspendisse orci lorem, molestie in auctor in, lacinia a felis. Nam molestie sagittis rutrum. Pellentesque tellus mi, posuere sed bibendum quis, laoreet a dui. In vehicula feugiat est, sit amet pellentesque neque porta sit amet. Nam in elit malesuada, imperdiet dolor eu, maximus elit.\n\nDuis tincidunt ante at massa ornare, in vehicula dolor bibendum. Integer eu est interdum, malesuada ex id, rhoncus lectus. Nullam elementum orci in tellus vestibulum porttitor. Etiam vel lectus aliquet, iaculis erat ac, convallis tortor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed bibendum ultrices tempus. Cras diam felis, sodales a lacinia non, rutrum sit amet nisl. Cras dapibus, ex vitae fringilla convallis, mi lacus faucibus lorem, a aliquam ligula orci in quam. Fusce eu erat maximus, volutpat mauris quis, egestas dolor.\n\nPellentesque elementum ultrices dignissim. Integer bibendum elementum auctor. Nulla facilisi. Integer tristique bibendum facilisis. Morbi id risus molestie, tempor diam non, dignissim mauris. In sit amet orci id tellus fringilla cursus. Nam rhoncus lectus a nibh congue, at fermentum elit accumsan. Proin congue nunc velit, at tempor arcu vulputate vitae. Aenean ac diam quis neque gravida ullamcorper. Pellentesque ac erat ex.\n\nMauris lectus risus, consequat quis eros vitae, feugiat fermentum purus. Aenean risus ipsum, dignissim quis consectetur hendrerit, ultrices sed velit. Duis maximus massa tellus, at blandit elit fringilla nec. Ut luctus facilisis mi, non vehicula lorem sagittis vel. Morbi gravida lacus eu sapien condimentum gravida. Vestibulum consectetur auctor est ac efficitur. Aliquam aliquam commodo nibh. Proin ultricies porttitor arcu id accumsan. Maecenas quam eros, egestas vitae fermentum laoreet, efficitur at lacus.\n\nCurabitur id erat eu sapien volutpat ullamcorper. Nulla volutpat dignissim varius. Duis vulputate imperdiet tincidunt. Aenean in leo feugiat, rhoncus erat quis, sollicitudin sapien. Vivamus imperdiet turpis sit amet velit tristique, in dictum dolor pharetra. Duis efficitur magna nec hendrerit congue. In vel luctus purus. ", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer44.Add( self.analytics_stat, 1, wx.EXPAND |wx.ALL, 5 )


		self.dPage4.SetSizer( bSizer44 )
		self.dPage4.Layout()
		bSizer44.Fit( self.dPage4 )
		self.tab.AddPage( self.dPage4, u"Analytics", False )

		bSizer3.Add( self.tab, 1, wx.EXPAND |wx.ALL, 5 )

		self.progress = wx.Gauge( self, wx.ID_ANY, 5000, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.progress.SetValue( 2500 )
		bSizer3.Add( self.progress, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.doQuit )
		self.Bind( wx.EVT_IDLE, self.doLoop )
		self.tab.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGING, self.loadNoteBook )
		self.bResetDelay.Bind( wx.EVT_BUTTON, self.bDoConfigureReset )
		self.tStart.Bind( wx.EVT_TEXT, self.doHexCheck )
		self.tEnd.Bind( wx.EVT_TEXT, self.doHexCheck )
		self.bConnect.Bind( wx.EVT_BUTTON, self.doConnect )
		self.bConnectRemote.Bind( wx.EVT_BUTTON, self.doConnectRemote )
		self.bForwardRemote.Bind( wx.EVT_BUTTON, self.doForwardRemote )
		self.bReconnectRemote.Bind( wx.EVT_BUTTON, self.doReconnectRemote )
		self.bDumpFlash.Bind( wx.EVT_BUTTON, self.doReadFlash )
		self.bDumpMemory.Bind( wx.EVT_BUTTON, self.doReadMemory )
		self.bStop.Bind( wx.EVT_BUTTON, self.doStop )
		self.bNandConfigure.Bind( wx.EVT_BUTTON, self.doNANDConfigure )
		self.bGo.Bind( wx.EVT_BUTTON, self.doGo )
		self.bHalt.Bind( wx.EVT_BUTTON, self.doHalt )
		self.bReset.Bind( wx.EVT_BUTTON, self.doReset )
		self.bHardReset.Bind( wx.EVT_BUTTON, self.doHardReset )
		self.bExecScript.Bind( wx.EVT_BUTTON, self.doScript )
		self.bExecLoader.Bind( wx.EVT_BUTTON, self.doLoader )
		self.bEnableMMU.Bind( wx.EVT_BUTTON, self.doEnableMMU )
		self.bDisableMMU.Bind( wx.EVT_BUTTON, self.doDisableMMU )
		self.bExec.Bind( wx.EVT_BUTTON, self.doExecAddress )
		self.tOCDCmd.Bind( wx.EVT_TEXT_ENTER, self.doOCDCmdExec )
		self.bConfigureLayoutFT232R.Bind( wx.EVT_BUTTON, self.doOpenFT232RConfig )
		self.bConfigureLayoutGPIOD.Bind( wx.EVT_BUTTON, self.doOpenGPIODConfig )
		self.cFTAdapter.Bind( wx.EVT_CHOICE, self.doFT232AdapterChange )
		self.bConfigureLayoutFT232H.Bind( wx.EVT_BUTTON, self.doOpenFT232HConfig )
		self.bDoIDCODE.Bind( wx.EVT_BUTTON, self.doIDCODE )
		self.bDoBYPASS.Bind( wx.EVT_BUTTON, self.doBYPASS )
		self.bDoRTCK.Bind( wx.EVT_BUTTON, self.doRTCK )
		self.bRegenUID.Bind( wx.EVT_BUTTON, self.doRegenUUID )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def doQuit( self, event ):
		event.Skip()

	def doLoop( self, event ):
		event.Skip()

	def loadNoteBook( self, event ):
		event.Skip()

	def bDoConfigureReset( self, event ):
		event.Skip()

	def doHexCheck( self, event ):
		event.Skip()


	def doConnect( self, event ):
		event.Skip()

	def doConnectRemote( self, event ):
		event.Skip()

	def doForwardRemote( self, event ):
		event.Skip()

	def doReconnectRemote( self, event ):
		event.Skip()

	def doReadFlash( self, event ):
		event.Skip()

	def doReadMemory( self, event ):
		event.Skip()

	def doStop( self, event ):
		event.Skip()

	def doNANDConfigure( self, event ):
		event.Skip()

	def doGo( self, event ):
		event.Skip()

	def doHalt( self, event ):
		event.Skip()

	def doReset( self, event ):
		event.Skip()

	def doHardReset( self, event ):
		event.Skip()

	def doScript( self, event ):
		event.Skip()

	def doLoader( self, event ):
		event.Skip()

	def doEnableMMU( self, event ):
		event.Skip()

	def doDisableMMU( self, event ):
		event.Skip()

	def doExecAddress( self, event ):
		event.Skip()

	def doOCDCmdExec( self, event ):
		event.Skip()

	def doOpenFT232RConfig( self, event ):
		event.Skip()

	def doOpenGPIODConfig( self, event ):
		event.Skip()

	def doFT232AdapterChange( self, event ):
		event.Skip()

	def doOpenFT232HConfig( self, event ):
		event.Skip()

	def doIDCODE( self, event ):
		event.Skip()

	def doBYPASS( self, event ):
		event.Skip()

	def doRTCK( self, event ):
		event.Skip()

	def doRegenUUID( self, event ):
		event.Skip()


###########################################################################
## Class forwardDialog
###########################################################################

class forwardDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 384,229 ), style = wx.CAPTION|wx.SYSTEM_MENU )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.lPin = wx.StaticText( self, wx.ID_ANY, u"Your Instance Code is:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.lPin.Wrap( -1 )

		self.lPin.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.lPin.SetMinSize( wx.Size( -1,30 ) )

		bSizer23.Add( self.lPin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.lConnect = wx.StaticText( self, wx.ID_ANY, u"Ready to Connect. Time your\nJTAG interface connection\n(click Connect)\nAuto-connect in 15 seconds.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.lConnect.Wrap( -1 )

		self.lConnect.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )
		self.lConnect.Hide()
		self.lConnect.SetMinSize( wx.Size( -1,30 ) )

		bSizer23.Add( self.lConnect, 1, wx.ALL|wx.EXPAND, 5 )

		self.tPin = wx.TextCtrl( self, wx.ID_ANY, u"1a2b3c4d", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_READONLY )
		self.tPin.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer23.Add( self.tPin, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.status = wx.richtext.RichTextCtrl( self, wx.ID_ANY, u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac libero vel massa tristique ullamcorper ac et quam. Nunc ultricies dui nibh, ac auctor augue pulvinar sit amet. Nulla malesuada, arcu eu aliquet semper, leo est tincidunt ante, id aliquet tortor leo vel ex. Suspendisse orci lorem, molestie in auctor in, lacinia a felis. Nam molestie sagittis rutrum. Pellentesque tellus mi, posuere sed bibendum quis, laoreet a dui. In vehicula feugiat est, sit amet pellentesque neque porta sit amet. Nam in elit malesuada, imperdiet dolor eu, maximus elit.\n\nDuis tincidunt ante at massa ornare, in vehicula dolor bibendum. Integer eu est interdum, malesuada ex id, rhoncus lectus. Nullam elementum orci in tellus vestibulum porttitor. Etiam vel lectus aliquet, iaculis erat ac, convallis tortor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed bibendum ultrices tempus. Cras diam felis, sodales a lacinia non, rutrum sit amet nisl. Cras dapibus, ex vitae fringilla convallis, mi lacus faucibus lorem, a aliquam ligula orci in quam. Fusce eu erat maximus, volutpat mauris quis, egestas dolor.\n\nPellentesque elementum ultrices dignissim. Integer bibendum elementum auctor. Nulla facilisi. Integer tristique bibendum facilisis. Morbi id risus molestie, tempor diam non, dignissim mauris. In sit amet orci id tellus fringilla cursus. Nam rhoncus lectus a nibh congue, at fermentum elit accumsan. Proin congue nunc velit, at tempor arcu vulputate vitae. Aenean ac diam quis neque gravida ullamcorper. Pellentesque ac erat ex.\n\nMauris lectus risus, consequat quis eros vitae, feugiat fermentum purus. Aenean risus ipsum, dignissim quis consectetur hendrerit, ultrices sed velit. Duis maximus massa tellus, at blandit elit fringilla nec. Ut luctus facilisis mi, non vehicula lorem sagittis vel. Morbi gravida lacus eu sapien condimentum gravida. Vestibulum consectetur auctor est ac efficitur. Aliquam aliquam commodo nibh. Proin ultricies porttitor arcu id accumsan. Maecenas quam eros, egestas vitae fermentum laoreet, efficitur at lacus.\n\nCurabitur id erat eu sapien volutpat ullamcorper. Nulla volutpat dignissim varius. Duis vulputate imperdiet tincidunt. Aenean in leo feugiat, rhoncus erat quis, sollicitudin sapien. Vivamus imperdiet turpis sit amet velit tristique, in dictum dolor pharetra. Duis efficitur magna nec hendrerit congue. In vel luctus purus. ", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.status.Hide()

		bSizer23.Add( self.status, 1, wx.EXPAND |wx.ALL, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.bStop = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.bStop, 0, wx.ALL, 5 )

		self.bConnect = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bConnect.Enable( False )

		gSizer3.Add( self.bConnect, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer23.Add( gSizer3, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer23 )
		self.Layout()
		self.pConnectTimeout = wx.Timer()
		self.pConnectTimeout.SetOwner( self, self.pConnectTimeout.GetId() )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_IDLE, self.doLoop )
		self.bStop.Bind( wx.EVT_BUTTON, self.doStop )
		self.bConnect.Bind( wx.EVT_BUTTON, self.doConnect )
		self.Bind( wx.EVT_TIMER, self.doConnectTimeout, id=self.pConnectTimeout.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def doLoop( self, event ):
		event.Skip()

	def doStop( self, event ):
		event.Skip()

	def doConnect( self, event ):
		event.Skip()

	def doConnectTimeout( self, event ):
		event.Skip()


###########################################################################
## Class FT232H_Pin_Config
###########################################################################

class FT232H_Pin_Config ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 650,565 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

		self.l_Board = wx.StaticText( self, wx.ID_ANY, u"Board:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.l_Board.Wrap( -1 )

		self.l_Board.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.l_Board.SetMinSize( wx.Size( 72,20 ) )

		bSizer29.Add( self.l_Board, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		c_BoardChoices = []
		self.c_Board = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, c_BoardChoices, 0 )
		self.c_Board.SetSelection( 0 )
		bSizer29.Add( self.c_Board, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer33.Add( bSizer29, 0, wx.ALIGN_RIGHT, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		cfg_p10Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p10 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p10Choices, 0 )
		self.cfg_p10.SetSelection( 6 )
		bSizer36.Add( self.cfg_p10, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p11Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p11 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p11Choices, 0 )
		self.cfg_p11.SetSelection( 6 )
		bSizer36.Add( self.cfg_p11, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p12Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p12 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p12Choices, 0 )
		self.cfg_p12.SetSelection( 6 )
		bSizer36.Add( self.cfg_p12, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p13Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p13 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p13Choices, 0 )
		self.cfg_p13.SetSelection( 6 )
		bSizer36.Add( self.cfg_p13, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p14Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p14 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p14Choices, 0 )
		self.cfg_p14.SetSelection( 6 )
		bSizer36.Add( self.cfg_p14, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p15Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p15 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p15Choices, 0 )
		self.cfg_p15.SetSelection( 6 )
		bSizer36.Add( self.cfg_p15, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p16Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p16 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p16Choices, 0 )
		self.cfg_p16.SetSelection( 6 )
		bSizer36.Add( self.cfg_p16, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p17Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p17 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p17Choices, 0 )
		self.cfg_p17.SetSelection( 6 )
		bSizer36.Add( self.cfg_p17, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer27.Add( bSizer36, 1, wx.EXPAND, 5 )

		self.board = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.board.SetMaxSize( wx.Size( 250,440 ) )

		bSizer27.Add( self.board, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		bSizer361 = wx.BoxSizer( wx.VERTICAL )

		cfg_p20Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p20 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p20Choices, 0 )
		self.cfg_p20.SetSelection( 6 )
		bSizer361.Add( self.cfg_p20, 0, wx.ALL, 5 )

		self.m_staticline9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer361.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p21Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p21 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p21Choices, 0 )
		self.cfg_p21.SetSelection( 6 )
		bSizer361.Add( self.cfg_p21, 0, wx.ALL, 5 )

		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer361.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p22Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p22 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p22Choices, 0 )
		self.cfg_p22.SetSelection( 6 )
		bSizer361.Add( self.cfg_p22, 0, wx.ALL, 5 )

		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer361.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p23Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p23 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p23Choices, 0 )
		self.cfg_p23.SetSelection( 6 )
		bSizer361.Add( self.cfg_p23, 0, wx.ALL, 5 )

		self.m_staticline12 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer361.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p24Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p24 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p24Choices, 0 )
		self.cfg_p24.SetSelection( 6 )
		bSizer361.Add( self.cfg_p24, 0, wx.ALL, 5 )

		self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer361.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p25Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p25 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p25Choices, 0 )
		self.cfg_p25.SetSelection( 6 )
		bSizer361.Add( self.cfg_p25, 0, wx.ALL, 5 )

		self.m_staticline14 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer361.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p26Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p26 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p26Choices, 0 )
		self.cfg_p26.SetSelection( 6 )
		bSizer361.Add( self.cfg_p26, 0, wx.ALL, 5 )

		self.m_staticline15 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer361.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )

		cfg_p27Choices = [ u"TDI", u"TDO", u"TCK", u"TMS", u"TRST", u"SRST", u"High", u"Low", u"RTCK" ]
		self.cfg_p27 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_p27Choices, 0 )
		self.cfg_p27.SetSelection( 6 )
		bSizer361.Add( self.cfg_p27, 0, wx.ALL, 5 )

		self.m_staticline16 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer361.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer27.Add( bSizer361, 1, wx.EXPAND, 5 )


		bSizer33.Add( bSizer27, 1, wx.EXPAND|wx.ALIGN_RIGHT, 5 )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.bApply = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.bApply, 0, wx.ALL, 5 )

		self.bCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.bCancel, 0, wx.ALL, 5 )

		self.bReset = wx.Button( self, wx.ID_ANY, u"Reset to Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.bReset, 0, wx.ALL, 5 )


		bSizer33.Add( bSizer28, 1, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer33 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.c_Board.Bind( wx.EVT_CHOICE, self.doChangeBoard )
		self.cfg_p10.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p11.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p12.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p13.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p14.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p15.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p16.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p17.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p20.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p21.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p22.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p23.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p24.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p25.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p26.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_p27.Bind( wx.EVT_CHOICE, self.doChange )
		self.bApply.Bind( wx.EVT_BUTTON, self.doApply )
		self.bCancel.Bind( wx.EVT_BUTTON, self.doCancel )
		self.bReset.Bind( wx.EVT_BUTTON, self.doReset )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def doChangeBoard( self, event ):
		event.Skip()

	def doChange( self, event ):
		event.Skip()
















	def doApply( self, event ):
		event.Skip()

	def doCancel( self, event ):
		event.Skip()

	def doReset( self, event ):
		event.Skip()


###########################################################################
## Class FT232R_Pin_Config
###########################################################################

class FT232R_Pin_Config ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 380,565 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

		self.l_Board = wx.StaticText( self, wx.ID_ANY, u"Board:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.l_Board.Wrap( -1 )

		self.l_Board.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.l_Board.SetMinSize( wx.Size( 72,20 ) )

		bSizer29.Add( self.l_Board, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		c_BoardChoices = []
		self.c_Board = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, c_BoardChoices, 0 )
		self.c_Board.SetSelection( 0 )
		bSizer29.Add( self.c_Board, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer33.Add( bSizer29, 0, wx.ALIGN_RIGHT, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )

		self.l_tdi = wx.StaticText( self, wx.ID_ANY, u"TDI:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.l_tdi.Wrap( -1 )

		self.l_tdi.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.l_tdi.SetMinSize( wx.Size( 60,20 ) )

		bSizer42.Add( self.l_tdi, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cfg_tdiChoices = [ u"TX", u"RX", u"RTS", u"CTS", u"DTR", u"DSR", u"DCD", u"RI" ]
		self.cfg_tdi = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_tdiChoices, 0 )
		self.cfg_tdi.SetSelection( 1 )
		bSizer42.Add( self.cfg_tdi, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer36.Add( bSizer42, 0, wx.ALIGN_RIGHT, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer421 = wx.BoxSizer( wx.HORIZONTAL )

		self.l_tdo = wx.StaticText( self, wx.ID_ANY, u"TDO:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.l_tdo.Wrap( -1 )

		self.l_tdo.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.l_tdo.SetMinSize( wx.Size( 60,20 ) )

		bSizer421.Add( self.l_tdo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cfg_tdoChoices = [ u"TX", u"RX", u"RTS", u"CTS", u"DTR", u"DSR", u"DCD", u"RI" ]
		self.cfg_tdo = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_tdoChoices, 0 )
		self.cfg_tdo.SetSelection( 2 )
		bSizer421.Add( self.cfg_tdo, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer36.Add( bSizer421, 0, wx.ALIGN_RIGHT, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer422 = wx.BoxSizer( wx.HORIZONTAL )

		self.l_tms = wx.StaticText( self, wx.ID_ANY, u"TMS:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.l_tms.Wrap( -1 )

		self.l_tms.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.l_tms.SetMinSize( wx.Size( 60,20 ) )

		bSizer422.Add( self.l_tms, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cfg_tmsChoices = [ u"TX", u"RX", u"RTS", u"CTS", u"DTR", u"DSR", u"DCD", u"RI" ]
		self.cfg_tms = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_tmsChoices, 0 )
		self.cfg_tms.SetSelection( 3 )
		bSizer422.Add( self.cfg_tms, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer36.Add( bSizer422, 0, wx.ALIGN_RIGHT, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer423 = wx.BoxSizer( wx.HORIZONTAL )

		self.l_tck = wx.StaticText( self, wx.ID_ANY, u"TCK:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.l_tck.Wrap( -1 )

		self.l_tck.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.l_tck.SetMinSize( wx.Size( 60,20 ) )

		bSizer423.Add( self.l_tck, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cfg_tckChoices = [ u"TX", u"RX", u"RTS", u"CTS", u"DTR", u"DSR", u"DCD", u"RI" ]
		self.cfg_tck = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_tckChoices, 0 )
		self.cfg_tck.SetSelection( 0 )
		bSizer423.Add( self.cfg_tck, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer36.Add( bSizer423, 0, wx.ALIGN_RIGHT, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer424 = wx.BoxSizer( wx.HORIZONTAL )

		self.l_trst = wx.StaticText( self, wx.ID_ANY, u"TRST:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.l_trst.Wrap( -1 )

		self.l_trst.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.l_trst.SetMinSize( wx.Size( 60,20 ) )

		bSizer424.Add( self.l_trst, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cfg_trstChoices = [ u"TX", u"RX", u"RTS", u"CTS", u"DTR", u"DSR", u"DCD", u"RI" ]
		self.cfg_trst = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_trstChoices, 0 )
		self.cfg_trst.SetSelection( 4 )
		bSizer424.Add( self.cfg_trst, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer36.Add( bSizer424, 0, wx.ALIGN_RIGHT, 5 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer425 = wx.BoxSizer( wx.HORIZONTAL )

		self.l_srst = wx.StaticText( self, wx.ID_ANY, u"SRST:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.l_srst.Wrap( -1 )

		self.l_srst.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.l_srst.SetMinSize( wx.Size( 60,20 ) )

		bSizer425.Add( self.l_srst, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cfg_srstChoices = [ u"TX", u"RX", u"RTS", u"CTS", u"DTR", u"DSR", u"DCD", u"RI" ]
		self.cfg_srst = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cfg_srstChoices, 0 )
		self.cfg_srst.SetSelection( 6 )
		bSizer425.Add( self.cfg_srst, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer36.Add( bSizer425, 0, wx.ALIGN_RIGHT, 5 )

		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer27.Add( bSizer36, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.board = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.board.SetMaxSize( wx.Size( 250,440 ) )

		bSizer27.Add( self.board, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer33.Add( bSizer27, 1, wx.EXPAND|wx.ALIGN_RIGHT, 5 )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		self.bApply = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.bApply, 0, wx.ALL, 5 )

		self.bCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.bCancel, 0, wx.ALL, 5 )

		self.bReset = wx.Button( self, wx.ID_ANY, u"Reset to Defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.bReset, 0, wx.ALL, 5 )


		bSizer33.Add( bSizer28, 1, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer33 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.c_Board.Bind( wx.EVT_CHOICE, self.doChangeBoard )
		self.cfg_tdi.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_tdo.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_tms.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_tck.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_trst.Bind( wx.EVT_CHOICE, self.doChange )
		self.cfg_srst.Bind( wx.EVT_CHOICE, self.doChange )
		self.bApply.Bind( wx.EVT_BUTTON, self.doApply )
		self.bCancel.Bind( wx.EVT_BUTTON, self.doCancel )
		self.bReset.Bind( wx.EVT_BUTTON, self.doReset )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def doChangeBoard( self, event ):
		event.Skip()

	def doChange( self, event ):
		event.Skip()






	def doApply( self, event ):
		event.Skip()

	def doCancel( self, event ):
		event.Skip()

	def doReset( self, event ):
		event.Skip()


###########################################################################
## Class ResetDelayConfig
###########################################################################

class ResetDelayConfig ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer59 = wx.BoxSizer( wx.VERTICAL )

		bSizer58 = wx.BoxSizer( wx.HORIZONTAL )

		self.lnTRSTWidth = wx.StaticText( self, wx.ID_ANY, u"nTRST Pulse Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lnTRSTWidth.Wrap( -1 )

		bSizer58.Add( self.lnTRSTWidth, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nNTRSTWidth = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0 )
		bSizer58.Add( self.nNTRSTWidth, 0, wx.ALL, 5 )


		bSizer59.Add( bSizer58, 1, wx.EXPAND, 5 )

		bSizer581 = wx.BoxSizer( wx.HORIZONTAL )

		self.lnSRSTWidth = wx.StaticText( self, wx.ID_ANY, u"nSRST Pulse Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lnSRSTWidth.Wrap( -1 )

		bSizer581.Add( self.lnSRSTWidth, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nSRSTWidth = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0 )
		bSizer581.Add( self.nSRSTWidth, 0, wx.ALL, 5 )


		bSizer59.Add( bSizer581, 1, wx.EXPAND, 5 )

		bSizer582 = wx.BoxSizer( wx.HORIZONTAL )

		self.lNTRSTDelay = wx.StaticText( self, wx.ID_ANY, u"nTRST Delay:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lNTRSTDelay.Wrap( -1 )

		bSizer582.Add( self.lNTRSTDelay, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nNTRSTDelay = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0 )
		bSizer582.Add( self.nNTRSTDelay, 0, wx.ALL, 5 )


		bSizer59.Add( bSizer582, 1, wx.EXPAND, 5 )

		bSizer583 = wx.BoxSizer( wx.HORIZONTAL )

		self.lSRSTDelay = wx.StaticText( self, wx.ID_ANY, u"nSRST Delay:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lSRSTDelay.Wrap( -1 )

		bSizer583.Add( self.lSRSTDelay, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nSRSTDelay = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0 )
		bSizer583.Add( self.nSRSTDelay, 0, wx.ALL, 5 )


		bSizer59.Add( bSizer583, 1, wx.EXPAND, 5 )

		bSizer584 = wx.BoxSizer( wx.HORIZONTAL )

		self.lnResetDelay = wx.StaticText( self, wx.ID_ANY, u"Reset Delay", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lnResetDelay.Wrap( -1 )

		bSizer584.Add( self.lnResetDelay, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nResetDelay = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0 )
		bSizer584.Add( self.nResetDelay, 0, wx.ALL, 5 )


		bSizer59.Add( bSizer584, 1, wx.EXPAND, 5 )

		bSizer5842 = wx.BoxSizer( wx.HORIZONTAL )

		self.cUseCustom = wx.CheckBox( self, wx.ID_ANY, u"Use Custom Timings", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		bSizer5842.Add( self.cUseCustom, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer59.Add( bSizer5842, 1, wx.ALIGN_RIGHT, 5 )

		bSizer5841 = wx.BoxSizer( wx.HORIZONTAL )

		self.bApply = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5841.Add( self.bApply, 0, wx.ALL, 5 )

		self.bCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5841.Add( self.bCancel, 0, wx.ALL, 5 )


		bSizer59.Add( bSizer5841, 1, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer59 )
		self.Layout()
		bSizer59.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.bApply.Bind( wx.EVT_BUTTON, self.bDoApply )
		self.bCancel.Bind( wx.EVT_BUTTON, self.bDoCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def bDoApply( self, event ):
		event.Skip()

	def bDoCancel( self, event ):
		event.Skip()


###########################################################################
## Class NANDControllerConfig
###########################################################################

class NANDControllerConfig ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 410,240 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer65 = wx.BoxSizer( wx.VERTICAL )

		bSizer68 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer70 = wx.BoxSizer( wx.VERTICAL )

		bSizer69 = wx.BoxSizer( wx.HORIZONTAL )

		self.lPageWidth = wx.StaticText( self, wx.ID_ANY, u"Page Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lPageWidth.Wrap( -1 )

		bSizer69.Add( self.lPageWidth, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		cPageWidthChoices = [ u"Auto", u"8-bit", u"16-bit" ]
		self.cPageWidth = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cPageWidthChoices, 0 )
		self.cPageWidth.SetSelection( 0 )
		bSizer69.Add( self.cPageWidth, 0, wx.ALL, 5 )


		bSizer70.Add( bSizer69, 0, wx.EXPAND, 5 )

		bSizer691 = wx.BoxSizer( wx.HORIZONTAL )

		self.bSkipRegInit = wx.CheckBox( self, wx.ID_ANY, u"Skip Register Init:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		bSizer691.Add( self.bSkipRegInit, 1, wx.ALL, 5 )


		bSizer70.Add( bSizer691, 0, wx.EXPAND, 5 )

		bSizer6911 = wx.BoxSizer( wx.HORIZONTAL )

		self.bSkipGPIOInit = wx.CheckBox( self, wx.ID_ANY, u"Skip GPIO Init\n(MSM62XX only):", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		bSizer6911.Add( self.bSkipGPIOInit, 1, wx.ALL, 5 )


		bSizer70.Add( bSizer6911, 1, wx.EXPAND, 5 )


		bSizer68.Add( bSizer70, 1, 0, 5 )

		bSizer701 = wx.BoxSizer( wx.VERTICAL )

		bSizer692 = wx.BoxSizer( wx.HORIZONTAL )

		self.lCustomCFG1 = wx.StaticText( self, wx.ID_ANY, u"CFG1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lCustomCFG1.Wrap( -1 )

		bSizer692.Add( self.lCustomCFG1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tCustomCFG1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer692.Add( self.tCustomCFG1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer701.Add( bSizer692, 0, wx.EXPAND, 5 )

		bSizer6912 = wx.BoxSizer( wx.HORIZONTAL )

		self.lCustomCFG2 = wx.StaticText( self, wx.ID_ANY, u"CFG2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lCustomCFG2.Wrap( -1 )

		bSizer6912.Add( self.lCustomCFG2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tCustomCFG2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6912.Add( self.tCustomCFG2, 1, wx.ALL, 5 )


		bSizer701.Add( bSizer6912, 0, wx.EXPAND, 5 )

		bSizer69111 = wx.BoxSizer( wx.HORIZONTAL )

		self.lCustomCFGCMN = wx.StaticText( self, wx.ID_ANY, u"Common\nCFG:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lCustomCFGCMN.Wrap( -1 )

		bSizer69111.Add( self.lCustomCFGCMN, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tCustomCFGCMN = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer69111.Add( self.tCustomCFGCMN, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer701.Add( bSizer69111, 0, wx.EXPAND, 5 )

		bSizer691111 = wx.BoxSizer( wx.HORIZONTAL )

		self.bCodeEdit = wx.Button( self, wx.ID_ANY, u"Edit Init Code", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer691111.Add( self.bCodeEdit, 0, wx.ALL, 5 )


		bSizer701.Add( bSizer691111, 1, wx.ALIGN_RIGHT, 5 )


		bSizer68.Add( bSizer701, 1, wx.EXPAND, 5 )


		bSizer65.Add( bSizer68, 1, wx.EXPAND, 5 )

		bSizer66 = wx.BoxSizer( wx.HORIZONTAL )

		self.bApply = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer66.Add( self.bApply, 0, wx.ALL, 5 )

		self.bCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer66.Add( self.bCancel, 0, wx.ALL, 5 )


		bSizer65.Add( bSizer66, 0, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer65 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.bCodeEdit.Bind( wx.EVT_BUTTON, self.doCodeEdit )
		self.bApply.Bind( wx.EVT_BUTTON, self.doApply )
		self.bCancel.Bind( wx.EVT_BUTTON, self.doCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def doCodeEdit( self, event ):
		event.Skip()

	def doApply( self, event ):
		event.Skip()

	def doCancel( self, event ):
		event.Skip()


###########################################################################
## Class NANDCodeEdit
###########################################################################

class NANDCodeEdit ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 640,480 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer99 = wx.BoxSizer( wx.VERTICAL )

		self.tTCLCode = wx.stc.StyledTextCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.tTCLCode.SetUseTabs ( True )
		self.tTCLCode.SetTabWidth ( 4 )
		self.tTCLCode.SetIndent ( 4 )
		self.tTCLCode.SetTabIndents( True )
		self.tTCLCode.SetBackSpaceUnIndents( True )
		self.tTCLCode.SetViewEOL( False )
		self.tTCLCode.SetViewWhiteSpace( False )
		self.tTCLCode.SetMarginWidth( 2, 0 )
		self.tTCLCode.SetIndentationGuides( True )
		self.tTCLCode.SetReadOnly( False );
		self.tTCLCode.SetMarginType ( 1, wx.stc.STC_MARGIN_SYMBOL )
		self.tTCLCode.SetMarginMask ( 1, wx.stc.STC_MASK_FOLDERS )
		self.tTCLCode.SetMarginWidth ( 1, 16)
		self.tTCLCode.SetMarginSensitive( 1, True )
		self.tTCLCode.SetProperty ( "fold", "1" )
		self.tTCLCode.SetFoldFlags ( wx.stc.STC_FOLDFLAG_LINEBEFORE_CONTRACTED | wx.stc.STC_FOLDFLAG_LINEAFTER_CONTRACTED );
		self.tTCLCode.SetMarginType( 0, wx.stc.STC_MARGIN_NUMBER );
		self.tTCLCode.SetMarginWidth( 0, self.tTCLCode.TextWidth( wx.stc.STC_STYLE_LINENUMBER, "_99999" ) )
		self.tTCLCode.MarkerDefine( wx.stc.STC_MARKNUM_FOLDER, wx.stc.STC_MARK_BOXPLUS )
		self.tTCLCode.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDER, wx.BLACK)
		self.tTCLCode.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDER, wx.WHITE)
		self.tTCLCode.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.stc.STC_MARK_BOXMINUS )
		self.tTCLCode.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.BLACK )
		self.tTCLCode.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.WHITE )
		self.tTCLCode.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERSUB, wx.stc.STC_MARK_EMPTY )
		self.tTCLCode.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEREND, wx.stc.STC_MARK_BOXPLUS )
		self.tTCLCode.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEREND, wx.BLACK )
		self.tTCLCode.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEREND, wx.WHITE )
		self.tTCLCode.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.stc.STC_MARK_BOXMINUS )
		self.tTCLCode.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.BLACK)
		self.tTCLCode.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.WHITE)
		self.tTCLCode.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERMIDTAIL, wx.stc.STC_MARK_EMPTY )
		self.tTCLCode.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERTAIL, wx.stc.STC_MARK_EMPTY )
		self.tTCLCode.SetSelBackground( True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT ) )
		self.tTCLCode.SetSelForeground( True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		bSizer99.Add( self.tTCLCode, 1, wx.EXPAND |wx.ALL, 5 )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.bApply = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.bApply, 0, wx.ALL, 5 )

		self.bCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.bCancel, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer99.Add( gSizer4, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer99 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.bApply.Bind( wx.EVT_BUTTON, self.doApply )
		self.bCancel.Bind( wx.EVT_BUTTON, self.doCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def doApply( self, event ):
		event.Skip()

	def doCancel( self, event ):
		event.Skip()



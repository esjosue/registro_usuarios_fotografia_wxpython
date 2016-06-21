# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  9 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import sys
import wx
import wx.xrc
import sqlite3
import wx.dataview
import time
import conectPostgres as conn

###########################################################################
## Class MyFrame2
###########################################################################



class MyFrame2 ( wx.Frame ):
	
	
	
	
	
	
	def __init__( self, parent ):
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Welcome", pos = wx.DefaultPosition, size = wx.Size( 268,220 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"MENU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 12, 74, 90, 92, False, "Sans" ) )
		fgSizer1.Add( self.m_staticText1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"r.png", wx.BITMAP_TYPE_ANY ) , wx.DefaultPosition,wx.Size( 90,90 ), wx.BU_AUTODRAW )
		fgSizer1.Add( self.m_bpButton1, 0, wx.ALL, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button2 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"busqueda.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size(90,90), wx.BU_AUTODRAW )
		fgSizer1.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.abrir_registro )
		self.m_button2.Bind( wx.EVT_BUTTON, self.abrir_busqueda )
		
		self.postgres = conn.Database()
		
	def __del__( self ):
		pass
	
	def abrir_busqueda( self, event):
		busqueda = MyFrame3(self)
		busqueda.Show()
		
		self.m_button2.Disable()
		
	def abrir_registro( self, event):
		registre= registro(self)
		registre.Show()
		
		self.mbp_Button1.Disable()
		
		
class registro ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Registro", pos = wx.DefaultPosition, size = wx.Size( 475,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer2.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.txt_nombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_nombre, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		#####
		
		self.ruta="sii.jpg"
		img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)
		
		
		##bitmap
		
		
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition, wx.Size( 140,140 ), 0 )
		fgSizer2.Add( self.m_bitmap1, 0, wx.ALL, 5 )
		
		self.user = wx.StaticText( self, wx.ID_ANY, u"Apellido:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.user.Wrap( -1 )
		fgSizer2.Add( self.user, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_apellido = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_apellido, 0, wx.ALL, 5 )
		
		self.btn_foto = wx.Button( self, wx.ID_ANY, u"Foto", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn_foto, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Dirección", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_dir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_dir, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Teléfono:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer2.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_tel = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_tel, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"DUI:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer2.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt_dui = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_dui, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"NIT:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.txt_nit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.txt_nit, 0, wx.ALL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn_guardar = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn_guardar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn_cancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn_cancelar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( fgSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
		
		# Connect Events
		self.btn_guardar.Bind( wx.EVT_BUTTON, self.guardar )
		self.btn_cancelar.Bind( wx.EVT_BUTTON, self.cancelar )
	
	def __del__( self ):
		pass
	def abrir_registro( self, event ):
		registro = registro(self)
		registro.Show()
		
	
	# Virtual event handlers, overide them in your derived class
	def guardar( self, event ):
		self.nombre = str(self.txt_nombre.GetValue())
		self.apellido = str(self.txt_apellido.GetValue()) 
        self.direc = str(self.txt_dir.GetValue()) 
        self.telefono = str(self.txt_tel.GetValue()) 
        self.dui = str(self.txt_dui.GetValue()) 
        self.nit = str(self.txt_nit.GetValue()) 
        sql="INSERT INTO usuarios(nombre,apellido,direccion,telefono,dui,nit) VALUES ('"+self.nombre+"', '"+self.apellido+"','"+self.direccion+"', '"+self.telefono+"', '"+self.dui+"', '"+self.nit+"')"
        data_param=("")
        typesql='I'
        self.dial = wx.MessageDialog(None, 'DATOS GUARDADOS', 'Info', wx.OK|wx.CENTRE)
        if postgres.query(sql,data_param,typesql):
			 self.dial.ShowModal()
	
    #def cancelar( self, event ):
	#	event.Skip()
	
class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Buscar Usuario", pos = wx.DefaultPosition, size = wx.Size( 745,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT ) )
		
		fgSizer3 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Busqueda", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 319,-1 ), 0 )
		fgSizer3.Add( self.m_textCtrl11, 0, wx.ALL, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_dataViewListCtrl3 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 320,440 ), 0 )
		fgSizer3.Add( self.m_dataViewListCtrl3, 0, wx.ALL, 5 )
		
		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.ruta="sii.jpg"
		img = wx.Image(self.ruta, wx.BITMAP_TYPE_ANY)
		
		self.m_bitmap5 = wx.StaticBitmap( self, wx.ID_ANY, wx.BitmapFromImage(img), wx.DefaultPosition, wx.Size( 140,140 ), 0 )
		fgSizer5.Add( self.m_bitmap5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer5.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textCtrl19, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		fgSizer5.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textCtrl21, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Apellido", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		fgSizer5.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textCtrl22, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Dirección", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		fgSizer5.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textCtrl23, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Telefono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer5.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textCtrl24, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"DUI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		fgSizer5.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.m_textCtrl25 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textCtrl25, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"NIT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer5.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.m_textCtrl26 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer5.Add( self.m_textCtrl26, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Modificar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button13 = wx.Button( self, wx.ID_ANY, u"Menu", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer3.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.m_button13.Bind( wx.EVT_BUTTON, self.abrir_menu )
	
	def __del__( self ):
		pass
	def abrir_menu( self, event ):
		menu = MyFrame2(self)
		menu.Show()
		
		#self.m_button2.Disable(True)
		#self.padre = parent
		
		
		


	
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame2(None)
        self.SetTopWindow(frame)
        frame.Show()
        return 1
# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()


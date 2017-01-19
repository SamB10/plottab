import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import wx
from numpy import arange, sin, pi
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

class ExamplePanel(wx.Panel):
    def __init__(self, parent, title):
        wx.Panel.__init__(self, parent, title=title, size=(300,300))
        self.quote = wx.StaticText(self, label="Assuming a completely ionized gas, this program computes the \r density and the total pressure for a given T, P_gas, X and Y.", 
                                   pos=(20, 10))

        #self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), 
        #                          style=wx.TE_MULTILINE | wx.TE_READONLY)
        
        #filemenu = wx.Menu()            
        
        # A button
        self.button = wx.Button(self, label="Calculate", pos=(200, 325))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        
        self.temperature = 0.
        self.pressure = 0.
        self.abdcx = 0.
        self.abdcy = 0.
        
        
        self.lblname = wx.StaticText(self, label="Temperature :",
                                    pos=(20,90))
        self.enterTemperature = wx.TextCtrl(self, pos=(125, 90), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtTemp, self.enterTemperature)
        
        self.lblname = wx.StaticText(self, label="Pressure :",
                                     pos=(20,120))
        self.enterPressure = wx.TextCtrl(self, pos=(125, 120), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtPress, self.enterPressure)
        
        self.lblname = wx.StaticText(self, label="Abundance X :",
                                     pos=(20,150))
        self.enterAbdcx = wx.TextCtrl(self, pos=(125, 150), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtAbdcx, self.enterAbdcx)
        
        self.lblname = wx.StaticText(self, label="Abundance Y :",
                                     pos=(20,180))
        self.enterAbdcy = wx.TextCtrl(self, pos=(125, 180), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtAbdcy, self.enterAbdcy)
        
        self.lblname = wx.StaticText(self, label="Z :",
                                     pos=(335,170))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.enterZ = wx.TextCtrl(self, pos=(350, 170), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtZ, self.enterZ)
        
        self.lblname = wx.StaticText(self, label="mu :",
                                     pos=(320,93))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.enterMu = wx.TextCtrl(self, pos=(350, 90), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtMu, self.enterMu)
        
        self.lblname = wx.StaticText(self, label="P_rad :",
                                     pos=(305,123))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.enterPrad = wx.TextCtrl(self, pos=(350, 120), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtPrad, self.enterPrad)
        
        self.lblname = wx.StaticText(self, label="P_T :",
                                     pos=(190,223))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.enterPT = wx.TextCtrl(self, pos=(220, 220), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtPT, self.enterPT)
        
        self.lblname = wx.StaticText(self, label="Density :",
                                     pos=(160,253))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.enterRho = wx.TextCtrl(self, pos=(220, 250), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtRho, self.enterRho)
        
        #self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        #self.figure = Figure()
        #self.axes = self.figure.add_subplot(211)
        #t = arange(0.0, 3.0, 0.01)
        #s = sin(2 * pi * t)
        
        #self.axes.plot(t, s)
        #self.canvas = FigureCanvas(self, -1, self.figure)    
        
    #    #plt.figure()
    #    #plt.imshow(image_data, cmap='gist_heat',origin='lower')
    #    #plt.colorbar();
            
        #USE SOME SIZERS TO SEE LAYOUT OPTIONS
        #self.sizer = wx.BoxSizer(wx.VERTICAL)
    #    #self.sizer.Add(self.control, 1, wx.EXPAND)
        #self.sizer.Add(self.sizer2, 0, wx.EXPAND)
        #self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        
        #layout sizers
        #self.SetSizer(self.sizer)
        #self.SetAutoLayout(1)
        #self.sizer.Fit(self)
        
        #self.Show()


#    def EvtText(self, event):
 #       self.logger.AppendText('EvtText: %s\n' % event.GetString())
        
    def EvtTemp(self,event):
        self.T = float(self.enterTemperature.GetValue())
        #self.temperature = event.GetString()
        
    def EvtPress(self,event):
        self.Pgas = float(self.enterPressure.GetValue())
        #self.pressure = event.GetString()
        
    def EvtAbdcx(self,event):
        self.X = float(self.enterAbdcx.GetValue())
        #print "self.X"
        #self.abdcx.SetValue()
        #self.abdcx = event.GetString()
        
    def EvtAbdcy(self,event):
        self.Y = float(self.enterAbdcy.GetValue())
        #self.abdcy = event.GetString()
        
    def EvtZ(self,event):
        self.z = event.GetString()
        
    def EvtMu(self,event):
        self.mu = event.GetString()
        
    def EvtPrad(self,event):
        self.prad = event.GetString()
        
    def EvtPT(self,event):
        self.pt = event.GetString()
        
    def EvtRho(self,event):
        self.rho = event.GetString()    
        
    def OnClick(self,event):
        
        if type(self.T) == float: 
            self.T = True 
            self.Pgas = True
            self.X = True
            self.Y = True
        else:
            dlg = wx.MessageDialog(self, "This is not a number. Please introduce a valid input", "Error message", wx.OK)
            dlg.ShowModal() 
            dlg.Destroy()
            
        Z = 1-self.X-self.Y
        mu = 1.0 / (2*self.X + (3.0/4.0)*self.Y + (1.0/2.0)*Z)
        a = 7.56e-15 #erg cm^-3 K^-4 
        R = 8.31447e+7 #erg g^-1 K^-1 
        Prad = (1.0/3.0)*a*((self.T)**4)
        P = Prad*(1.0e-6) + self.Pgas
        rho = (P - Prad*(1.0e-6))*(mu/(R*self.T))
        self.enterMu.SetValue(str(mu))
        self.enterZ.SetValue(str(Z))
        self.enterPrad.SetValue(str(Prad))
        self.enterPT.SetValue(str(P))
        self.enterRho.SetValue(str(rho))
        
#app = wx.App(False)
#frame = ExamplePanel(None, "Sample frame")
#app.MainLoop()
        
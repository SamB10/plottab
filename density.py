import wx
import numpy as np
from numpy import arange
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #Program instructions
        self.quote = wx.StaticText(self, label="Instructions: \r Introduce values for the temperature, total pressure and abundances in \r the appropiated units, then click on 'Calculate' to display the results on \r the right column.", 
                                   pos=(20, 10)) 

        # Create button
        self.button = wx.Button(self, label="Calculate", pos=(70, 250))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        
        self.temperature = 0.
        self.pressure = 0.
        self.abdcx = 0.
        self.abdcy = 0.
        
        # Create boxes and labels for input and output
        self.lblname = wx.StaticText(self, label="Temp.[K] :",
                                    pos=(20,110))
        self.enterTemperature = wx.TextCtrl(self, pos=(125, 110), size=(80,-1))
        self.Bind(wx.EVT_TEXT, self.EvtTemp, self.enterTemperature)
        
        self.lblname = wx.StaticText(self, label="Pressure[bar] :",
                                     pos=(20,140))
        self.enterPressure = wx.TextCtrl(self, pos=(125, 140), size=(80,-1))
        self.Bind(wx.EVT_TEXT, self.EvtPress, self.enterPressure)
        
        self.lblname = wx.StaticText(self, label="Abundance X :",
                                     pos=(20,170))
        self.enterAbdcx = wx.TextCtrl(self, pos=(125, 170), size=(80,-1))
        self.Bind(wx.EVT_TEXT, self.EvtAbdcx, self.enterAbdcx)
        
        self.lblname = wx.StaticText(self, label="Abundance Y :",
                                     pos=(20,200))
        self.enterAbdcy = wx.TextCtrl(self, pos=(125, 200), size=(80,-1))
        self.Bind(wx.EVT_TEXT, self.EvtAbdcy, self.enterAbdcy)
        
        self.lblname = wx.StaticText(self, label="Z :",
                                     pos=(328,170))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.enterZ = wx.TextCtrl(self, pos=(350, 170), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtZ, self.enterZ)
        
        self.lblname = wx.StaticText(self, label="mu :",
                                     pos=(316,85))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.enterMu = wx.TextCtrl(self, pos=(350, 80), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtMu, self.enterMu)
        
        self.lblname = wx.StaticText(self, label="Prad[erg cm^-3] :",
                                     pos=(226,113))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.enterPrad = wx.TextCtrl(self, pos=(350, 110), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtPrad, self.enterPrad)
        
        self.lblname = wx.StaticText(self, label="Pgas[erg cm^-3] :",
                                     pos=(226,143))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.enterPgas = wx.TextCtrl(self, pos=(350, 140), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtPgas, self.enterPgas)
        
        self.lblname = wx.StaticText(self, label="Density[g cm^-3] :",
                                     pos=(222,200))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.enterRho = wx.TextCtrl(self, pos=(350, 200), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtRho, self.enterRho)
        
        self.lblname = wx.StaticText(self, label="log rho :",
                                     pos=(290,230))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.enterLogR = wx.TextCtrl(self, pos=(350, 230), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtLogR, self.enterLogR)
        
        self.lblname = wx.StaticText(self, label="log T :",
                                     pos=(305,260))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.enterLogT = wx.TextCtrl(self, pos=(350, 260), size=(90,-1))
        self.Bind(wx.EVT_TEXT, self.EvtLogT, self.enterLogT)
        
        self.lblname = wx.StaticText(self, label="",
                                     pos=(300,260))
        self.Bind(wx.EVT_TEXT, self.EvtMu, self.enterMu)
        
        self.quote = wx.StaticText(self, label="Now you can look at the graph and check where the obtained values \r for rho and T fall for your star.", 
                                   pos=(20, 310))
        # Create the plot
        self.figure = Figure()
        self.axes = self.figure.add_subplot(311)
        rho = arange(-10.0, 10.0, 1.0)
        t = (1.0/3.0)*(rho)+8
        x = arange(-10.0, 7.0, 1.0)
        y = (2.0/3.0)*x+4
        self.axes.set_ylim(2.0, 10.0, 1.0)
        x1 = arange(6.0, 11.0, 1.0)
        y1 = (1.0/3.0)*x1+6
        y2 = arange(2.0, 9.0, 1.0)
        x2 = (6.0)+0.0*y2

        self.axes.set_xlabel('log rho')
        self.axes.set_ylabel('log T')
        self.axes.set_title('Density as a function of temperature')
        
        self.axes.plot(rho, t, linewidth=0.5, linestyle='dashed')
        self.axes.plot(x, y, linewidth=0.5, linestyle='dashed')
        self.axes.plot(x1, y1, linewidth=0.5, linestyle='dashed')
        self.axes.plot(x2, y2, linewidth=0.5, linestyle='dashed')
        box = self.axes.get_position()
        self.axes.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        self.axes.text(-5,8.5,'radiation', rotation=0, fontsize=10)
        self.axes.text(-5,4.5,'ideal gas', rotation=0, fontsize=10)
        self.axes.text(4,5,'degenerate', rotation=0, fontsize=10)
        self.axes.text(3,4,'NR', rotation=0, fontsize=10)
        self.axes.text(8,4,'ER', rotation=0, fontsize=10)
#        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        self.axes.grid(True)
        
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.lblname, 1, wx.LEFT | wx.BOTTOM | wx.EXPAND)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()
        
    def displayMessage(self,message):
        dlg = wx.MessageDialog(self, message, "Error message", wx.OK)
        dlg.ShowModal() 
        dlg.Destroy()    
        
    # Definitions of the functions    
    def EvtTemp(self,event):
            self.T = float(self.enterTemperature.GetValue())
        
    def EvtPress(self,event):
            self.PT = float(self.enterPressure.GetValue())
        
    def EvtAbdcx(self,event):
        # To show an error message if the user does not enter a number
        try:
            self.X = float(self.enterAbdcx.GetValue())
        except:
            self.displayMessage("X is not a number. Please introduce a valid input.")

    def EvtAbdcy(self,event):
        # To show an error message if the user does not enter a number
        try:
            self.Y = float(self.enterAbdcy.GetValue())
        except:
            self.displayMessage("Y is not a number. Please introduce a valid input.")
        
    def EvtZ(self,event):
        self.z = event.GetString() 
        
    def EvtMu(self,event):
        self.mu = event.GetString()
        
    def EvtPrad(self,event):
        self.prad = event.GetString()
        
    def EvtPgas(self,event):
        self.pgas = event.GetString()
        
    def EvtRho(self,event):
        self.rho = event.GetString()    
        
    def EvtLogR(self,event):
        self.logr = event.GetString()
        
    def EvtLogT(self,event):
        self.logt = event.GetString() 
        
    # Not working yet
    def EvtPlot(self,event):
        self.plot = event.self.axes.text(logr,logt,'o', rotation=0, fontsize=15, color='blue')    
        
    def OnClick(self,event):
        try:
            # Equations and constants
            Z = 1-self.X-self.Y
            mu = 1.0 / (2*self.X + (3.0/4.0)*self.Y + (1.0/2.0)*Z)
            a = 7.56e-15 #erg cm^-3 K^-4 
            R = 8.31447e+7 #erg g^-1 K^-1 
            Prad = (1.0/3.0)*a*((self.T)**4)
            Pgas = self.PT*(1.0e6) - Prad
            rho = (Pgas)*(mu/(R*self.T))
            logr = np.log10(rho)
            logt = np.log10(self.T)
            self.enterMu.SetValue(str(mu))
            self.enterZ.SetValue(str(Z))
            self.enterPrad.SetValue(str(Prad))
            self.enterPgas.SetValue(str(Pgas))
            self.enterRho.SetValue(str(rho))
            self.enterLogR.SetValue(str(logr))
            self.enterLogT.SetValue(str(logt))
            self.axes.text(logr,logt,'o', rotation=0, fontsize=15, color='blue')
        except:
            if type(self.X) != float: 
                dlg = wx.MessageDialog(self, "T is not a float. Please introduce a valid input", "Error message", wx.OK)
                dlg.ShowModal() 
                dlg.Destroy()

# To create the frame
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(550,800))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() 

        # To create a menu
        filemenu= wx.Menu()

        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # To create the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") 
        self.SetMenuBar(menuBar)

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)
    
    # Description of the program
    def OnAbout(self,e):
        dlg = wx.MessageDialog( self, "This program computes the density and the gas and radiation pressures for a given T, P, X and Y, assuming a completely ionized gas.", "About Star's density", wx.OK)
        dlg.ShowModal() 
        dlg.Destroy() 

    # To close the program when clicking on Quit    
    def OnExit(self,e):
        self.Close(True)  

app = wx.App(0)
frame = MainWindow(None, "Star's density")
nb = wx.Notebook(frame)
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()
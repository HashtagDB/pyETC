# Titolo del tool
__title__= 'Crea grafico'

# Tooltip visualizzabile quando il cursore passa sopra il tool
# Per i commenti serve uno spazio dopo il cancelletto e no caretteri speciali come i caratteri accentati
"""Crea grafico da dati strutturati"""

# Autore del tool
__author__= 'RP'

import clr
import System

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *

clr.AddReference("RevitServices") #permette di importare le librerie del Documento attivo e del Transaction necessarie per utilizzare le API
import RevitServices
from RevitServices.Persistence import DocumentManager #permette di importare il modulo del documento attivo
from RevitServices.Transactions import TransactionManager #permette di importare il modulo per eseguire modifiche

# Metodi di INPUT finestre popup pyRevit
from pyrevit import forms
from pyrevit.forms import ProgressBar

# Metodi di OUTPUT finestre popup pyRevit"
from pyrevit import script

from pyrevit import coreutils
from collections import defaultdict
from pyrevit import HOST_APP
from pyrevit.framework import List


doc = __revit__.ActiveUIDocument.Document
uidoc =  __revit__.ActiveUIDocument


# Richiamo finestra output vuota
output = script.get_output()

#Crea una chartline con il metodo
chart = output.make_line_chart() 

h=500
height= 'height:{}px'.format(h)

# Cambiamo la dimensione della chartline
chart.set_style('height:500px')
#chart.set_style(height)

#Settiamo le impostazioni principali
chart.options.title = {'display':True, 'text':'Chart Title', 'fontSize': 18, 'fontColor':'#000', 'fontStyle':'bold'}

#Dati sulla X
chart.data.labels = ['Lun','Mar','Mer','Gio','Ven','Sab','Dom']

#Creo il primo set di dati
set_a=chart.data.new_dataset('Set A')
#Aggiungo i dati
set_a.data = [1,2,3,4,5,6,7]
#Setto il colore LSL color
set_a.set_color(0xFF, 0x8c, 0x8D, 0.8)

#Creo il secondo set di dati
set_b=chart.data.new_dataset('Set B')
#Aggiungo i dati
set_a.data = [10,20,30,40,50,60,70]
#Setto il colore
set_a.set_color(0xFF, 0xCE, 0x56, 0.8)

#Creo il terzo set di dati
set_c=chart.data.new_dataset('Set C')
#Aggiungo i dati
set_c.data = [100,200,300,400,500,600,700]
#Setto il colore
#Posso utilizzare notazione RGB
set_c.set_color(100,100,100, 0.8)
#Posso modificare il riempimento
set_c.fill=False

chart.draw()



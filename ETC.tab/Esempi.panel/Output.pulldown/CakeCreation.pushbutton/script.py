# Titolo del tool
__title__= 'Crea grafico a torte'

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

chart = output.make_pie_chart()

h=500
height= 'height:{}px'.format(h)

# Cambiamo la dimensione della chartline
chart.set_style('height:500px')
#chart.set_style(height)

#Settiamo le impostazioni principali
chart.options.title = {'display':True, 'text':'Chart Title', 'fontSize': 18, 'fontColor':'#000', 'fontStyle':'bold'}

chart.data.labels = ['A','B','C']

#Creo il primo set di dati
set_a=chart.data.new_dataset('Set A')
#Aggiungo i dati
set_a.data = [10,20,30]
#Setto il colore
set_a.backgroundColor = ["#560764", "#1F6CB0", "#F98B60"]

#Creo il secondo set di dati
set_b=chart.data.new_dataset('Set B')
#Aggiungo i dati
set_b.data = [100,200,300]
#Setto il colore
set_b.backgroundColor = ["#913175", "#70A3C4", "#FFC057"]

#Creo il terzo set di dati
set_c=chart.data.new_dataset('Set C')
#Aggiungo i dati
set_c.data = [1000,2000,3000]
#Setto il colore
set_c.backgroundColor = ["#DD5B82", "#E7E8F5", "#FFE084"]

chart.draw()





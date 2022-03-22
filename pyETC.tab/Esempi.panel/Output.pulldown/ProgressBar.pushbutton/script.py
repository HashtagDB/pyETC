# Titolo del tool
__title__= 'Progress bar'

# Tooltip visualizzabile quando il cursore passa sopra il tool
# Per i commenti serve uno spazio dopo il cancelletto e no caretteri speciali come i caratteri accentati
"""Selezione multipla da una lista strutturata"""

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

max_value = 100

# Progressbar semplice
'''
with ProgressBar() as pb:
'''

# Progressbar con titolo e avanzamento
'''
with ProgressBar(title='Avanzamento...({value} of {max_value})') as pb:
    for counter in range(0, max_value):
        pb.update_progress(counter, max_value)
'''

# Progressbar con titolo avanzamento e possibilita di arrestare
'''
with ProgressBar(title='Avanzamento...({value} of {max_value})',cancellable=True) as pb:
    for counter in range(0, max_value):
        if pb.cancelled:
            break
        else:
            pb.update_progress(counter, max_value)
'''

# Progressbar con titolo avanzamento possibilita di arrestare step
with ProgressBar(title='Avanzamento...({value} of {max_value})',cancellable=True, indeterminate=True, step=10) as pb:
    for counter in range(0, max_value):
        if pb.cancelled:
            break
        else:
            pb.update_progress(counter, max_value)

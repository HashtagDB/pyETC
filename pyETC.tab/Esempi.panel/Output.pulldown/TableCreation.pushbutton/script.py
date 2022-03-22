# Titolo del tool
__title__= 'Crea tabella'

# Tooltip visualizzabile quando il cursore passa sopra il tool
# Per i commenti serve uno spazio dopo il cancelletto e no caretteri speciali come i caratteri accentati
"""Crea tabella da dati strutturati"""

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

data = [['A','B','C',80],['D','E','F',100],['G','H','I',20]]

output.print_table(table_data = data,
    title = 'Tabella di esempio',
    columns=["Col1","Col2","Col3","%"],
    formats=['','','','{}%'],
    last_line_style='color:red;')
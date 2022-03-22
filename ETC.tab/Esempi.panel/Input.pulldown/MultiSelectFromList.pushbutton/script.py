# Titolo del tool
__title__= 'Selezione multipla'

# Tooltip visualizzabile quando il cursore passa sopra il tool
# Per i commenti serve uno spazio dopo il cancelletto e no caretteri speciali come i caratteri accentati
"""Selezione multipla da una lista strutturata"""

#Autore del tool
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

#Metodi di INPUT finestre popup pyRevit
from pyrevit import forms

#Metodi di OUTPUT finestre popup pyRevit"
from pyrevit import script

from pyrevit import coreutils
from collections import defaultdict
from pyrevit import HOST_APP
from pyrevit.framework import List



doc = __revit__.ActiveUIDocument.Document
uidoc =  __revit__.ActiveUIDocument

'''
#Richiedere all'utente di inserire una stringa
valuestring = forms.ask_for_string(
    default = 'Valore di default',
    prompt = 'Descrizione dell azione',
    title = 'Inserimento stringa per parametro')
'''
'''
#Richiedere all utente di scegliere un input da una lista
valueuniqueitem = forms.ask_for_one_item(
    ['Item 1', 'Item 2', 'Item 3'],
    default = 'Item',
    prompt = 'test',
    title = 'Titolo')
'''

result = forms.SelectFromList.show(
        {'All': '1 2 3 4 5 6 7 8 9 0'.split(),
        'Pari': '2 4 6 8 0'.split(),
        'Dispari': '1 3 5 7 9'.split()},
        title = 'MultiGroupList',
        group_selector_title = 'Select Integer Range',
        multiselect = True
    )


#Richiamo finestra output vuota
output = script.get_output()
#Scrivo nella prima riga della finestra di putput, print_md permette di formattare le scritte con cancelletto
#output.print_md(valueuniqueitem)

#Non posso scrivere in output dei numeri, per essere sicuri che result sia composto da stringhe applichiamo un .format alla lista
output.print_md('{}'.format(result))

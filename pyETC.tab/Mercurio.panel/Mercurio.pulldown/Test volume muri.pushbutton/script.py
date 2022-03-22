# Titolo del tool
__title__= 'Test volume muri'

# Tooltip visualizzabile quando il cursore passa sopra il tool
# Per i commenti serve uno spazio dopo il cancelletto e no caretteri speciali come i caratteri accentati
"""Estrazione dati da modelli collegati"""

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



# Boilerplate text
import clr #permette di entrare in comunicazione tra le dll "common language runtime" ----Sempre necessario----

import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')

import System   #permette di importare la libreria dei metodi interni del sistema windows ----Eliminare se non necessario----
from System import Array
from System.Collections.Generic import *

clr.AddReference('ProtoGeometry') #permette di importare la libreria delle geometrie di Dynamo
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitNodes") #permette di importare la libreria delle classi Revit di Dynamo
import Revit
clr.ImportExtensions(Revit.Elements) #Permette di importare il ToDSType
clr.ImportExtensions(Revit.GeometryConversion) #Permette di importare i metodi per convertire 

clr.AddReference("RevitServices") #permette di importare le librerie del Documento attivo e del Transaction necessarie per utilizzare le API
import RevitServices
from RevitServices.Persistence import DocumentManager #permette di importare il modulo del documento attivo
from RevitServices.Transactions import TransactionManager #permette di importare il modulo per eseguire modifiche

clr.AddReference("RevitAPI")  #permette di utilizzare la libreria delle APIdocs  ----Eliminare se non necessario----
clr.AddReference("RevitAPIUI") #permette di utilizzare l'User Interface e l'applicazione corrente di Revit ----Eliminare se non necessario----

import Autodesk 
from Autodesk.Revit.DB import *    #importare tutte le classi delle API  ----Eliminare se non necessario----
from Autodesk.Revit.UI import *    #importare tutte le classi delle APIUI  ----Eliminare se non necessario----


doc = __revit__.ActiveUIDocument.Document
uidoc =  __revit__.ActiveUIDocument

collector = FilteredElementCollector(doc)
linkInstances = collector.OfClass(RevitLinkInstance)

linkDoc, linkName, linkInstId, linktype, link = [], [], [], [], []
for i in linkInstances:
	link.append(i)
	linkDoc.append(i.GetLinkDocument())
	linkName.append(i.Name)
	linkInstId.append(i.Id)
	linktype.append(i.GetTypeId())


#Richiesta scelta modello collegato
linkmodel = forms.SelectFromList.show(
        {'All': linkName
        },
        title = 'MultiGroupList',
        group_selector_title = 'Select Linked Model',
        multiselect = True
    )

lista_cat=['Walls']

#Richiesta scelta categorie da analizzare
categorie = forms.SelectFromList.show(
        {'All': lista_cat
        },
        title = 'MultiGroupList',
        group_selector_title = 'Select Linked Model',
        multiselect = True
    )


cat=[]
for i in categorie:
	cat.append('1')

output=script.get_output()
for i in cat:
    output.print_md(i)

TransactionManager.Instance.EnsureInTransaction(doc)
a=Revit.Elements.Category.ByName('Walls')

TransactionManager.Instance.TransactionTaskDone()
#Revit.Elements.Category.ByName(i)

'''
cat=[]
for i in categorie:
	cat.append(Revit.Elements.Category.ByName(i))
'''

'''
#Richiamo finestra output vuota
output = script.get_output()
#Scrivo nella prima riga della finestra di putput, print_md permette di formattare le scritte con cancelletto
output.print_md('#Categorie selezionate')
for i in cat:
    output.print_md(i.Name)
'''


'''
data = [['A','B','C',80],['D','E','F',100],['G','H','I',20]]

output.print_table(table_data = data,
    title = 'Tabella di esempio',
    columns=["Col1","Col2","Col3","%"],
    formats=['','','','{}%'],
    last_line_style='color:red;')
'''

'''   
titoli=[]
for i in categorie:
    titoli.append(i.Name)
'''  
    
'''   
output.print_table(table_data = cat,
    title = 'Tabella riassuntiva',
    columns=titoli,
    formats=['','','','{}%'],
    last_line_style='color:red;')
'''


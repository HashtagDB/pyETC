import clr
import System
from System.Collections.Generic import *

clr.AddReference("RevitServices") 
import RevitServices
from RevitServices.Persistence import DocumentManager 
from RevitServices.Transactions import TransactionManager 

clr.AddReference("RevitAPI") 
clr.AddReference("RevitAPIUI") 

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

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

out=[]


# CategoryType == 'Model'
categories = doc.Settings.Categories
filtro=[]
filtro_cat=[]
for i in categories:
    if i.CategoryType == CategoryType.Model:
        if 'dwg' not in i.Name and i.SubCategories.Size > 0 or i.CanAddSubcategory:
            filtro.append(i.Name)
            filtro_cat.append(i)

sort_cat=sorted(filtro)

#Richiedere all utente di scegliere un input da una lista
valueuniqueitem = forms.ask_for_one_item(
    sort_cat,
    default = '',
    prompt = 'Selezionare la categoria dalla lista',
    title = 'Selezione categoria da eliminare')


for i,j in zip(filtro,filtro_cat):
	if i==valueuniqueitem:
		out=j

collector_ist = FilteredElementCollector(doc).OfCategoryId(out.Id).WhereElementIsNotElementType().ToElements()

t = Transaction(doc,'Canc')
t.Start()

try:
    for i in collector_ist:
        x=i.Id
        doc.Delete(x)
except:
    t.Rollback()
else:
    t.Commit()


#SELEZIONE TAVOLE
collector_sht = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets).WhereElementIsNotElementType().ToElements()

par_tot=collector_sht[0].Parameters

par_name_temp=[]
for i in par_tot:
    par_name_temp.append(i.Definition.Name)

par_name=sorted(par_name_temp)


#Richiedere all utente di scegliere un input da una lista
par_b = forms.ask_for_one_item(
    par_name,
    default = '',
    prompt = 'Selezionare parametro dalla lista',
    title = 'Selezione parametro da compilare')    

t = Transaction(doc,'Par Custom')
t.Start()

try:
    for i in collector_sht:
        par= i.LookupParameter(par_b)
        par.Set('OK')

except:
    t.Rollback()
else:
    t.Commit()

        








'''
# Creiamo oggetto transaction
# Su pyRevit ad ogni modifica singola deve corrispondere una transaction
# Uso il metodo Transaction con assegnazione di un nome
t = Transaction(doc,'Azione 1')

# La transazione deve essere avviata
t.Start()

# Ora posso eseguire le modifiche al database
'''

'''
# Per chiudere la transaction eseguo un update del documento e poi chiudo
t.RollBack()
t.Commit()
'''



'''
# Per essere sicuro che funzioni posso scrivere:
try:
    #Modifiche al database
except:
    t.Rollback()
else:
    t.Commit()
'''



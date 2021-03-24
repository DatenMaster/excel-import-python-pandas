'''
Created on 23 Mar 2021

@author: Daten Master
'''

import pandas as pd

##############################################################
################ .CSV-Datei einlesen #########################
##############################################################

#dateipfad = '/Users/.../Desktop/DATEN.csv'
#dataframe_csv = pd.read_csv(dateipfad, sep=';')
#print(dataframe_csv)

##############################################################
################ .XLSX-Datei einlesen #########################
##############################################################

dateipfad = '/Users/.../Desktop/DATEN.xlsx'
dataframe_xlsx = pd.read_excel(dateipfad)
print(dataframe_xlsx)

##############################################################
################ Datenuebersicht #############################
##############################################################

# Informationen bezgl. Datentypen etc. ausgeben
dataframe_xlsx.info()
# Anzahl der leeren Werte ausgeben
print(dataframe_xlsx.isnull().sum())
# statistische Kennzahlen ausgeben
print(dataframe_xlsx.describe())

##############################################################
################ Datenselektion ##############################
##############################################################

# alle Werte fuer Spalte 1 ausgeben
print(dataframe_xlsx['SPALTE_1'])
# alle Werte fuer Spalte 1 und 4 ausgeben
print(dataframe_xlsx[['SPALTE_1', 'SPALTE_4']])
# Wert aus Spalte 4 in Zeile 3 ausgeben
print(dataframe_xlsx['SPALTE_4'][3])

##############################################################
################ Daten schreiben #############################
##############################################################

# leeren Werte in Spalte 4 Zeile 3 mit Wert 99 ersetzen/ueberschreiben
dataframe_xlsx['SPALTE_4'][3] = 99
print(dataframe_xlsx['SPALTE_4'][3])

##############################################################
################ Datenexport #################################
##############################################################

# Export als .XLSX-Datei
dataframe_xlsx.to_excel('/Users/.../Desktop/DATEN_EXPORT.xlsx', index = False)
# Export als .CSV-Datei
#dataframe_csv.to_csv('/Users/.../Desktop/DATEN_EXPORT.csv', sep=';', index = False)
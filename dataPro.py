import pandas as pd
import datetime

class Data:
    def dataClean()->pd.DataFrame:
        dfProduits = pd.read_csv('C:\\Users\Joe\Desktop\py\melomane-flo_branch\olist\projects\produits.csv')
        
        dfClients = pd.read_csv('C:\\Users\Joe\Desktop\py\melomane-flo_branch\olist\projects\clients.csv')
        dfClients
       
        dfVentes = pd.read_csv('C:\\Users\Joe\Desktop\py\melomane-flo_branch\olist\projects\\ventes.csv')
        dfMerge1 = pd.merge(dfProduits, dfVentes, left_on='id_prod', right_on='id_prod')
        dfMerge1
        dfMergeFinale = pd.merge(dfClients, dfMerge1, left_on='client_id', right_on='client_id')
        dfClean1 = dfMergeFinale[dfMergeFinale.price >= 0]
        dfClean1['date'] = pd.to_datetime(dfClean1['date'], format="%Y-%m-%d %H:%M:%S.%f")
        dfClean1
        return dfClean1
    x= dataClean()
    print(x)

    
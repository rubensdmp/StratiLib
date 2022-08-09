import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
from .defaults import *
from .sedlogdef import *
from .functions import *


#---------------------------------------------- READ SEDLOG -----------------------------------------------


def read_sedlog(name):
    '''
    Args:
        path and name of file
    '''
    def mapstructs(s):
        structs = ''
        for st in s.split(','):
            structs += ',' + DICT_SL_DF_STRUCTURES.get(st,'')
        return structs[1:]

    def mapsfoss(s):
        foss = ''
        for st in s.split(','):
            foss += ',' + DICT_SL_DF_FOSSILS.get(st,'')
        return foss[1:]
    
    
    base, tope = 0, 0
    
    df = pd.read_csv(name, encoding="windows_1258")
    df.sort_index(ascending = False, inplace = True)
    df.reset_index(inplace= True)
    df.drop(columns='index', inplace = True)
    
    
    df.rename(columns = {'THICKNESS (CM)':'THICKNESS'}, inplace = True)
    
    df['TOP'] = 0
    df['BASE'] = 0
    for i in range(len(df)):
        base += df.loc[i,'THICKNESS']/100
        df.loc[i,'TOP'] = tope  
        df.loc[i,'BASE'] = base
        tope += df.loc[i,'THICKNESS']/100
        
    #df['LITHOLOGY'] = df['LITHOLOGY'].map(DICT_SL_DF_LITHO)
    df['LITH1'] = df['LITHOLOGY'].map(DICT_SL_DF_LITHO).map(DICT_LITHO)
    df['LITH1%'] = df['LITHOLOGY %'].astype(float)/100
    df['LITH2'] = df['LITHOLOGY2']
    df['LITH2'][df['LITH2']=='<none>'] = np.nan 
    df['LITH2'] = df['LITH2'].map(DICT_SL_DF_LITHO).map(DICT_LITHO)
    df['LITH2%'] = df['LITHOLOGY2 %'].astype(float)/100
    df['LITH3'] = df['LITHOLOGY3']
    df['LITH3'][df['LITH3']=='<none>'] = np.nan 
    df['LITH3'] = df['LITH3'].map(DICT_SL_DF_LITHO).map(DICT_LITHO)
    df['LITH3%'] = df['LITHOLOGY3 %'].astype(float)/100
    
    df['DESC'] = df['NOTES COLUMN']
    df['DESC'].fillna('', inplace=True)
    df['CONTACT'] = df['BASE BOUNDARY'].map(DICT_SL_DF_CONTACTS)
    df['GRAINB'] = df['GRAIN SIZE BASE'].map(DICT_SL_DF_GRAINS).map(DICT_GRAIN)
    df['GRAINT'] = df['GRAIN SIZE TOP'].map(DICT_SL_DF_GRAINS).map(DICT_GRAIN)
            
    df['SYMBOLS/STRUCTURES'].fillna('<none>', inplace=True)    
    
    #Sedimentary structures
    df['STRUCTURES'] = list(map(mapstructs,df['SYMBOLS IN BED']))
    df['STRUCTURES'] = df['STRUCTURES'] + ','
    df['STRUCTURES'] = df['STRUCTURES'] + list(map(mapstructs,df['SYMBOLS/STRUCTURES']))
    df['STRUCTURES'] = df['STRUCTURES'].str.lstrip(',')
    df['STRUCTURES'] = df['STRUCTURES'].str.rstrip(',')
    df['STRUCTURES'][df['STRUCTURES']==','] = np.nan
    df['STRUCTURES'][df['STRUCTURES']==''] = np.nan

    #Fossils
    df['FOSSILS'] = list(map(mapsfoss,df['SYMBOLS IN BED']))
    df['FOSSILS'] = df['FOSSILS'] + ','
    df['FOSSILS'] = df['FOSSILS'] + list(map(mapsfoss,df['SYMBOLS/STRUCTURES']))
    df['FOSSILS'] = df['FOSSILS'].str.lstrip(',')
    df['FOSSILS'] = df['FOSSILS'].str.rstrip(',')
    df['FOSSILS'][df['FOSSILS']==','] = np.nan
    df['FOSSILS'][df['FOSSILS']==''] = np.nan
        
    return df







#---------------------------------------------- TO SEDLOG CSV -----------------------------------------------

def to_sedlog_csv(df,name):
    '''
    Args:
        df: Pandas dataframe from read_litho() or read_sedlog()
        name: name of output csv file.
    '''
    
    
    def structs_to_csv(s1, s2):
        structs = ''        
        if not pd.isna(s1):
            for st in s1.split(','):
                structs += ',' + DICT_DF_SL_STRUCTURES.get(st,'')
        if not pd.isna(s2):            
            for st in s2.split(','):
                structs += ',' + DICT_DF_SL_FOSSILS.get(st,'')
        return structs[1:]

    
    NO_SEDLOG = False
    
    list_keys = df['LITH1'].unique().tolist() + df['LITH2'][df['LITH2'].isnull()==False].unique().tolist() + df['LITH3'][df['LITH3'].isnull()==False].unique().tolist()
    no_sedlog_lith = []
    for key in list_keys:
        if LITHOLOGIES[key]['sedlog'] == False:
            no_sedlog_lith.append(LITHOLOGIES[key]['lith'])
            NO_SEDLOG = True

    
    if NO_SEDLOG:
        print('The lithologies below are not in SedLog 3.1.')
        print(no_sedlog_lith)
        print('Please modify lithologies in input excel file to generate sedlog csv file.')
    else:
        sedLogCSV = pd.DataFrame()
        vacio ='""'

        for i in range(len(df)-1,-1,-1):
            sedLogCSV = sedLogCSV.append(
                {'THICKNESS (CM)': df['THICKNESS'][i], 
                 'BASE BOUNDARY': DICT_DF_SL_CONTACTS.get(df['CONTACT'][i]) if df['CONTACT'][i] in DICT_DF_SL_CONTACTS else '<none>', 
                 'LITHOLOGY': DICT_DF_SL_LITHO.get(DICT_LITHO_RV.get(df['LITH1'][i])), 
                 'LITHOLOGY %': df['LITH1%'][i]*100,
                 'LITHOLOGY2': DICT_DF_SL_LITHO.get(DICT_LITHO_RV.get(df['LITH2'][i])) if not pd.isna(df['LITH2'][i]) else '<none>',
                 'LITHOLOGY2 %': df['LITH2%'][i]*100, 
                 'LITHOLOGY3': DICT_DF_SL_LITHO.get(DICT_LITHO_RV.get(df['LITH3'][i])) if not pd.isna(df['LITH3'][i]) else '<none>', 
                 'LITHOLOGY3 %': df['LITH3%'][i]*100,
                 'GRAIN SIZE BASE': DICT_DF_SL_GRAINS.get(DICT_GRAIN_RV.get(df['GRAINB'][i])) if not pd.isna(df['GRAINB'][i]) else '<none>',
                 'PHI VALUES BASE': DICT_DF_SL_PHI.get(DICT_GRAIN_RV.get(df['GRAINB'][i])) if not pd.isna(df['GRAINB'][i]) else 0.0, 
                 'GRAIN SIZE TOP': DICT_DF_SL_GRAINS.get(DICT_GRAIN_RV.get(df['GRAINT'][i])) if not pd.isna(df['GRAINT'][i]) else '<none>',
                 'PHI VALUES TOP': DICT_DF_SL_PHI.get(DICT_GRAIN_RV.get(df['GRAINT'][i])) if not pd.isna(df['GRAINB'][i]) else 0.0, 
                 'SYMBOLS IN BED': '<none>', 
                 'SYMBOLS/STRUCTURES': str(structs_to_csv(df['STRUCTURES'][i],df['FOSSILS'][i])),
                 'NOTES COLUMN': df['DESC'][i],             
                 'BIOTURBATION TYPE':  '<none>', 
                 'INTENSITY': '0',
                 'PALAEOCURRENT VALUES': vacio, 
                 'FACIES': '0', 
                 'OTHER1 TEXT': vacio, 
                 'OTHER1 SYMBOL': vacio,
                 'OTHER2 TEXT': vacio, 
                 'OTHER2 SYMBOL': vacio,                      
                 'OTHER3 TEXT': vacio, 
                 'OTHER3 SYMBOL': vacio}

                ,ignore_index =True)

        #sedLogCSV.to_csv("sedLogCSV.csv", index =False, quoting=csv.QUOTE_NONE)
        sedLogCSV.to_csv(name + '.csv', index =False)
        return sedLogCSV


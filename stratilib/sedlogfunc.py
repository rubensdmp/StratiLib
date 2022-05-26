def to_sedlog_csv(datos):
    #Columnas del SedLog para cargar por CSV
    sedLogCSV = pd.DataFrame()
    vacio ='""'

    for i in range(len(datos)):
        sedLogCSV = sedLogCSV.append(
            {'THICKNESS (CM)': datos['Espesor'][i], 
             'BASE BOUNDARY': DICT_SL_CONTACTS.get(datos['Contacto'][i]) if datos['Contacto'][i] in DICT_SL_CONTACTS else '<none>', 
             'LITHOLOGY': DICT_SL_LITHO.get(datos['Litología'][i]), 
             'LITHOLOGY %': '100',
             'LITHOLOGY2': '<none>', #if pd.isna(datos['Litología 2'][i]) else getLitho(datos['Litología 2'][i]),
             'LITHOLOGY2 %': '0', 
             'LITHOLOGY3': '<none>', 
             'LITHOLOGY3 %': '0',
             'GRAIN SIZE BASE': DICT_SL_GRAINS.get(datos['Granulometría'][i]) if datos['Granulometría'][i] in DICT_SL_GRAINS else '<none>',
             'PHI VALUES BASE': 0, 
             'GRAIN SIZE TOP': DICT_SL_GRAINS.get(datos['Granulometría'][i]) if datos['Granulometría'][i] in DICT_SL_GRAINS else '<none>',
             'PHI VALUES TOP': 0, 
             'SYMBOLS IN BED': DICT_SL_STRUCTURES.get(datos['Estructuras'][i]) if datos['Estructuras'][i] in DICT_SL_STRUCTURES else '<none>', 
             'SYMBOLS/STRUCTURES': vacio,       
             'NOTES COLUMN': vacio,             
             'BIOTURBATION TYPE': '<none>', 
             'INTENSITY': '0',
             'PALAEOCURRENT VALUES': vacio, 
             'FACIES': '0', 
             'OTHER1 TEXT': vacio, 
             'OTHER1 SYMBOL': vacio,
             'OTHER2 TEXT': vacio, 
             'OTHER2 SYMBOL': vacio,                      
             'OTHER3 TEXT': vacio, 
             'OTHER3 SYMBOL':vacio}

            ,ignore_index =True)

    sedLogCSV.to_csv("sedLogCSV.csv", index =False,quoting=csv.QUOTE_NONE)
    return sedLogCSV
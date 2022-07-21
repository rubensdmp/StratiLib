import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
from .defaults import *
from .sedlogdef import *
from .sedlogfunc import *


#---------------------------------------------- SHOW LITHO -----------------------------------------------

#Función para plotear las litologías como leyenda
def show_litho(**kwargs):
    '''
    kwargs:
        sedlog = True: show only SedLog 3.1 lithologys
        lang = {'sp','es'} : language sp:spanish, es:english
        df = pandas dataframe from read_litho or read_sedlog
        rows = number of rows to plot lithologys
        cols = number of cols to plot lithologys
        tit = title
        keys = True: show lithology keys
        save_fig = name of file to be saved
    '''
    lang = 'es'
    keys, sedlog, save = False, False, False
    list_keys = LITHOLOGIES.keys()
    keys_tit = ''
    rows = 7
    cols = 5
    sizecols = 3
    sizerows = 2.2 
    add_tit = ''
    tit = 'Lithologies'
    
    for key, value in kwargs.items():
        if (key == 'lang'):    
            lang = value
        if (key == 'df'):    
            df = value
            list_keys = df['LITH1'].unique().tolist()
            rows = len(list_keys)
            cols = 1
        if (key == 'sedlog'):
            if (value =='True'):    
                sedlog = True
                rows = 5
                add_tit = ' SedLog '
                list_keys = [key for key in LITHOLOGIES.keys() if LITHOLOGIES[key]['sedlog'] == sedlog]
        if (key == 'cols'):
            cols = value
            rows = int(np.ceil(len(list_keys)/cols))
        if (key == 'rows'):
            rows = value
            cols = int(np.ceil(len(list_keys)/rows))
        if (key == 'tit'):
            tit = value
        if (key == 'keys'):
            keys = value
        if (key == 'save_fig'):
            save = True 
            name = value
            
    y = [0, 1]
    x = [1, 1]

    fig, axes = plt.subplots(ncols=cols,nrows=rows, sharex=True, sharey=True,
                             figsize=(sizecols*cols,sizerows*rows), subplot_kw={'xticks': [], 'yticks': []})

    for ax, key in zip(axes.flat, list_keys):
        ax.plot(x, y)
        ax.fill_betweenx(y, 0, 1, facecolor=LITHOLOGIES[key]['color'], hatch=LITHOLOGIES[key]['hatch'])
        ax.set_xlim(0, 0.1)
        ax.set_ylim(0, 1)        
        if key == 99999:
            ax.plot([0,0.1], [0,1], color="black", zorder =10, lw=1)    
            ax.plot([0,0.1], [1,0], color="black", zorder =10, lw=1)    
        
        if keys:
            keys_tit = ' (' + DICT_LITHO_RV.get(key) + ')'
            
        if lang == 'sp':
            ax.set_title(str(LITHOLOGIES[key]['sp'])+keys_tit)
            fig.suptitle(tit + add_tit, y=1, ha='center', fontsize=22)
        else:
            ax.set_title(str(LITHOLOGIES[key]['lith'])+keys_tit)
            fig.suptitle(add_tit + tit, y=1, ha='center', fontsize=22)
            
    plt.tight_layout()

    if save:
        plt.savefig(name + '.png') 
    
    plt.show()




#---------------------------------------------- READ LITHO -----------------------------------------------


def read_litho(name, **kwargs):
    '''
    **Kwargs:
        sand_colors = show diferent colors for diferent grain size (see show_litho()). Default False
        
        RETURN: dataframe        
    '''
        
    sand_colors = 'False'
    dfLito = pd.read_excel(name)
    
    columns = dfLito.columns
    #Completo columnas que faltan
    #dfLito['COLNAME'] = '' if 'COLNAME' not in columns else dfLito['COLNAME'] 
    
    dfLito['LITHOLOGY'][dfLito['LITHOLOGY'].isna()==True] = '-'
    
    dfLito['FM'] = '' if 'FM' not in columns else dfLito['FM'] 
    dfLito['BASE'] = 0 if 'BASE' not in columns else dfLito['BASE'] 
    dfLito['THICKNESS'] = None if 'THICKNESS' not in columns else dfLito['THICKNESS'] 
    dfLito['DESC'] = '' if 'DESC' not in columns else dfLito['DESC'] 
    dfLito['GRAINSZ'] = '' if 'GRAINSZ' not in columns else dfLito['GRAINSZ']
    dfLito['GRAINB'] = dfLito['GRAINSZ'].map(DICT_GRAIN) if 'GRAINB' not in columns else dfLito['GRAINB'].map(DICT_GRAIN)
    dfLito['GRAINB'].fillna(1, inplace=True)
    dfLito['GRAINT'] = dfLito['GRAINB'] if 'GRAINT' not in columns else dfLito['GRAINT'].map(DICT_GRAIN)
    dfLito['GRAINT'].fillna(1, inplace=True)
    dfLito['CONTACT'] = '' if 'CONTACT' not in columns else dfLito['CONTACT'] 
    dfLito['LITH1%'] = 1 if 'LITHOLOGY_1_%' not in columns else dfLito['LITHOLOGY_1_%'] 
    dfLito['LITH2'] = '' if 'LITHOLOGY_2' not in columns else dfLito['LITHOLOGY_2'] 
    dfLito['LITH2%'] = 0 if 'LITHOLOGY_2_%' not in columns else dfLito['LITHOLOGY_2_%'] 
    dfLito['LITH3'] = '' if 'LITHOLOGY_3' not in columns else dfLito['LITHOLOGY_3'] 
    dfLito['LITH3%'] = 0 if 'LITHOLOGY_3_%' not in columns else dfLito['LITHOLOGY_3'] 
    dfLito['STRUCTURES'] = np.nan if 'STRUCTURES' not in columns else dfLito['STRUCTURES'] 
    dfLito['FOSSILS'] = '' if 'FOSSILS' not in columns else dfLito['FOSSILS'] 
    
    tope = 0
    base = 0
    por_tope = dfLito['THICKNESS'].isnull().sum() == len(dfLito)
    for i in range(len(dfLito)):
        if por_tope:            
            base= dfLito.loc[i+1,'TOP'] if i < len(dfLito)-1 else dfLito.loc[i,'TOP'] + 99
            dfLito.loc[i,'BASE'] = base
            dfLito.loc[i,'THICKNESS'] = base-dfLito.loc[i,'TOP']
        else:            
            base += dfLito.loc[i,'THICKNESS']
            dfLito.loc[i,'TOP'] = tope  
            dfLito.loc[i,'BASE'] = base
            tope += dfLito.loc[i,'THICKNESS']

    #Cargo diccionario de litologias
    dfLito['LITH1'] = dfLito['LITHOLOGY'].str.lower().map(DICT_LITHO)
    
    #Cargo porcentaje de litologías
    if 'LITHOLOGY_1_%' in columns:
        dfLito['LITH1%'] = dfLito['LITHOLOGY_1_%']/100 
        dfLito['LITH1%'].fillna(1, inplace=True)
    
    if 'LITHOLOGY_2' in columns:
        dfLito['LITH2'] = dfLito['LITHOLOGY_2'].map(DICT_LITHO)
        dfLito['LITH2%'] = dfLito['LITHOLOGY_2_%']/100 
        dfLito['LITH2%'].fillna(0, inplace=True)
    
    if 'LITHOLOGY_3' in columns:
        dfLito['LITH3'] = dfLito['LITHOLOGY_3'].map(DICT_LITHO)
        dfLito['LITH3%'] = dfLito['LITHOLOGY_3_%']/100 
        dfLito['LITH3%'].fillna(0, inplace=True)
    
    
    for key, value in kwargs.items():
        if (key == 'sand_colors'):
            if (value == 'True'):
                dfLito.loc[dfLito['LITHOLOGY']=='S','LITHOLOGY'] = dfLito['LITHOLOGY'] + dfLito['GRAINSZ']
                dfLito['LITH1'] = dfLito['LITHOLOGY'].map(DICT_LITHO)
            
    dfLito['DESC'].fillna('', inplace=True)
               
    return dfLito




#---------------------------------------------- PLOT LITHO -----------------------------------------------

def plot_litho(dfLito, **kwargs):
    width, length = 4, 4
    top = dfLito['TOP'].min()
    base = dfLito['BASE'].max()
        
    suptit = ''
    show_des, struct_out, fossil_out = False,False,False
    save = False
    sub_plots, pos = 1,1
            
    for key, value in kwargs.items():
        if (key == 'show_des'):
            show_des = value
            sub_plots += 1
        if (key == 'width'):
            width = value
        if (key == 'length'):
            length = value
        if (key == 'top'):
            top = value
        if (key == 'base'):
            base = value
        if (key == 'suptit'):
            suptit = value
        if (key == 'struct_out'):
            struct_out = value
            sub_plots += 1
        if (key == 'fossil_out'):
            fossil_out = value
            sub_plots += 1
        if (key == 'save_fig'):
            save = True 
            name = value

    fig = plt.subplots(figsize=(width*sub_plots,length*4))
    
    if show_des:
        axD = sub_plot_des(dfLito, sub_plots, top, base)
    if struct_out:
        axS = sub_plot_struct(dfLito, sub_plots, 1, top, base, **kwargs)
    if fossil_out:
        axF = sub_plot_fossils(dfLito, sub_plots, pos, top, base, **kwargs)

    
    if suptit != '':
        plt.suptitle(suptit, y=1, ha='center', fontsize=22)
    
    axL = sub_plot_litho(dfLito, sub_plots, 0, top, base, **kwargs)

    plt.subplots_adjust(wspace=0)
    
    if save:
        plt.savefig(name + '.png')    
    
    plt.show()


    
    
#---------------------------------------------- SUB PLOT LITHO -----------------------------------------------

#Función para el ploteo de perfíl litológico
'''
Tenemos que sumar:
    -suavizar curva
    -
'''

#Parámetros:
    #tope, base,
    
def sub_plot_litho(dfLito, sub_plots, plot_pos, topep, basep, **kwargs):
    #Variables **kwargs por defecto:
    width, length = 4, 4
    show_fm, tick_unit = False, False
    show_fossils,show_structs = False, False 
    show_era = False
    show_des = False
    only_first_lith = False
    color_fill, show_gr = True, True
    fm_rot = 90
    fm_size = 20
    x_plot = 0
    step= ((basep-topep)/8)
    title ='       Lithology\n'
    none_length = 1
    
    axL = plt.subplot2grid((1,sub_plots), (0,plot_pos), rowspan=1, colspan = 1)        

    suav = False
    
    #list of NULL lithology
    null_list = list(zip(dfLito['TOP'][dfLito['LITH1']==99999].unique().tolist(),
                         dfLito['BASE'][dfLito['LITH1']==99999].unique().tolist()))
    
            
    #list of Contacts
    contact_list = list(zip(dfLito['BASE'][dfLito['CONTACT'].isnull()==False].tolist(),
                            dfLito['CONTACT'][dfLito['CONTACT'].isnull()==False].tolist(),
                            dfLito['GRAINB'][dfLito['CONTACT'].isnull()==False].tolist()))
    
    #list of Structures
    struct_list = []
    for idx in dfLito[dfLito['STRUCTURES'].isnull()==False].index.tolist():
        for s in dfLito['STRUCTURES'][idx].split(','):
            struct_list.append((dfLito['TOP'][idx], DICT_STRUCT[s], dfLito['BASE'][idx]))  
    
    fossil_list = []
    for idx in dfLito[dfLito['FOSSILS'].isnull()==False].index.tolist():
        for s in dfLito['FOSSILS'][idx].split(','):
            fossil_list.append((dfLito['TOP'][idx], DICT_FOSSILS[s], dfLito['BASE'][idx]))  
    
    
    #struct_list + list(zip(dfLito['TOP'][dfLito['FOSSILS'].isnull()==False].tolist(),
    #                        dfLito['FOSSILS'][dfLito['FOSSILS'].isnull()==False].map(DICT_FOSSILS).tolist(),
    #                        dfLito['BASE'][dfLito['FOSSILS'].isnull()==False].tolist()))
    
    
    #Duplico el valor de base para que el ploteo sea del espesor completo
    dfLito_aux = dfLito.copy()
    dfLito_aux['BASE'] = dfLito['TOP']
    dfLito_aux['GRAINB'] = dfLito['GRAINT']
    dfLito = pd.concat([dfLito_aux,dfLito])
    dfLito.sort_values(by=['TOP', 'BASE'], inplace =True)
    
    #reviso los Kwargs
    for key, value in kwargs.items():
        if (key == 'show_fm') & (value == 'True'):
            show_fm = True
            Fms = dfLito[['FM', 'TOP', 'CONTACT']].groupby(['FM']).first()
            Fms['BASE']= dfLito[['FM', 'BASE']].groupby(['FM']).last()
            Fms['CONTACT']= dfLito[['FM', 'CONTACT']].groupby(['FM']).last()
            Fms.reset_index(inplace=True)            
            x_plot +=0.5
            title = 'Fm           Litología\n'
        if (key == 'show_gr') & (value == 'False'):
            show_gr = False
            dfLito['GRAINB'] = 1
        if (key == 'color_fill') & (value == 'False'):
            color_fill = False
        if (key == 'show_fossils') & (value == 'True'):
            show_fossils = True
        if (key == 'show_structs') & (value == 'True'):
            show_structs = True
        if (key == 'fm_rot'):
            fm_rot = value
        if (key == 'fm_size'):
            fm_size = value
        if (key == 'suavizar') & (value == 'True'):
            suav = True
        if (key == 'width'):
            width = value
        if (key == 'length'):
            length = value
        if (key == 'ticks'):
            step = value
        if (key == 'tick_unit') & (value == 'True'):
            tick_unit = True
        if (key == 'title'):
            title = value
        if (key == 'none_length'):
            none_length = value
        if (key == 'only_first_lith'):
            only_first_lith = value
            
               
    dfLito['GRAINB'][dfLito['LITH1']==99999] = none_length
    dfLito['GRAINT'][dfLito['LITH1']==99999] = none_length
        
    escala = (basep - topep)/(length*60)
        
       
    # Lithology track
    #xL.plot(dfLito["LITHOLOGY"], dfLito['BASE'], color = "black", linewidth = 0.5)
    axL.set_title(title, fontsize = 20, linespacing = 2.0, ha = 'center', x=0.38)
    axL.set_xlim(0, x_plot+1)
    axL.xaxis.label.set_color("black")
    axL.tick_params(axis='x', colors="black")
    axL.spines["top"].set_edgecolor("black")
    axL.vlines(x=x_plot, ymin=topep, ymax=basep, colors='black', ls='-', lw=1, label='vline_single - full height',alpha = 1, zorder = 5)
    axL.hlines(y=topep, xmin=0, xmax=x_plot+1, colors='black', ls='-', lw=1, label='vline_single - full height',alpha = 1, zorder = 5)
    
    #Ploteo de granulometrías
    if show_gr:
        axL.vlines(x=x_plot+0.60, ymin=topep, ymax=basep, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3, zorder = 5)
        axL.vlines(x=x_plot+0.65, ymin=topep, ymax=basep, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3, zorder = 5)
        axL.vlines(x=x_plot+0.70, ymin=topep, ymax=basep, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3,zorder = 5)
        axL.vlines(x=x_plot+0.75, ymin=topep, ymax=basep, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3,zorder = 5)
        axL.vlines(x=x_plot+0.80, ymin=topep, ymax=basep, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3,zorder = 5)
        axL.vlines(x=x_plot+0.85, ymin=topep, ymax=basep, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3,zorder = 5)
        axL.vlines(x=x_plot+0.90, ymin=topep, ymax=basep, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3,zorder = 5)
        axL.vlines(x=x_plot+0.95, ymin=topep, ymax=basep, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3,zorder = 5)
        if suav:
            dfLito['GRAINB'][(dfLito['GRAINB']<1)] =dfLito['GRAINB'].apply(lambda x: x+np.random.random_sample()*0.03)
            
        axL.plot(x_plot+dfLito['GRAINB'],dfLito['BASE'], color="black", zorder =10, lw=0.8)
        
        axL.set_xticks([0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1.0])
        bbox_props = dict(boxstyle="Round, pad=0.8", fc="w", ec="0.5", alpha=0.0)
        axL.text(0.53, topep-((basep - topep)*0.015), '    s      f      c     g     b', 
            ha="left", va="bottom",linespacing = 1.0, size=10, multialignment='left',
            bbox=bbox_props, zorder=1,rotation=0)
        axL.text(0.53, topep-((basep - topep)*0.003), 'cl    vf     m    vc    p  ', 
            ha="left", va="bottom",linespacing = 1.0, size=10, multialignment='left',
            bbox=bbox_props, zorder=1,rotation=0)
        
    
    base_aux = 0
    #PLOTEO ESTRUCTURAS
    if show_structs:
        for i in range(len(struct_list)):
            pos = struct_list[i][0] + (struct_list[i][2] - struct_list[i][0])/2
            if struct_list[i][0] != base_aux:
                x0 = 0.15
            else:
                x0 =+ 0.40
            axL.imshow(struct_list[i][1], extent=[x_plot+x0,x_plot+x0+(0.50*(3/width)),pos+(7*escala),pos-(7*escala)], aspect='auto', zorder=20)
            #axL.imshow(sl.img_amo, extent=[x_plot+0.2,x_plot+0.2+(0.25*(4/width)),pos2,(pos2-(pos2/10)*escala/15)], aspect='auto', zorder=20)
            base_aux = struct_list[i][0]
    
    #PLOTEO FÓSILES
    if show_fossils:
        for i in range(len(fossil_list)):
            pos = fossil_list[i][0] + (fossil_list[i][2] - fossil_list[i][0])/2
            axL.imshow(fossil_list[i][1], extent=[x_plot+0.15,x_plot+0.15+(0.50*(4/width)),pos+(7*escala),pos-(7*escala)], aspect='auto', zorder=20)
            #axL.imshow(sl.img_amo, extent=[x_plot+0.2,x_plot+0.2+(0.25*(4/width)),pos2,(pos2-(pos2/10)*escala/15)], aspect='auto', zorder=20)

    
    #PLOTEAMOS LAS FORMACIONES
    if show_fm:
        bbox_props = dict(boxstyle="Round, pad=0.8", fc="w", ec="0.5", alpha=0.0)
        for i in range(len(Fms)):
            if (Fms.iloc[i,3] > topep) & (Fms.iloc[i,1] < basep):
                x_tope = Fms.iloc[i,1] if Fms.iloc[i,1] > topep else topep
                x_base = Fms.iloc[i,3] if Fms.iloc[i,3] < basep else basep                
                axL.text(0.25, (x_tope+x_base)/2, Fms.iloc[i,0], 
                    ha="center", va="center", size=fm_size,
                    bbox=bbox_props, zorder=1,rotation=fm_rot)
            #Ploteamos contacto entre formaciones
            if Fms.iloc[i,2]=='S':
                axL.hlines(y=Fms.iloc[i,3], xmin=0, xmax=x_plot, colors='black', ls='-', lw=3, zorder = 5)
            if Fms.iloc[i,2]=='E':
                x = np.arange(0,x_plot,0.001)   # start,stop,step
                y = np.sin(50*x)
                axL.plot(x,Fms.iloc[i,3]+escala*y, color="black", zorder =10, lw=3)
            if Fms.iloc[i,2]=='G':
                axL.hlines(y=Fms.iloc[i,3],  xmin=0, xmax=x_plot, colors='black', ls='--', lw=3, zorder = 5)


    
    #COLOREAMOS Y RELLENAMOS UNIDADES
    for key in LITHOLOGIES.keys(): 
        color = LITHOLOGIES[key]['color'] if color_fill else '#FF000000'
        hatch = LITHOLOGIES[key]['hatch']
        if only_first_lith:
            axL.fill_betweenx(dfLito['BASE'], x_plot, x_plot+(dfLito['GRAINB'] if show_gr else 1), interpolate = 'True'
                          , where=(dfLito['LITH1']==key),
                         facecolor=color, hatch=hatch)    
        else:
            axL.fill_betweenx(dfLito['BASE'], x_plot, x_plot+(dfLito['GRAINB'] if show_gr else 1)*dfLito['LITH1%'], interpolate = 'True'
                              , where=(dfLito['LITH1']==key),
                             facecolor=color, hatch=hatch)
            axL.fill_betweenx(dfLito['BASE'], x_plot+dfLito['LITH1%'], x_plot+dfLito['LITH1%']+dfLito['LITH2%'], interpolate = 'True'
                              , where=(dfLito['LITH2']==key),
                             facecolor=color, hatch=hatch)
            axL.fill_betweenx(dfLito['BASE'], x_plot+dfLito['LITH1%']+dfLito['LITH2%'], x_plot+dfLito['LITH1%']+dfLito['LITH2%']+dfLito['LITH3%'], interpolate = 'True'
                              , where=(dfLito['LITH3']==key),
                             facecolor=color, hatch=hatch)
        
        
    #ploteo para zonas cubiertas o sin litología descrita X
    for i in range(len(null_list)):
        axL.plot([x_plot, x_plot+none_length], [topep if null_list[i][0] < topep else null_list[i][0],
                                      basep if null_list[i][1] > basep else null_list[i][1]],
                                      color="black", zorder =10, lw=1)    
        axL.plot([x_plot, x_plot+none_length], [basep if null_list[i][1] > basep else null_list[i][1],
                                      topep if null_list[i][0] < topep else null_list[i][0]],                                      
                                      color="black", zorder =10, lw=1)    

        
    #Ploteo de contactos
    yticks = np.append([topep, basep],np.arange(0,basep,step)) # start,stop,step
    for i in range(len(contact_list)):    
        yticks = np.append(contact_list[i][0],yticks)
        if contact_list[i][1]=='S':
            axL.hlines(y=contact_list[i][0], xmin=x_plot, xmax=x_plot+contact_list[i][2], colors='black', ls='-', lw=3, zorder = 5)

        if contact_list[i][1]=='E':
            x = np.arange(x_plot,x_plot+contact_list[i][2],0.001)   # start,stop,step
            y = np.sin(50*x)
            axL.plot(x,contact_list[i][0]+escala*y, color="black", zorder =10, lw=3)

        if contact_list[i][1]=='G':
            axL.hlines(y=contact_list[i][0], xmin=x_plot, xmax=x_plot+contact_list[i][2], colors='black', ls='--', lw=3, zorder = 5)
    
    #mostramos ticks de las unidades
    if tick_unit:
        axL.set_yticks(yticks)
        
    axL.set_ylim(basep, topep)
    axL.grid(which='major', color='lightgrey', linestyle='-')
    axL.xaxis.set_ticks_position("top")
    axL.xaxis.set_label_position("top")
    #axL.spines["top"].set_position(("axes", 1.02))
    plt.setp(axL.get_xticklabels(), visible = False)
    axL.grid(False)

    return axL




#---------------------------------------------- SUB PLOT STRUCT -----------------------------------------------

def sub_plot_struct(df, sub_plots, pos, tope, basee, **kwargs):
    axS = plt.subplot2grid((1,sub_plots), (0,pos), rowspan=1, colspan = 1)        
    width, length = 4, 4
    step= ((basee-tope)/8)
    
    df_str = df[['TOP', 'BASE', 'STRUCTURES', 'FOSSILS']]
    
    #list of Structures
    struct_list = []
    for idx in df_str[df_str['STRUCTURES'].isnull()==False].index.tolist():
        for s in df_str['STRUCTURES'][idx].split(','):
            struct_list.append((df_str['TOP'][idx], DICT_STRUCT[s], df_str['BASE'][idx]))  
    
    fossil_list = []
    for idx in df_str[df_str['FOSSILS'].isnull()==False].index.tolist():
        for s in df_str['FOSSILS'][idx].split(','):
            fossil_list.append((df_str['TOP'][idx], DICT_FOSSILS[s], df_str['BASE'][idx]))  
    
    #list of Contacts
    contact_list = list(zip(df['BASE'].tolist(),
                            df['CONTACT'].tolist(),
                            df['GRAINB'].tolist()))
    
    
    #reviso los Kwargs
    for key, value in kwargs.items():
        if (key == 'length'):
            length = value
        
    escala = (basee - tope)/(length*60)
    
    
        
    
    axS.set_xlim(0, 1)
    axS.hlines(y=tope, xmin=0, xmax=1, colors='black', ls='-', lw=1, label='vline_single - full height',alpha = 1, zorder = 5)
    axS.set_title('Structures\n', fontsize = 20, linespacing = -0.01)

            
    #PLOTEO ESTRUCTURAS
    base_aux = 0
    for i in range(len(struct_list)):
        pos = struct_list[i][0] + (struct_list[i][2] - struct_list[i][0])/2
        if struct_list[i][0] != base_aux:
            x0 = 0.05
        else:
            x0 =+ 0.30
        axS.imshow(struct_list[i][1], extent=[x0,x0+(0.50*(2/width)),pos+(5*escala),pos-(5*escala)], aspect='auto', zorder=20)
        base_aux = struct_list[i][0]
        
    #Ploteo de contactos
    yticks = np.append([tope, basee],np.arange(0,basee,step)) # start,stop,step
    for i in range(len(contact_list)):    
        yticks = np.append(contact_list[i][0],yticks)
        if contact_list[i][1]=='S':
            axS.hlines(y=contact_list[i][0], xmin=0, xmax=1, colors='black', ls='-', lw=2, zorder = 5, alpha = 0.5)

        if contact_list[i][1]=='E':
            x = np.arange(0,1,0.001)   # start,stop,step
            y = np.sin(50*x)
            axS.plot(x,contact_list[i][0]+escala*y, color="black", zorder =10, lw=2, alpha = 0.5)

        if contact_list[i][1]=='G':
            axS.hlines(y=contact_list[i][0], xmin=0, xmax=1, colors='black', ls='--', lw=2, zorder = 5, alpha = 0.5)
        
        if pd.isna(contact_list[i][1]):
            axS.hlines(y=contact_list[i][0], xmin=0, xmax=1, colors='black', ls='-', lw=1, zorder = 5, alpha = 0.5)
    
    
            
    axS.set_ylim(basee, tope)
    axS.grid(which='major', color='lightgrey', linestyle='-')
    axS.axes.get_xaxis().set_visible(False)
    plt.setp(axS.get_yticklabels(), visible = False)
    axS.tick_params(axis='x', colors="black")
    axS.grid(False)

    return axS






#---------------------------------------------- SUB PLOT DES -----------------------------------------------


def sub_plot_des(df, sub_plots, tope, basee):
    axD = plt.subplot2grid((1,sub_plots), (0,sub_plots-1), rowspan=1, colspan = 1)        
    
    axD.set_xlim(0, 1)
    axD.hlines(y=tope, xmin=0, xmax=1, colors='black', ls='-', lw=1, label='vline_single - full height',alpha = 1, zorder = 5)
    axD.set_title('Description\n', fontsize = 20, linespacing = -0.01)

    df_des = df[['TOP', 'BASE', 'DESC']]

    #Ploteamos las descripciones
    for i in range(len(df_des)):
        if (df_des.iloc[i,0] > tope) & (df_des.iloc[i,1] < basee):
            #axD.hlines(y=df_des.iloc[i,1], xmin=0, xmax=1, colors='black', ls='-', lw=1, label='vline_single - full height',alpha = 1, zorder = 5)
            bbox_props = dict(boxstyle="Round, pad=0.8", fc="w", ec="0.5", alpha=0.0)
            axD.text(0.01, df_des.iloc[i,1]-((df_des.iloc[i,1]-df_des.iloc[i,0])/2.8), df_des.iloc[i,2], 
                ha="left", va="bottom",linespacing = 1.0, size=10, multialignment='left',
                bbox=bbox_props, zorder=1,rotation=0)

    
    #list of Contacts
    contact_list = list(zip(df['BASE'].tolist(),
                            df['CONTACT'].tolist(),
                            df['GRAINB'].tolist()))
    width, length = 4, 4
    step= ((basee-tope)/8)        
    escala = (basee - tope)/(length*60)
    #Ploteo de contactos
    yticks = np.append([tope, basee],np.arange(0,basee,step)) # start,stop,step
    for i in range(len(contact_list)):    
        yticks = np.append(contact_list[i][0],yticks)
        if contact_list[i][1]=='S':
            axD.hlines(y=contact_list[i][0], xmin=0, xmax=1, colors='black', ls='-', lw=2, zorder = 5, alpha = 0.5)

        if contact_list[i][1]=='E':
            x = np.arange(0,1,0.001)   # start,stop,step
            y = np.sin(50*x)
            axD.plot(x,contact_list[i][0]+escala*y, color="black", zorder =10, lw=2, alpha = 0.5)

        if contact_list[i][1]=='G':
            axD.hlines(y=contact_list[i][0], xmin=0, xmax=1, colors='black', ls='--', lw=2, zorder = 5, alpha = 0.5)
        
        if pd.isna(contact_list[i][1]):
            axD.hlines(y=contact_list[i][0], xmin=0, xmax=1, colors='black', ls='-', lw=1, zorder = 5, alpha = 0.5)            
    
    
    
    
            
    axD.set_ylim(basee, tope)
    axD.grid(which='major', color='lightgrey', linestyle='-')
    axD.axes.get_xaxis().set_visible(False)
    plt.setp(axD.get_yticklabels(), visible = False)
    axD.tick_params(axis='x', colors="black")
    axD.grid(False)

    return axD







#---------------------------------------------- PLOT STRCUTS -----------------------------------------------

#Dictionary for Sedimentary structures in SYMBOLS IN BED' y 'SYMBOLS/STRUCTURES'
DICT_PLT_STRUCTURES = {
'r':'''Current ripple
cross-lamination''',
'w':'''Wave ripple
cross-lamination''',
'p':'''Planar cross
bedding''',
'cr':'''Trough cross 
bedding''',
'h':'''Horizontal planar 
lamination''',
'hm':'''Hummocky cross
stratification''',
'sw':'''Swaley cross 
srtatification''',
'mc':'Mudcracks',
'sc':'''Synaeresis 
cracks''',
'cl':'''Convolute 
lamination''',
'lc':'Load casts',
'ws':'Water structures',
'hb':'''Herring-bones 
cross bedding''',
'nac':'''Nodules and 
concretions''',
'int':'Intraclasts',
'mcl':'Mudclasts',
'flm':'Flute marks',
'gro':'Groove marks',
'scr':'Scours'}

#Dictionary for Fossils in SYMBOLS IN BED' y 'SYMBOLS/STRUCTURES'
DICT_PLT_FOSSILS = {
'fsh':'Shells',
'fbi':'Bivalves',
'fga':'Gastropods',
'fce':'Cephalopods',
'fbr':'Brachiopods',
'fec':'Echinoids',
'fcr':'Crinoids',
'fsco':'Solitary corals',
'fcco':'Colonial corals',
'ffo':'Foraminifera',
'fal':'Algae',
'fbry':'Bryzoa',
'fst':'Stromatolites',
'fve':'Vertebrates',
'fplm':'Plant material',
'fro':'Roots',
'flo':'Logs',
'ftrs':'Tree stumps',
'fos':'Ostracods',
'fra':'Radiolaria',
'fsp':'Sponges',
'fbiol':'''Minor 
bioturbation''',
'fbiom':'''Moderate 
bioturbation''',
'fbioh':'''Intense 
bioturbation''',
'ftrk':'Tracks',
'ftra':'Trails',
'fvbu':'Vertical burrows',
'fhbu':'''Horizontal 
burrows'''}




def plot_structs(**kwargs):
    '''
    kwargs:
        df = pandas dataframe from read_litho or read_sedlog
        keys = True: show lithology keys
        save_fig = name of file to be saved
    '''
    
    plot = 'both'
    from_df, keys = False, False
    save = False
    
    for key, value in kwargs.items():
        if (key == 'plot'):    
            plot = value
        if (key == 'df'):
            from_df = True 
            df = value
        if (key == 'save_fig'):
            save = True 
            name = value
        if (key == 'keys'):
            keys = True 

   
    bbox_props = dict(boxstyle="Round, pad=0.8", fc="w", ec="0.5", alpha=0.0)

    list_struct = set()
    list_fossils = set()

    if plot =='structures' or plot =='both':
        if from_df:
            for e in df['STRUCTURES'][df['STRUCTURES'].isnull() ==False].to_list():
                for k in e.split(','):
                    list_struct.add(k)
        else:
            list_struct = list(DICT_STRUCT.keys())
            
    if plot =='fossils' or plot =='both':
        if from_df:
            for e in df['FOSSILS'][df['FOSSILS'].isnull() ==False].to_list():
                for k in e.split(','):
                    list_fossils.add(k)    
        else:
            list_fossils = list(DICT_FOSSILS.keys())
            
            
    s_rows = -(-len(list_struct)//6) # ceil
    f_rows = -(-len(list_fossils)//6) # ceil
    maxstruct = max(len(list_struct), len(list_struct))
    
    fig = plt.subplots(figsize=(15 if maxstruct > 5 else maxstruct * 2.5,(s_rows*(2+0.2))+ (f_rows*(2+0.2))))
    ax = plt.subplot2grid((1,1), (0,0), rowspan=1, colspan = 1) 
    
    y = (s_rows + f_rows)*12 + (10 if plot == 'both' else 5)
    ax.set_ylim(0, y)
    xmax = 100 if maxstruct > 5 else maxstruct * 16.66
    ax.set_xlim(0, xmax)    
    
  
    if plot == 'structures' or plot == 'both':
        ax.text(xmax/2, y-1, 'STRUCTURES',  weight='bold',
            ha="center", va="top",linespacing = 1.2, size=25, multialignment='left',
            bbox=bbox_props, zorder=1,rotation=0,wrap=True)             
        #ax.hlines(y=y-4, xmin=xmax/2.55, xmax=xmax/1.65, colors='black', ls='-.', lw=1, zorder = 5)
        
        y -=12

        x=4           
        for k in list_struct:
            ax.imshow(DICT_STRUCT.get(k), extent=[x,x+10,y,y+7], aspect='auto', zorder=20)
            ax.text(x+5, y,  DICT_PLT_STRUCTURES.get(k) + ' (' + k + ')' if keys else DICT_PLT_STRUCTURES.get(k), 
                ha="center", va="top",linespacing = 1.2, size=12, multialignment='left',
                bbox=bbox_props, zorder=1,rotation=0,wrap=True)             
            x = (x + 16) if x < 83 else 3
            y = (y - 12) if x == 3 else y

        y -=5
    
    if plot == 'both':
        ax.hlines(y=y, xmin=2, xmax=xmax-2, colors='black', ls='--', lw=1, zorder = 5)
               
    if plot == 'fossils' or plot == 'both':
        ax.text(xmax/2, y-1, 'FOSSILS',   weight='bold',
            ha="center", va="top",linespacing = 1.2, size=25, multialignment='left',
            bbox=bbox_props, zorder=1,rotation=0,wrap=True)             
        #ax.hlines(y=y-4, xmin=43, xmax=57, colors='black', ls='-.', lw=1, zorder = 5)

        y -=12

        x=4
        for k in list_fossils:
            ax.imshow(DICT_FOSSILS.get(k), extent=[x,x+10,y,y+7], aspect='auto', zorder=20)
            ax.text(x+5, y, DICT_PLT_FOSSILS.get(k) + ' (' + k + ')' if keys else DICT_PLT_FOSSILS.get(k), 
                ha="center", va="top",linespacing = 1.2, size=12, multialignment='left',
                bbox=bbox_props, zorder=1,rotation=0,wrap=True)             
            x = (x + 16) if x < 83 else 3
            y = (y - 12) if x == 3 else y
        

    
    ax.grid(which='major', color='lightgrey', linestyle='-')
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    plt.setp(ax.get_yticklabels(), visible = False)
    ax.tick_params(axis='x', colors="black")
    ax.grid(False)
    
    if save:
        plt.savefig(name + '.png')
    
    plt.show()
    








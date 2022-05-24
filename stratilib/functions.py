import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
from .defaults import *





def read_lito(name, **kwargs):
    sand_colors = 'False'
    dfLito = pd.read_excel(name)
    
    tope = 0
    base = 0
    por_tope = dfLito['Espesor'].isnull().sum() ==len(dfLito)
    
    for i in range(len(dfLito)):
        if por_tope:            
            base= dfLito.loc[i+1,'Tope'] if i < len(dfLito)-1 else dfLito.loc[i,'Tope'] + 99
            dfLito.loc[i,'Base'] = base
            dfLito.loc[i,'Espesor'] = base-dfLito.loc[i,'Tope']
        else:            
            base += dfLito.loc[i,'Espesor']
            dfLito.loc[i,'Tope'] = tope  
            dfLito.loc[i,'Base'] = base
            tope += dfLito.loc[i,'Espesor']

    for key, value in kwargs.items():
        if (key == 'sand_colors'):
            if (value == 'True'):
                dfLito.loc[dfLito['Litología']=='S','Litología'] = dfLito['Litología'] + dfLito['Granulometría']
                dfLito['Litología'] = dfLito['Litología'].map(DICT_LITO)
            else:
                dfLito['Litología'] = dfLito['Litología'].map(DICT_LITO)
        
    dfLito['Gran'] = dfLito['Granulometría'].map(DICT_GRAN)
    dfLito['Gran'].fillna(1, inplace=True)
    dfLito['Descripción'].fillna('', inplace=True)
               
    return dfLito






#Parámetros:
    #tope, base,
    
def sub_plot_lito(dfLito, tope, base, **kwargs):
    
    #Variables **kwargs por defecto:
    show_fm = False
    show_gr = False
    show_fossils = False
    show_era = False
    color_fill = False
    fm_rot = 90
    fm_size = 20
    x_plot = 0
    escala = (base - tope)/2500
    axL = plt.subplot2grid((1,1), (0,0), rowspan=1, colspan = 1)    
       
    for key, value in kwargs.items():
        if (key == 'show_fm') & (value == 'True'):
            show_fm = True
            Fms = dfLito[['Fm', 'Tope']].groupby(['Fm']).first()
            Fms['Base']= dfLito[['Fm', 'Base']].groupby(['Fm']).last()
            Fms.reset_index(inplace=True)
            x_plot +=0.5
        if (key == 'show_gr') & (value == 'True'):
            show_gr = True
        if (key == 'color_fill') & (value == 'True'):
            color_fill = True
        if (key == 'show_fossils') & (value == 'True'):
            show_fossils = True
        if (key == 'fm_rot'):
            fm_rot = value
        if (key == 'fm_size'):
            fm_size = value
            
       
    # Lithology track
    axL.plot(dfLito["Litología"], dfLito['Base'], color = "black", linewidth = 0.5)
    axL.set_xlabel("Litología")
    axL.set_xlim(0, x_plot+1)
    axL.xaxis.label.set_color("black")
    axL.tick_params(axis='x', colors="black")
    axL.spines["top"].set_edgecolor("black")
    
    
    
    
    #Ploteo de granulometrías
    if show_gr:
        axL.vlines(x=x_plot, ymin=0, ymax=4000, colors='black', ls='-', lw=1, label='vline_single - full height',alpha = 1, zorder = 5)
        axL.vlines(x=x_plot+0.65, ymin=0, ymax=4000, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3, zorder = 5)
        axL.vlines(x=x_plot+0.7, ymin=0, ymax=4000, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3,zorder = 5)
        axL.vlines(x=x_plot+0.75, ymin=0, ymax=4000, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3,zorder = 5)
        axL.vlines(x=x_plot+0.8, ymin=0, ymax=4000, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3,zorder = 5)
        axL.vlines(x=x_plot+0.85, ymin=0, ymax=4000, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3,zorder = 5)
        axL.vlines(x=x_plot+0.9, ymin=0, ymax=4000, colors='#999999', ls='--', lw=1, label='vline_single - full height',alpha = 0.3,zorder = 5)
        axL.plot(x_plot+dfLito['Gran'],dfLito['Base'], color="black", zorder =10, lw=0.8)
    
    pos1 =1100
    pos2 =1300
    if show_fossils:
        axL.imshow(rip, extent=[x_plot+0.15,x_plot+0.45,pos1,(pos1-(pos1/10)*(2*escala))], aspect='auto', zorder=20)
        axL.imshow(rip, extent=[x_plot+0.35,x_plot+0.65,pos1,(pos1-(pos1/10)*(2*escala))], aspect='auto', zorder=20)
        axL.imshow(im, extent=[x_plot+0.2,x_plot+0.45,pos2,(pos2-(pos2/10)*escala)], aspect='auto', zorder=20)

    #Ploteamos las Formaciones
    if show_fm:
        x = np.arange(0,1,0.001)   # start,stop,step
        y = np.sin(50*x)
        bbox_props = dict(boxstyle="Round, pad=0.8", fc="w", ec="0.5", alpha=0.0)
        for i in range(len(Fms)):
            if (Fms.iloc[i,2] > tope) & (Fms.iloc[i,1] < base):
                x_tope = Fms.iloc[i,1] if Fms.iloc[i,1] > tope else tope
                x_base = Fms.iloc[i,2] if Fms.iloc[i,2] < base else base                
                axL.text(0.25, (x_tope+x_base)/2, Fms.iloc[i,0], 
                    ha="center", va="center", size=fm_size,
                    bbox=bbox_props, zorder=1,rotation=fm_rot)
                #axL.hlines(y=Fms.iloc[i,2], xmin=0, xmax=2, colors='black', ls='-', lw=1, label='vline_single - full height',zorder = 5)
                axL.plot(x,Fms.iloc[i,2]+escala*8*y, color="black", zorder =10, lw=1)

                
    #Ploteamos Eras
    if show_era:
        x = np.arange(0,1,0.001)   # start,stop,step
        y = np.sin(50*x)
        bbox_props = dict(boxstyle="Round, pad=0.8", fc="w", ec="0.5", alpha=0.0)
        for i in range(len(Fms)):
            if (Fms.iloc[i,2] > tope) & (Fms.iloc[i,1] < base):
                x_tope = Fms.iloc[i,1] if Fms.iloc[i,1] > tope else tope
                x_base = Fms.iloc[i,2] if Fms.iloc[i,2] < base else base                
                axL.text(0.25, (x_tope+x_base)/2, Fms.iloc[i,0], 
                    ha="center", va="center", size=fm_size,
                    bbox=bbox_props, zorder=1,rotation=fm_rot)
                #axL.hlines(y=Fms.iloc[i,2], xmin=0, xmax=2, colors='black', ls='-', lw=1, label='vline_single - full height',zorder = 5)
                axL.plot(x,Fms.iloc[i,2]+escala*8*y, color="black", zorder =10, lw=1)

                
    
    #Relleno de las Formaciones
    for key in lithologys.keys():
        color = lithologys[key]['color'] if color_fill else '#FF000000'
        hatch = lithologys[key]['hatch']
        axL.fill_betweenx(dfLito['Base'], x_plot, x_plot+(dfLito['Gran'] if show_gr else 2)
                          , where=(dfLito['Litología']==key),
                         facecolor=color, hatch=hatch)
        
       
    return axL




def plot_lito(dfLito, largo, tope, base, **kwargs):
    fig, axL = plt.subplots(figsize=(largo,largo*4))
    
    axL = plt.subplot2grid((1,1), (0,0), rowspan=1, colspan = 1)

    axL = subplotLito(dfLito, tope, base, **kwargs)

    axL.set_ylim(base, tope)
    axL.grid(which='major', color='lightgrey', linestyle='-')
    axL.xaxis.set_ticks_position("top")
    axL.xaxis.set_label_position("top")
    axL.spines["top"].set_position(("axes", 1.02))
    plt.setp(axL.get_xticklabels(), visible = False)
    axL.grid(False)

    plt.show()









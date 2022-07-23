# coding=utf-8

import numpy as np
import pandas as pd
import matplotlib.hatch
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon
import os
import warnings



##CREACIÓN DE HATCH PARA LITOLOGÍAS, TENER EN CUENTA QUE A PARTIR DE LA V 3.8 DE MATPLOTLIB DEJARÁ DE FUNCIONAR
warnings.filterwarnings('ignore')


#---------------------------------------------- HATCH -----------------------------------------------

#polígonos creados para uso como hatch.

hatch_chert1 = Polygon([[0.3, 0.2],[0.5, 0.4], [0.7, 0.2]],
   closed=True, fill=False)

hatch_chert = Polygon([[-0.4, -0.4],[0.0, -0.1], [0.4, -0.4]],
   closed=True, fill=False)

hatch_beccia = Polygon([[-0.35, 0.2],[0.1, 0.4], [0.4, 0.3]],
   closed=True, fill=False)

hatch_granite = Polygon([[0.15, 0.5],[0.15, 0.55],[0.5, 0.55], [0.5, 0.9], [0.55, 0.9], [0.55, 0.55],
                         [0.9, 0.55],[0.9, 0.5], [0.55, 0.5], [0.55, 0.15], [0.5, 0.15], [0.5, 0.5]],
   closed=True, fill=False)

hatch_granite2 = Polygon([[0.0, -0.3],[0.0, 0.0],[0.3, 0.0], [0.0, 0.0], [0.0, 0.3], [0.0, 0.0], [-0.3,0.0],[0.0, 0.0],],
   closed=True, fill=False)

hatch_clay = Polygon([[-0.5, 0.0],[-0.5, 0.1], [0.5, 0.1], [0.5, 0.0]],
   closed=True, fill=False)

hatch_siltstone1 = Polygon([[-0.5, -0.5],[-0.5, -0.4], [0.0, -0.4], [0.0, -0.5]],
   closed=True, fill=False)
hatch_siltstone2 = Polygon([[0.45, -0.45],[0.45, -0.5], [0.5, -0.45], [0.5, -0.5]],
   closed=True, fill=False)

hatch_coarse_ash = Polygon([[-0.3, 0.2],[0.0, -0.3], [0.3, 0.2], [0.3, 0.2], [0.0, -0.3], [-0.3, 0.2]],
   closed=True, fill=False)

hatch_limestone2 = Polygon([[0.0, -1.0],[0.0, 1.0]],
   closed=True, fill=False)

hatch_dolomite = Polygon([[-1.0, -1.0],[1.0, 1.0]],
   closed=True, fill=False)

hatch_limemud = Polygon([[-1.0, 0.0],[-0.2, 0.0]],
   closed=True, fill=False)

hatch_lava = Polygon([[-1.0, 0.0],[-0.2, 0.0]],
   closed=True, fill=False)


#Lista de los hatch para recorrer y cargar en matplotlib
list_c_hatch = [['a',hatch_coarse_ash],
                ['b1',hatch_siltstone1],
                ['b2',hatch_siltstone2],
                ['c',hatch_clay],
                ['d',hatch_dolomite],
                ['e',hatch_chert],
                ['f',hatch_granite2],
                ['g',hatch_beccia],
                ['h',hatch_lava],
                ['i',hatch_granite],
                ['l',hatch_limestone2],                
                ['m',hatch_limemud]]


#función para carga de hatchs
def add_hatch(pol, idh):
    class CustomHatch(matplotlib.hatch.Shapes):
        """
        Custom hatches defined by a path drawn inside [-0.5, 0.5] square.
        Identifier 'c'.
        """
        filled = False
        size = 0.5
        path = pol.get_path()
        
        def __init__(self, hatch, density):
            self.num_rows = (hatch.count(idh)) * density
            self.shape_vertices = self.path.vertices
            self.shape_codes = self.path.codes
            matplotlib.hatch.Shapes.__init__(self, hatch, density)

    matplotlib.hatch._hatch_types.append(CustomHatch)
    
for element in list_c_hatch:
    add_hatch(element[1], element[0])
    



#---------------------------------------------- DICT GRAIN -----------------------------------------------

#Dictionary for grain size
DICT_GRAIN = {'cl':0.55,
              'cls':0.58,
              's':0.6,
              'svf':0.63,
              'vf':0.65,
              'vff':0.68,
              'f':0.7,
              'fm':0.73,
              'm':0.75,
              'mc':0.78,
              'c':0.8,
              'cvc':0.83,
              'vc':0.85,
              'vcg':0.88,
              'g':0.9,
              'gp':0.93,
              'p':0.95,
              'pco':0.97,
              'co':0.98,
              'cob':0.99,
              'b':1}

#---------------------------------------------- DICT LITHO -----------------------------------------------

#Dictionary for lithologies
DICT_LITHO = {'f':18000, #Mudstone
             'cl':20000, #Claystone
             'sh':17000, #Shale
             'sl':19000, #Siltstone
             's':11000,  #Sandstone
             'svf':11500,#Sandstone very fine
             'sf':11600, #Sandstone fine
             'sm':11700, #Sandstone medium
             'sc':11800, #Sandstone gross
             'svc':11900,#Sandstone very gross
             'g':12000,  #Conglomerade
             'c':31000,  #Coal
             'l':22000,  #Limestone
             'ch':28000, #Chert
             'v':35000,  #Volcaniclastic
             
             'lm':24000, #Lime mudstone
             'olm':25000,#Oolite Limestone
             'ws':26000, #Wackstone
             'ps':27000, #Packstone
             'gs':23000, #Grainstone
             'h':29000,  #Halite
             'gy':30000, #Gypsum
             'd':21000,  #Dolomite
             
             'b':15000,  #Breccia
             'mg':13000, #Matrix-sup conglomerate
             'cg':14000, #Clast-sup conglomerate
             'lv':32000, #Lava
             'fa':33000, #Fine ash
             'ca':34000, #Coarse ash
             
             'db':36000, #Diabase
             'bt':37000, #Basalt
             'bs':38000, #Basement
             'gn':39000, #Gneiss
             'sch':40000,#Schist
              
             'ssh':16000,#Sandstone/Shale
              
             '-':99999}  

#---------------------------------------------- DICT LITHOLOGIES -----------------------------------------------

#Definición de tramas y colores para las litologías
LITHOLOGIES = {11500: {'lith':'Sandstone very fine', 'sedlog': False,'sp':'Arenisca muy fina','lith_num':1, 'hatch': '..', 'color':'#ffff00'},
              11600: {'lith':'Sandstone fine', 'sedlog': False,'sp':'Arenisca fina','lith_num':1, 'hatch': '..', 'color':'#e8e800'},
              11700: {'lith':'Sandstone medium', 'sedlog': False,'sp':'Arenisca media','lith_num':1, 'hatch': '..', 'color':'#e3d617'},
              11800: {'lith':'Sandstone gross', 'sedlog': False,'sp':'Arenisca gruesa','lith_num':1, 'hatch': '..', 'color':'#cfcf02'},
              11900: {'lith':'Sandstone very gross', 'sedlog': False,'sp':'Arenisca muy gruesa','lith_num':1, 'hatch': '..', 'color':'#baba02'},
              11000: {'lith':'Sandstone', 'sedlog': True,'sp':'Arenisca','lith_num':1, 'hatch': '..', 'color':'#ffff00'},              
              12000: {'lith':'Conglomerade', 'sedlog': True,'sp':'Conglomerado','lith_num':2, 'hatch':'O', 'color':'#b3b302'},
              13000: {'lith':'Matrix-sup conglomerate', 'sedlog': True,'sp':'Conglomerado matriz soportado','lith_num':3, 'hatch':'O', 'color':'#b3b302'},
              14000: {'lith':'Clast-sup conglomerate', 'sedlog': True,'sp':'Conglomerado clasto soportado','lith_num':4, 'hatch':'ob2b1b2', 'color':'#b3b302'},
              15000: {'lith':'Breccia', 'sedlog': True,'sp':'Brecha','lith_num':5, 'hatch':'b2gb1', 'color':'#b3b302'},
              16000: {'lith':'Sandstone/Shale','sedlog': False, 'sp':'Arenisca','lith_num':6, 'hatch':'-.', 'color':'#ffe119'},
              17000: {'lith':'Shale', 'sedlog': True,'sp':'Esquisto','lith_num':7, 'hatch':'--', 'color':'#bebebe'},
              18000: {'lith':'Mudstone', 'sedlog': True,'sp':'Lutita','lith_num':8, 'hatch':'b1ee', 'color':'#9c793e'},
              19000: {'lith':'Siltstone', 'sedlog': True,'sp':'Limolita','lith_num':9, 'hatch':'b1b2', 'color':'#d1c7b6'},
              20000: {'lith':'Claystone', 'sedlog': True,'sp':'Pelita','lith_num':10, 'hatch':'c', 'color':'#baa786'},
              21000: {'lith':'Dolomite', 'sedlog': True,'sp':'Dolomita','lith_num':11, 'hatch':'-d', 'color':'#ccb8f2'},
              22000: {'lith':'Limestone', 'sedlog': True,'sp':'Caliza','lith_num':12, 'hatch':'-l', 'color':'#80ffff'},
              23000: {'lith':'Grainstone', 'sedlog': True,'sp':'???','lith_num':13, 'hatch':'--ll', 'color':'#80ffff'},
              24000: {'lith':'Lime mudstone', 'sedlog': True,'sp':'???','lith_num':14, 'hatch':'-lm', 'color':'#80ffff'},              
              25000: {'lith':'Oolite Limestone', 'sedlog': False,'sp':'Caliza oolítica','lith_num':15, 'hatch':'-lO', 'color':'#80ffff'},
              26000: {'lith':'Wackstone', 'sedlog': True,'sp':'???','lith_num':16, 'hatch':'c|', 'color':'#c6f5f5'},
              27000: {'lith':'Packstone', 'sedlog': True,'sp':'???','lith_num':17, 'hatch':'.-|', 'color':'#e3ffff'},
              28000: {'lith':'Chert', 'sedlog': True,'sp':'Chert','lith_num':18, 'hatch':'e', 'color':'#fcddcc'},
              29000: {'lith':'Halite', 'sedlog': True,'sp':'Halita','lith_num':19, 'hatch':'x', 'color':'#7ddfbe'},
              30000: {'lith':'Gypsum', 'sedlog': True,'sp':'Yeso','lith_num':20, 'hatch':'\\\\', 'color':'#ae97db'},
              31000: {'lith':'Coal', 'sedlog': True,'sp':'Carbón','lith_num':21, 'hatch':'', 'color':'#000000'},
              32000: {'lith':'Lava', 'sedlog': True,'sp':'Lava','lith_num':22, 'hatch':'-a', 'color':'#f7a14a'},
              33000: {'lith':'Fine ash', 'sedlog': True,'sp':'Ceniza volcánica','lith_num':23, 'hatch':'b2b1b2', 'color':'#e3e2e1'},
              34000: {'lith':'Coarse ash', 'sedlog': True,'sp':'Ceniza volcánica','lith_num':24, 'hatch':'a', 'color':'#e3e2e1'},
              35000: {'lith':'Volcaniclastic', 'sedlog': True,'sp':'Ceniza volcánica','lith_num':25, 'hatch':'', 'color':'#e3e2e1'},
              36000: {'lith':'Diabase', 'sedlog': False,'sp':'Diabasa','lith_num':26, 'hatch':'ib2', 'color':'#687a68'},
              37000: {'lith':'Basalt', 'sedlog': False,'sp':'Basalto','lith_num':27, 'hatch':'ca', 'color':'#687a68'},
              38000: {'lith':'Basement', 'sedlog': False,'sp':'Basamento','lith_num':28, 'hatch':'f', 'color':'#d95959'},
              39000: {'lith':'Gneiss', 'sedlog': False,'sp':'Gneiss','lith_num':29, 'hatch':'/a', 'color':'#67706d'},
              40000: {'lith':'Schist', 'sedlog': False,'sp':'Esquisto','lith_num':30, 'hatch':'gd', 'color':'#889490'},
              99999: {'lith':'Not available', 'sedlog': False,'sp':'No disponible','lith_num':99, 'hatch':'', 'color':'white'}}


#---------------------------------------------- IMAGES -----------------------------------------------

#img_amo = plt.imread('images/Amo.png')

path = os.path.dirname(pd.__file__)[:-6]

#/stratilib/images of structures
img_r =  plt.imread(path + '/stratilib/images/ripple.png')
img_w =  plt.imread(path + '/stratilib/images/wripple.png')
img_p =  plt.imread(path + '/stratilib/images/p.png')
img_cr =  plt.imread(path + '/stratilib/images/cr.png')
img_h =  plt.imread(path + '/stratilib/images/h.png')
img_hm =  plt.imread(path + '/stratilib/images/hm.png')
img_sw =  plt.imread(path + '/stratilib/images/sw.png')
img_mc =  plt.imread(path + '/stratilib/images/mc.png')
img_sc =  plt.imread(path + '/stratilib/images/sc.png')
img_cl =  plt.imread(path + '/stratilib/images/cl.png')
img_lc =  plt.imread(path + '/stratilib/images/lc.png')
img_ws =  plt.imread(path + '/stratilib/images/ws.png')
img_hb =  plt.imread(path + '/stratilib/images/hb.png')
img_nac =  plt.imread(path + '/stratilib/images/nac.png')
img_int =  plt.imread(path + '/stratilib/images/int.png')
img_mcl =  plt.imread(path + '/stratilib/images/mcl.png')
img_flm =  plt.imread(path + '/stratilib/images/flm.png')
img_gro =  plt.imread(path + '/stratilib/images/gro.png')
img_scr =  plt.imread(path + '/stratilib/images/scr.png')


#/stratilib/images of Fossils
img_fsh   = plt.imread(path + '/stratilib/images/fsh.png')
img_fbi   = plt.imread(path + '/stratilib/images/fbi.png')
img_fga   = plt.imread(path + '/stratilib/images/fga.png')
img_fce   = plt.imread(path + '/stratilib/images/fce.png')
img_fbr   = plt.imread(path + '/stratilib/images/fbr.png')
img_fec   = plt.imread(path + '/stratilib/images/fec.png')
img_fcr   = plt.imread(path + '/stratilib/images/fcr.png')
img_fsco  = plt.imread(path + '/stratilib/images/fsco.png')
img_fcco  = plt.imread(path + '/stratilib/images/fcco.png')
img_ffo   = plt.imread(path + '/stratilib/images/ffo.png')
img_fal   = plt.imread(path + '/stratilib/images/fal.png')
img_fbry  = plt.imread(path + '/stratilib/images/fbry.png')
img_fst   = plt.imread(path + '/stratilib/images/fst.png')
img_fve   = plt.imread(path + '/stratilib/images/fve.png')
img_fplm  = plt.imread(path + '/stratilib/images/fplm.png')
img_fro   = plt.imread(path + '/stratilib/images/fro.png')
img_flo   = plt.imread(path + '/stratilib/images/flo.png')
img_ftrs  = plt.imread(path + '/stratilib/images/ftrs.png')
img_fos   = plt.imread(path + '/stratilib/images/fos.png')
img_fra   = plt.imread(path + '/stratilib/images/fra.png')
img_fsp   = plt.imread(path + '/stratilib/images/fsp.png')
img_fbiol = plt.imread(path + '/stratilib/images/fbiol.png')
img_fbiom = plt.imread(path + '/stratilib/images/fbiom.png')
img_fbioh = plt.imread(path + '/stratilib/images/fbioh.png')
img_ftrk  = plt.imread(path + '/stratilib/images/ftrk.png')
img_ftra  = plt.imread(path + '/stratilib/images/ftra.png')
img_fvbu  = plt.imread(path + '/stratilib/images/fvbu.png')
img_fhbu  = plt.imread(path + '/stratilib/images/fhbu.png')



#---------------------------------------------- DICT STRUCT & FOSSILS -----------------------------------------------

#Dictionary for structures images
DICT_STRUCT = {'r':img_r,
               'w':img_w,
               'p':img_p,
               'cr':img_cr,
               'h':img_h,
               'hm':img_hm,
               'sw':img_sw,
               'mc':img_mc,
               'sc':img_sc,
               'cl':img_cl,
               'lc':img_lc,
               'ws':img_ws,
               'hb':img_hb,
               'nac':img_nac,
               'int':img_int,
               'mcl':img_mcl,
               'flm':img_flm,
               'gro':img_gro,
               'scr':img_scr}

#Dictionary for fossils images
DICT_FOSSILS = {'fsh':img_fsh,
                'fbi':img_fbi,
                'fga':img_fga,
                'fce':img_fce,
                'fbr':img_fbr,
                'fec':img_fec,
                'fcr':img_fcr,
                'fsco':img_fsco,
                'fcco':img_fcco,
                'ffo':img_ffo,
                'fal':img_fal,
                'fbry':img_fbry,
                'fst':img_fst,
                'fve':img_fve,
                'fplm':img_fplm,
                'fro':img_fro,
                'flo':img_flo,
                'ftrs':img_ftrs,
                'fos':img_fos,
                'fra':img_fra,
                'fsp':img_fsp,
                'fbiol':img_fbiol,
                'fbiom':img_fbiom,
                'fbioh':img_fbioh,
                'ftrk':img_ftrk,
                'ftra':img_ftra,
                'fvbu':img_fvbu,
                'fhbu':img_fhbu}

#---------------------------------------------- REVERT DICTIONARIES -----------------------------------------------

DICT_GRAIN_RV = {v: k for k, v in DICT_GRAIN.items()}
DICT_LITHO_RV = {v: k for k, v in DICT_LITHO.items()}
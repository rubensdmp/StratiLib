# coding=utf-8

#Diccionario para granulometría
DICT_GRAN = {'cl':0.55,
              's':0.6,
              'vf':0.65,
              'f':0.7,
              'm':0.75,
              'c':0.8,
              'vc':0.85,
              'g':0.9}


#Diccionario para litologías
DICT_LITO = {'C':100,
            'M':200,
            'B':300,
            'S':400,
            'Sf':400,
            'Sm':450,
            'Sc':475,
            'Sg':490,
            'G':500,
            'D':600}

#Definición de tramas y colores para las litologías
LITHOLOGYS = {400: {'lith':'Sandstone', 'lith_num':1, 'hatch': '..', 'color':'#ffff00'},
              450: {'lith':'Sandstone', 'lith_num':1, 'hatch': '..', 'color':'#e8e800'},
              475: {'lith':'Sandstone', 'lith_num':1, 'hatch': '..', 'color':'#cfcf02'},
              490: {'lith':'Sandstone', 'lith_num':1, 'hatch': '..', 'color':'#bfb302'},
              100: {'lith':'Sandstone/Shale', 'lith_num':2, 'hatch':'-.', 'color':'#ffe119'},
              65000: {'lith':'Shale', 'lith_num':3, 'hatch':'--', 'color':'#bebebe'},
              74000: {'lith':'Dolomite', 'lith_num':5, 'hatch':'-/', 'color':'#8080ff'},
              86000: {'lith':'Limestone', 'lith_num':6, 'hatch':'+', 'color':'#80ffff'},
              70032: {'lith':'Chalk', 'lith_num':7, 'hatch':'..', 'color':'#80ffff'},
              65030: {'lith':'Halite', 'lith_num':8, 'hatch':'x', 'color':'#7ddfbe'},
              200: {'lith':'Mudstone', 'lith_num':9, 'hatch':'', 'color':'#9c793e'},
              600: {'lith':'Diabase', 'lith_num':10, 'hatch':'-|', 'color':'#144513'},
              300: {'lith':'Basalt', 'lith_num':11, 'hatch':'', 'color':'#144513'},
              500: {'lith':'Basement', 'lith_num':12, 'hatch':'-|', 'color':'#ef138a'},
              8800: {'lith':'Gypsum', 'lith_num':13, 'hatch':'\\\\', 'color':'#ae97db'},
              8440: {'lith':'Conglomerade', 'lith_num':14, 'hatch':'o', 'color':'#b3b302'}}

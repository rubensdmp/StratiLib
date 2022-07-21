#---------------------------------------------- DICT CONTACTS -----------------------------------------------

#Dictionary for 'BASE BOUNDARY'
DICT_DF_SL_CONTACTS = {'s':'Sharp',
                       'e':'Erosion',
                       'g':'Gradational'}


#---------------------------------------------- DICT STRUCTURES -----------------------------------------------

#Dictionary for Sedimentary structures in SYMBOLS IN BED' y 'SYMBOLS/STRUCTURES'
DICT_DF_SL_STRUCTURES = {'':'<none>',
                         'r':'Current ripple cross-lamination',
                         'w':'Wave ripple cross-lamination',
                         'p':'Planar cross bedding',
                         'cr':'Trough cross bedding',
                         'h':'Horizontal planar lamination',
                         'hm':'Hummocky cross stratification',
                         'sw':'Swaley cross srtatification',
                         'mc':'Mudcracks',
                         'sc':'Synaeresis cracks',
                         'cl':'Convolute lamination',
                         'lc':'Load casts',
                         'ws':'Water structures',
                         'hb':'Herring-bones cross bedding',
                         'nac':'Nodules and concretions',
                         'int':'Intraclasts',
                         'mcl':'Mudclasts',
                         'flm':'Flute marks',
                         'gro':'Groove marks',
                         'scr':'Scours'}

#---------------------------------------------- DICT FOSSILS -----------------------------------------------

#Dictionary for Fossils in SYMBOLS IN BED' y 'SYMBOLS/STRUCTURES'
DICT_DF_SL_FOSSILS = {'fsh':'Shells',
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
                      'fbiol':'Minor bioturbation',
                      'fbiom':'Moderate bioturbation',
                      'fbioh':'Intense bioturbation',
                      'ftrk':'Tracks',
                      'ftra':'Trails',
                      'fvbu':'Vertical burrows',
                      'fhbu':'Horizontal burrows'}


#---------------------------------------------- DICT GRAINS -----------------------------------------------

#Dictionary for 'GRAIN SIZE BASE' y 'GRAIN SIZE TOP'
DICT_DF_SL_GRAINS = {'cl':'clay',
                     'cls':'clay/silt',
                     's':'silt',
                     'svf':'silt/vf',
                     'vf':'vf',
                     'vff':'vf/f',
                     'f':'f',
                     'fm':'f/m',
                     'm':'m',
                     'mc':'m/c',
                     'c':'c',
                     'cvc':'c/vc',
                     'vc':'vc',
                     'vcg':'vc/granule',
                     'g':'granule',
                     'gp':'granule/pebble',
                     'p':'pebble',
                     'pco':'pebble/cobble',
                     'co':'cobble',
                     'cob':'cobble/boulder',
                     'b':'boulder'}

#---------------------------------------------- PHI GRAINS -----------------------------------------------

#Dictionary for 'GRAIN SIZE BASE' y 'GRAIN SIZE TOP'
DICT_DF_SL_PHI = {'cl':10.0,
                  'cls':8.0,
                  's':6.0,
                  'svf':4.0,
                  'vf':3.5,
                  'vff':3.0,
                  'f':2.5,
                  'fm':2.0,
                  'm':1.5,
                  'mc':1.0,
                  'c':0.5,
                  'cvc':0.0,
                  'vc':-0.5,
                  'vcg':-1.0,
                  'g':-1.5,
                  'gp':-2.3,
                  'p':-3.0,
                  'pco':-4.5,
                  'co':-6.0,
                  'cob':-8.0,
                  'b':-10.0}


#---------------------------------------------- DICT LITHO -----------------------------------------------
#Lithologies in SEDLOG
DICT_DF_SL_LITHO = {'f':'Mudstone',
                    'cl':'Claystone',
                    'sh':'Shale',
                    'sl':'Siltstone',
                    's':'Sandstone',
                    'g':'Conglomerate',
                    'c':'Coal',
                    'l':'Limestone',
                    'ch':'Chert',
                    'v':'Volcaniclastic',
                    
                    'lm':'Lime mudstone',
                    'ws':'Wackstone',
                    'ps':'Packstone',
                    'gs':'Grainstone',
                    'h':'Halite',
                    'gy':'Gypsum/Anhydrite',
                    'd':'Dolomite',
                    
                    'b':'Breccia',
                    'mg':'Matrix-supported conglomerate',
                    'cg':'Clast-supported conglomerate',
                    'lv':'Lava',
                    'fa':'Fine ash',
                    'ca':'Coarse ash',
                    
                    '-': '<none>'}


#---------------------------------------------- INVERT DICTIONARIES -----------------------------------------------

#Diccionarios invertidos para el pasaje de SedLog a StratiLib

DICT_SL_DF_LITHO = {v: k for k, v in DICT_DF_SL_LITHO.items()}
DICT_SL_DF_GRAINS = {v: k for k, v in DICT_DF_SL_GRAINS.items()}
DICT_SL_DF_CONTACTS = {v: k for k, v in DICT_DF_SL_CONTACTS.items()}
DICT_SL_DF_STRUCTURES = {v: k for k, v in DICT_DF_SL_STRUCTURES.items()}
DICT_SL_DF_FOSSILS = {v: k for k, v in DICT_DF_SL_FOSSILS.items()}
DICT_SL_DF_PHI = {v: k for k, v in DICT_DF_SL_PHI.items()}
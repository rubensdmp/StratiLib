# StratiLib

Working in progres...

Open-source, stratigraphic columns modeling in Python.
[![license: LGPL v3](https://img.shields.io/badge/license-LGPL%20v3-blue.svg)](https://github.com/rubensdmp/StratiLib/blob/main/LICENCE)

## Introduction\n
    
Library for stratigraphy and geophysical studies

With this library we can plot stratigraphic columns and link files with SedLog 3.1

## Installation
    
``` python
pip install stratilib
````

## Quick start
    
``` python
import stratilib as sl
df_lithology = sl.read_lito('my_data.xlsx')
sl.plot_lito(df_lithology, plot_width, top_depth, bottom_depth)
```
In the tutorial notebooks you can find more parameters.

## Gallery


### Stratigraphic columns
![Example 1](Images/Perfíl.png)
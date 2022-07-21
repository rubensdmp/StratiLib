# ⛏️ StratiLib

**`StratiLib` facilitates the loading, processing and ploting stratigraphic columns.**

>Open-source stratigraphic modeling in Python.

[![license: LGPL v3](https://img.shields.io/badge/license-LGPL%20v3-blue.svg)](https://github.com/rubensdmp/StratiLib/blob/main/LICENCE)
Designed by [Rubens Merlino](https://www.linkedin.com/in/rubens-merlino-uy/).

## 📝 Introduction

StratiLib was designed to plot stratigraphic columns with matplotlib and analyze stratigraphic data with a very simple excel input file for non programers.

StratiLib reads Excel files (xlsx) and csv files from exporting SedLog 3.1 plots, and also from xlsx files, with a very simple format, generate csv files to import from SedLog 3.1 too.

StratiLib has all and more lithologys than sedLog 3.1 and also, at least, the same geological structures, fossils and trace fossils to be referenced in stratigraphic columns.

StratiLib use Pandas Dataframes to manipulate data.

In further versions, StratiLib will can analyze data statistically and apply machine learning models to them. 


## ⚡ Installation

``` python
pip install stratilib
```

StratiLib depends on the following packages:

-   `pandas`
-   `matplotlib`
-   `numpy`


## 📓 Quick start

In the next lines you can see the most important functions of StratiLib

``` python
#Import library
import stratilib as sl

#Read data
df_lithology = sl.read_litho('my_data.xlsx', **kwargs)

#Plot data
sl.plot_litho(df_lithology, plot_width, top_depth, bottom_depth, **kwargs)

#Read SedLog csv
df_sedlog = sl.read_sedlog(name = "my_sedlog.csv")

#Plot SedLog data
sl.plot_litho(df_sedlog, plot_width, top_depth, bottom_depth, **kwargs)

#Write SedLog csv to be imported from SedLog 3.1
sl.to_sedlog_csv(df_data, **kwargs)

#Plot lithologies
sl.show_litho(**kwargs)

#Plot structures and fossils
sl.plot_structs(**kwargs)
```

In the tutorial notebooks you can find more parameters.

:notebook:

## 📚 Documentation

The StratiLib documentation is a work in progress.

## 💡 Questions or suggestions?

To report bugs or suggest new features/improvements to the code, please [open an issue](https://github.com/rubensdmp/StratiLib/issues).

## ✨ Contributing

There are several important ways you can help; here are some examples:

- Submitting bug reports and feature requests: see [Issues](https://github.com/rubensdmp/StratiLib/issues).
- Fixing typos and generally improving the documentation.
- Writing tutorials, examples, and how-to documents.

Please see contact [me](https://www.linkedin.com/in/rubens-merlino-uy/) for more information.

## 🖼️ Gallery of examples



### Example of lithologies and its patterns that can be used
``` python
#Plot lithologies
sl.show_litho()
```
![Example 1](https://github.com/rubensdmp/StratiLib/blob/main/images/readme/lithologies.png?raw=true)



### Example of Structures and Fossils that can be used
``` python
#Plot structures and fossils
sl.plot_structs()
```
![Example 2](https://github.com/rubensdmp/StratiLib/blob/main/images/readme/StructuresANDFossils.png?raw=true)
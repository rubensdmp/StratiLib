{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bf38321c",
   "metadata": {},
   "source": [
    "# StratiLib\n",
    "Working in progres...\n",
    "\n",
    "Open-source, stratigraphic columns modeling in Python.\n",
    "[![license: LGPL v3](https://img.shields.io/badge/license-LGPL%20v3-blue.svg)](https://github.com/rubensdmp/StratiLib/blob/main/LICENCE)\n",
    "\n",
    "\n",
    "## Introduction\n",
    "\n",
    "Library for stratigraphy and geophysical studies\n",
    "\n",
    "With this library we can plot stratigraphic columns and link files with SedLog 3.1\n",
    "\n",
    "\n",
    "## Installation\n",
    "\n",
    "``` python \n",
    "pip install stratilib\n",
    "````\n",
    "\n",
    "\n",
    "## Quick start\n",
    "\n",
    "``` python\n",
    "import stratilib as sl\n",
    "df_lithology = sl.read_lito('my_data.xlsx')\n",
    "sl.plot_lito(df_lithology, plot_width, top_depth, bottom_depth)\n",
    "```\n",
    "\n",
    "In the tutorial notebooks you can find more parameters.\n",
    "\n",
    "## Gallery\n",
    "\n",
    "### Stratigraphic columns\n",
    "![Example 1](images/Perfíl.png)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0023469e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

# StratiLib

[![license: LGPL v3](https://img.shields.io/badge/license-LGPL%20v3-blue.svg)]

## Introduction

Library for stratigraphy and geophysical studies

With this library we can plot stratigraphic columns and link files with SedLog 3.1

[![PyPI license](https://img.shields.io/pypi/l/welly.svg)](https://pypi.org/project/welly/)

**`welly` facilitates the loading, processing, and analysis of subsurface wells and well data, such as striplogs, formation tops, well log curves, and synthetic seismograms.**

GeoPandas is a project to add support for geographic data to [pandas](http://pandas.pydata.org) objects. It currently implements `GeoSeries` and `GeoDataFrame` types which are subclasses of `pandas.Series` and `pandas.DataFrame` respectively. GeoPandas objects can act on [shapely](http://shapely.readthedocs.io/en/latest/) geometry objects and perform geometric operations.

GeoPandas geometry operations are cartesian. The coordinate reference system (crs) can be stored as an attribute on an object, and is automatically set when loading from a file. Objects may be transformed to new coordinate systems with the `to_crs()` method. There is currently no enforcement of like coordinates for operations, but that may change in the future.

Documentation is available at [geopandas.org](http://geopandas.org) (current release) and [Read the Docs](http://geopandas.readthedocs.io/en/latest/) (release and development versions).

## Installation

    pip install stratilib

For developers, there are `pip` options for installing `test`, `docs` or `dev` (docs plus test) dependencies.

## Quick start

``` python
import stratilib as sl

df_lithology = sl.read_lito('my_data.xlsx')

sl.plot_lito(df_lithology, plot_width, top_depth, bottom_depth)
```

In the tutorial notebooks you can find more parameters.

## Documentation

[The StratiLib documentation] is a work in progress.

## Questions or suggestions?

[![slack](https://img.shields.io/badge/chat-on_slack-808493.svg?longCache=true&style=flat&logo=slack)](https://swung.slack.com/)

**If you'd like to chat about `welly` with us or other users, look for the** #welly-and-lasio\*\* channel in the [Software Underground's Slack](https://softwareunderground.org/slack).\*\*

To report bugs or suggest new features/improvements to the code, please [open an issue](https://github.com/agilescientific/welly/issues).

## Contributing

Please see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Philosophy

The [`lasio`](https://github.com/kinverarity1/lasio) project provides a very nice way to read and write [CWLS](http://www.cwls.org/) Log ASCII Standard files. The result is an object that contains all the LAS data --- it's more or less analogous to the LAS file.

Sometimes we want a higher-level object, for example to contain methods that have nothing to do with LAS files. We may want to handle other well data, such as deviation surveys, tops (aka picks), engineering data, striplogs, synthetics, and so on. This is where `welly` comes in.

`welly` uses `lasio` for data I/O, but hides much of it from the user. We recommend you look at both projects before deciding if you need the 'well-level' functionality that `welly` provides.

[![pypi](https://img.shields.io/pypi/v/geopandas.svg)](https://pypi.python.org/pypi/geopandas/) [![Actions Status](https://github.com/geopandas/geopandas/workflows/Tests/badge.svg)](https://github.com/geopandas/geopandas/actions?query=workflow%3ATests) [![Coverage Status](https://codecov.io/gh/geopandas/geopandas/branch/main/graph/badge.svg)](https://codecov.io/gh/geopandas/geopandas) [![Join the chat at https://gitter.im/geopandas/geopandas](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/geopandas/geopandas?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/geopandas/geopandas/main) [![DOI](https://zenodo.org/badge/11002815.svg)](https://zenodo.org/badge/latestdoi/11002815)

## Install

See the [installation docs](https://geopandas.readthedocs.io/en/latest/install.html) for all details. GeoPandas depends on the following packages:

-   `pandas`
-   `shapely`
-   `fiona`
-   `pyproj`
-   `packaging`

Further, `matplotlib` is an optional dependency, required for plotting, and [`rtree`](https://github.com/Toblerity/rtree) is an optional dependency, required for spatial joins. `rtree` requires the C library [`libspatialindex`](https://github.com/libspatialindex/libspatialindex).

Those packages depend on several low-level libraries for geospatial analysis, which can be a challenge to install. Therefore, we recommend to install GeoPandas using the [conda package manager](https://conda.io/en/latest/). See the [installation docs](https://geopandas.readthedocs.io/en/latest/install.html) for more details.

## Get in touch

-   Ask usage questions ("How do I?") on [StackOverflow](https://stackoverflow.com/questions/tagged/geopandas) or [GIS StackExchange](https://gis.stackexchange.com/questions/tagged/geopandas).
-   Report bugs, suggest features or view the source code [on GitHub](https://github.com/geopandas/geopandas).
-   For a quick question about a bug report or feature request, or Pull Request, head over to the [gitter channel](https://gitter.im/geopandas/geopandas).
-   For less well defined questions or ideas, or to announce other projects of interest to GeoPandas users, ... use the [mailing list](https://groups.google.com/forum/#!forum/geopandas).

## Examples

    >>> import geopandas
    >>> from shapely.geometry import Polygon
    >>> p1 = Polygon([(0, 0), (1, 0), (1, 1)])
    >>> p2 = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
    >>> p3 = Polygon([(2, 0), (3, 0), (3, 1), (2, 1)])
    >>> g = geopandas.GeoSeries([p1, p2, p3])
    >>> g
    0         POLYGON ((0 0, 1 0, 1 1, 0 0))
    1    POLYGON ((0 0, 1 0, 1 1, 0 1, 0 0))
    2    POLYGON ((2 0, 3 0, 3 1, 2 1, 2 0))
    dtype: geometry

![Example 1](doc/source/gallery/test.png)

Some geographic operations return normal pandas object. The `area` property of a `GeoSeries` will return a `pandas.Series` containing the area of each item in the `GeoSeries`:

    >>> print(g.area)
    0    0.5
    1    1.0
    2    1.0
    dtype: float64

Other operations return GeoPandas objects:

    >>> g.buffer(0.5)
    0    POLYGON ((-0.3535533905932737 0.35355339059327...
    1    POLYGON ((-0.5 0, -0.5 1, -0.4975923633360985 ...
    2    POLYGON ((1.5 0, 1.5 1, 1.502407636663901 1.04...
    dtype: geometry

![Example 2](doc/source/gallery/test_buffer.png)

GeoPandas objects also know how to plot themselves. GeoPandas uses [matplotlib](http://matplotlib.org) for plotting. To generate a plot of our GeoSeries, use:

    >>> g.plot()

GeoPandas also implements alternate constructors that can read any data format recognized by [fiona](http://fiona.readthedocs.io/en/latest/). To read a zip file containing an ESRI shapefile with the [boroughs boundaries of New York City](https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm) (GeoPandas includes this as an example dataset):

    >>> nybb_path = geopandas.datasets.get_path('nybb')
    >>> boros = geopandas.read_file(nybb_path)
    >>> boros.set_index('BoroCode', inplace=True)
    >>> boros.sort_index(inplace=True)
    >>> boros
                   BoroName     Shape_Leng    Shape_Area  \
    BoroCode
    1             Manhattan  359299.096471  6.364715e+08
    2                 Bronx  464392.991824  1.186925e+09
    3              Brooklyn  741080.523166  1.937479e+09
    4                Queens  896344.047763  3.045213e+09
    5         Staten Island  330470.010332  1.623820e+09

                                                       geometry
    BoroCode
    1         MULTIPOLYGON (((981219.0557861328 188655.31579...
    2         MULTIPOLYGON (((1012821.805786133 229228.26458...
    3         MULTIPOLYGON (((1021176.479003906 151374.79699...
    4         MULTIPOLYGON (((1029606.076599121 156073.81420...
    5         MULTIPOLYGON (((970217.0223999023 145643.33221...

![New York City boroughs](doc/source/gallery/nyc.png)

    >>> boros['geometry'].convex_hull
    BoroCode
    1    POLYGON ((977855.4451904297 188082.3223876953,...
    2    POLYGON ((1017949.977600098 225426.8845825195,...
    3    POLYGON ((988872.8212280273 146772.0317993164,...
    4    POLYGON ((1000721.531799316 136681.776184082, ...
    5    POLYGON ((915517.6877458114 120121.8812543372,...
    dtype: geometry

![Convex hulls of New York City boroughs](doc/source/gallery/nyc_hull.png)

\#

<p align="center">

<img src="docs/readme_images/header_combined_slim.png" width="1000"/>

</p>

> Open-source, implicit 3D structural geological modeling in Python.

[![PyPI](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/downloads/) [![PyPI](https://img.shields.io/badge/pypi-1.0-blue.svg)](https://pypi.org/project/gempy/) [![license: LGPL v3](https://img.shields.io/badge/license-LGPL%20v3-blue.svg)](https://github.com/cgre-aachen/gempy/blob/master/LICENSE) [![Documentation Status](https://assets.readthedocs.org/static/projects/badges/passing-flat.svg)](http://docs.gempy.org) [![Travis Build](https://travis-ci.org/cgre-aachen/gempy.svg?branch=master)](https://travis-ci.org/github/cgre-aachen/gempy/branches) [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/cgre-aachen/gempy/master) [![DOI](https://zenodo.org/badge/96211155.svg)](https://zenodo.org/badge/latestdoi/96211155) [![DOCKER](https://img.shields.io/docker/cloud/automated/leguark/gempy.svg)](https://cloud.docker.com/repository/docker/leguark/gempy)

:warning: **Warning: GemPy requires pandas version \< 1.4.0. The new pandas release is not compatible with GemPy.\
We're actively working on this issue for a future release.\
Please make sure to use Pandas version 1.3.x when working with GemPy for the time being.** :warning: \## Overview

[GemPy](https://www.gempy.org/) is a Python-based, **open-source geomodeling library**. It is capable of constructing complex **3D geological models** of folded structures, fault networks and unconformities, based on the underlying powerful **implicit representation** approach.

## Installation

We provide the latest release version of GemPy via PyPi package services. We highly recommend using PyPi,

`$ pip install gempy`

as it will take care of automatically installing all the required dependencies - except in windows that requires one extra step.

Windows does not have a gcc compilers pre-installed. The easiest way to get a theano compatible compiler is by using the theano conda installation. Therefore the process would be the following:

`$ conda install theano`

`$ pip install gempy`

For more information, refer to the [installation documentation](https://docs.gempy.org/installation.html).

## Resources

After installation you can either check the [notebook tutorials](https://docs.gempy.org/getting_started/get_started.html#sphx-glr-getting-started-get-started-py) or the [video introduction](https://www.youtube.com/watch?v=n0btC5Zilyc) to get started.

Go to the [documentation site](http://docs.gempy.org/) for further information and enjoy the [tutorials and examples](https://www.gempy.org/tutorials).

For questions and support, please use [discussions](https://github.com/cgre-aachen/gempy/discussions).

If you find a bug or have a feature request, create an [issue](https://github.com/cgre-aachen/gempy/issues).

Follow these [guidelines](https://github.com/cgre-aachen/gempy/blob/WIP_readme-update-march21/CONTRIBUTING.md) to contribute to GemPy.

<a name="ref"></a> \## References

-   de la Varga, M., Schaaf, A., and Wellmann, F. (2019). [GemPy 1.0: open-source stochastic geological modeling and inversion](https://gmd.copernicus.org/articles/12/1/2019/gmd-12-1-2019.pdf), Geosci. Model Dev., 12, 1-32.
-   Wellmann, F., & Caumon, G. (2018). [3-D Structural geological models: Concepts, methods, and uncertainties.](https://hal.univ-lorraine.fr/hal-01921494/file/structural_models_for_geophysicsHAL.pdf) In Advances in Geophysics (Vol. 59, pp. 1-121). Elsevier.
-   Calcagno, P., Chilès, J. P., Courrioux, G., & Guillen, A. (2008). Geological modelling from field data and geological knowledge: Part I. Modelling method coupling 3D potential-field interpolation and geological rules. Physics of the Earth and Planetary Interiors, 171(1-4), 147-157.
-   Lajaunie, C., Courrioux, G., & Manuel, L. (1997). Foliation fields and 3D cartography in geology: principles of a method based on potential interpolation. Mathematical Geology, 29(4), 571-584.

## Publications using GemPy

-   Schaaf, A., de la Varga, M., Wellmann, F., & Bond, C. E. (2021). [Constraining stochastic 3-D structural geological models with topology information using approximate Bayesian computation in GemPy 2.1](https://gmd.copernicus.org/articles/14/3899/2021/gmd-14-3899-2021.html). Geosci. Model Dev., 14(6), 3899-3913. <doi:10.5194/gmd-14-3899-2021>
-   Güdük, N., de la Varga, M. Kaukolinna, J. and Wellmann, F. (in review). Model-Based Probabilistic Inversion Using Magnetic Data: A Case Study on the Kevitsa Deposit.
-   Stamm, F. A., de la Varga, M., and Wellmann, F. (2019). [Actors, actions, and uncertainties: optimizing decision-making based on 3-D structural geological models](https://se.copernicus.org/articles/10/2015/2019/se-10-2015-2019.html), Solid Earth, 10, 2015--2043.
-   Wellmann, F., Schaaf, A., de la Varga, M., & von Hagke, C. (2019). [From Google Earth to 3D Geology Problem 2: Seeing Below the Surface of the Digital Earth](https://www.sciencedirect.com/science/article/pii/B9780128140482000156). In Developments in Structural Geology and Tectonics (Vol. 5, pp. 189-204). Elsevier.

A continuously growing list of gempy-applications (e.g. listing real-world models) can be found [here](https://hackmd.io/@Japhiolite/B1juPvCxc).

## Gallery

### Stratigraphic columns

<p>

|                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                      |                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [![colormapped image plot thumbnail](docs/readme_images/model1_nodata.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/examples/geometries/1_horizontal_stratigraphic.html#sphx-glr-examples-geometries-1-horizontal-stratigraphic-py) | [![colormapped image plot thumbnail](docs/readme_images/model2_nodata.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/examples/geometries/2_fold.html#sphx-glr-examples-geometries-2-fold-py)   | [![colormapped image plot thumbnail](docs/readme_images/model3_nodata.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/examples/geometries/3_recumbent_fold.html#sphx-glr-examples-geometries-3-recumbent-fold-py) |
| [![colormapped image plot thumbnail](docs/readme_images/model4_nodata.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/examples/geometries/4_pinchout.html#sphx-glr-examples-geometries-4-pinchout-py)                                 | [![colormapped image plot thumbnail](docs/readme_images/model5_nodata.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/examples/geometries/5_fault.html#sphx-glr-examples-geometries-5-fault-py) | [![colormapped image plot thumbnail](docs/readme_images/model6_nodata.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/examples/geometries/6_unconformity.html#sphx-glr-examples-geometries-6-unconformity-py)     |

</p>

### Lithologys

<p>

|                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [![colormapped image plot thumbnail](docs/readme_images/sectiontest.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/tutorials/ch1_fundamentals/ch1_3b_cross_sections.html#sphx-glr-tutorials-ch1-fundamentals-ch1-3b-cross-sections-py) | [![colormapped image plot thumbnail](docs/readme_images/data_vis.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/tutorials/ch1_fundamentals/ch1_7_3d_visualization.html#sphx-glr-tutorials-ch1-fundamentals-ch1-7-3d-visualization-py) | [![colormapped image plot thumbnail](docs/readme_images/scalarfield.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/examples/geometries/7_combination.html#sphx-glr-examples-geometries-7-combination-py)             |
| [![colormapped image plot thumbnail](docs/readme_images/geomap.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/tutorials/ch1_fundamentals/ch1_3b_cross_sections.html#sphx-glr-tutorials-ch1-fundamentals-ch1-3b-cross-sections-py)      | [![colormapped image plot thumbnail](docs/readme_images/topology.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/tutorials/ch4-Topology/ch4-1-Topology.html#sphx-glr-tutorials-ch4-topology-ch4-1-topology-py)                         | [![colormapped image plot thumbnail](docs/readme_images/topology_matrix.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/tutorials/ch4-Topology/ch4-1-Topology.html#sphx-glr-tutorials-ch4-topology-ch4-1-topology-py) |

</p>

### Case studies

<p>

|                                                                                                                                                                                                          |                                                                                                                                                                                                               |                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [![colormapped image plot thumbnail](docs/readme_images/alesmodel.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/examples/real/Alesmodel.html#sphx-glr-examples-real-alesmodel-py) | [![colormapped image plot thumbnail](docs/readme_images/perthmodel.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/examples/real/Perth_basin.html#sphx-glr-examples-real-perth-basin-py) | [![colormapped image plot thumbnail](docs/readme_images/greenstonemodel.png){alt="colormapped image plot thumbnail"}](https://docs.gempy.org/examples/real/Greenstone.html#sphx-glr-examples-real-greenstone-py) |

</p>

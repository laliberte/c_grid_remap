# This Python file uses the following encoding: utf-8


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

from setuptools import setup, find_packages

package_name='c_grid_remap'
setup(
       name = package_name,
       version = "0.1",
       packages=[package_name],
       package_dir = {package_name: 'lib'},
#
#        # metadata for upload to PyPI
        author = "F. B. Laliberte",
        author_email = "frederic.laliberte@canada.ca",
        description = "Tools manipulate to remap to c-grids.",
        license = "BSD",
        keywords = "atmospheric sciences cryospheric sciecnes meteorology climate",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Science/Research",
            "Natural Language :: English",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 2.7",
            "Topic :: Scientific/Engineering :: Cryospheric Science",
            "Topic :: Scientific/Engineering :: Atmospheric Science",
            "Topic :: Scientific/Engineering :: Climate Science",
            "Topic :: Scientific/Engineering :: Mathematics"
        ],
        long_description=read('README'),
        install_requires = ['numpy','netcdf4','scipy','cdo','netcdf4_soft_links'],
        zip_safe=False,
        # other arguments here...
        entry_points = {
                  'console_scripts': [
                           'c_grid_remap= '+package_name+'.interface:c_grid_remap'
                                     ],
                       }
    )

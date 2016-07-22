from __future__ import division, absolute_import, print_function

import click
import netCDF4
import numpy as np
import itertools
#import cdo
import scipy.interpolate as interpolate

import netcdf4_soft_links.netcdf_utils as netcdf_utils
import netcdf4_soft_links.subset_utils as subset_utils

@click.group()
def c_grid_remap():
    return

#default_box=(0.0,360.0,-90.0,90.0)
default_lon='lon'
default_lat='lat'
@click.option('--lat_var',default=default_lat)
@click.option('--lon_var',default=default_lon)
@click.argument('output_file')
@click.argument('input_file')
@c_grid_remap.command()
def vertices(input_file,output_file,lat_var=default_lat,lon_var=default_lon):
    with netCDF4.Dataset(input_file) as dataset:
        with netCDF4.Dataset(output_file,'w') as output:
            netcdf_utils.replicate_full_netcdf_recursive(dataset,output,check_empty=True)
            record_vertices(dataset,output,lat_var,lon_var)
    return

def record_vertices(dataset,output,lat_var,lon_var):
    if set([lat_var,lon_var]).issubset(dataset.variables.keys()):
        lat=dataset.variables[lat_var][:]
        lon=np.mod(dataset.variables[lon_var][:],360.0)
        if subset_utils.check_basic_consistency(dataset,lat_var,lon_var):
            lat_vertices, lon_vertices=subset_utils.get_vertices(dataset,lat_var,lon_var)
            lat_vertices, lon_vertices=subset_utils.sort_vertices_counterclockwise_array(lat_vertices, lon_vertices)
            output.createDimension('nv',size=4)
            lat_tmp=output.createVariable(lat_var+'_vertices','f',dataset.variables[lat_var].dimensions+('nv',))
            lat_tmp[:]=lat_vertices
            lon_tmp=output.createVariable(lon_var+'_vertices','f',dataset.variables[lon_var].dimensions+('nv',))
            lon_tmp[:]=lon_vertices
    return output

if __name__ == '__main__':
    c_grid_remap()

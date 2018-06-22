#!/usr/bin/env python

'''
gsconfig is a python library for manipulating a GeoServer instance via the GeoServer RESTConfig API.

The project is distributed under a MIT License .
'''

__author__ = "David Winslow"
__copyright__ = "Copyright 2012-2015 Boundless, Copyright 2010-2012 OpenPlans"
__license__ = "MIT"

from geoserver.catalog import Catalog
import pdb

pdb.set_trace()
cat = Catalog("http://192.168.99.110:8080/geoserver/rest", "admin", "geoserver")
name = "geogig8"
ds = cat.create_datastore(name)
ds.type = "GeoGig"
ds.connection_parameters.update(
    geogig_repository="/vagrant/dev/.geoserver/data/geogig/geogig6",
    branch="master",
    create="true")

cat.save(ds)
ds = cat.get_store(name)
#components = \
#  dict((ext, "myfile." + ext) for ext in ["shp", "prj", "shx", "dbf"])
#cat.add_data_to_store(ds, "mylayer", components)

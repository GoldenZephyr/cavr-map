#!/usr/bin/python

import numpy as np
from shape_lib import *
import math
from collections import namedtuple
import re

#function for grabbing data from a line of the header
def get_header_data(data):
	ind = data.find("\t")
	data = data[(ind+1):-1]
	return float(data)

#stores all of the header data
def read_header_data(fo):
	Header = namedtuple('Header', 'ncols nrows xllcenter yllcenter cellsize nodata_value')
	col = fo.readline()
	row = fo.readline()
	xll = fo.readline()
	yll = fo.readline()
	cellsize = fo.readline()
	nodata = fo.readline()
    
	ncol = get_header_data(col)
	nrows = get_header_data(row)
	cell_size = get_header_data(cellsize)
	xllcenter = get_header_data(xll)
	yllcenter = get_header_data(yll)
	no_data = get_header_data(nodata)
	head = Header(ncol, nrows, xllcenter, yllcenter, cell_size, no_data)
	return head

#grabs all data between <BEGIN SHAPES> and <END SHAPES> tags
def get_shape_data(fo):
	data = fo.read()	
	ind = data.find("<")
	data = data[(ind+15):]
	ind = data.find("<")
	data = data[:-13]
	return data


#parses the shape information and creates objects for each
def parse_shapes(shapes):
	shape_list = []
	while(shapes.find("\n") != -1):
		ind = shapes.find("\n")
		line = shapes[:ind]
		matches = re.findall("\d+", line)
		matches = map(int, matches)
		if(line.find("rect") != -1):
			if(line.find("3d") != -1):
				shape_list.append(Rectangle3D(*matches))
			else:
				shape_list.append(Rectangle(*matches))
		elif(line.find("ellipse") != -1):
			if(line.find("3d") != -1):
				shape_list.append(Ellipse3D(*matches))
			else:
				shape_list.append(Ellipse(*matches))
		elif(line.find("square") != -1):
			if(line.find("3d") != -1):
				shape_list.append(Square3D(*matches))
			else:
				shape_list.append(Square(*matches))
		elif(line.find("circle") != -1):
			if(line.find("3d") != -1):
				shape_list.append(Circle3D(*matches))
			else:
				shape_list.append(Circle(*matches))
		shapes = shapes[(ind+1):]

	return shape_list



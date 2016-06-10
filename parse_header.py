#!/usr/bin/python

import numpy as np
from shape_lib import *
import math
from collections import namedtuple
#filename = 'test.txt'
#fo = open(filename, 'r+')
#ncol = 0
#nrows = 0
#cell_size = 0
#no_data = 0

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

#write_header_data()
#shapes = get_shape_data()

#function to shorten shape maker code
def read_arg(shape):
	ind = shape.find(",")
	if(ind != -1):
		clip = shape[:ind]
	else:
		ind = shape.find(")")
		clip = shape[:ind]
	return clip
	
def move_string(key, string):
	ind = string.find(key)
	string = string[(ind+1):]
	return string

#uses parse shape information to make shape objects
def rect_maker(shape):
	x = 0
	y = 0
	lx = 0
	ly = 0
	rot = 0

	shape = move_string("(", shape)

	x = int(read_arg(shape))
	shape = move_string(" ", shape)
	
	y = int(read_arg(shape))
	shape = move_string(" ", shape)
	
	lx = int(read_arg(shape))
	shape = move_string(" ", shape)

	ly = int(read_arg(shape))
	shape = move_string(" ", shape)

	rot = math.radians(float(read_arg(shape)))

	rect = Rectangle(x, y, lx, ly, rot)
	return rect

def square_maker(shape):
	x = 0
	y = 0
	l = 0
	rot = 0

	shape = move_string("(",shape)

	x = int(read_arg(shape))
	shape = move_string(" ",shape)
	
	y = int(read_arg(shape))
	shape = move_string(" ",shape)
	
	l = int(read_arg(shape))
	shape = move_string(" ",shape)

	rot = math.radians(float(read_arg(shape)))

	square = Square(x, y, l, rot)
	return square
	

def ellipse_maker(shape):
	x = 0
	y = 0
	lx = 0
	ly = 0
	rot = 0

	shape = move_string("(", shape)

	x = int(read_arg(shape))
	shape = move_string(" ",shape)
	
	y = int(read_arg(shape))
	shape = move_string(" ",shape)
	
	lx = int(read_arg(shape))
	shape = move_string(" ",shape)

	ly = int(read_arg(shape))
	shape = move_string(" ",shape)

	rot = math.radians(float(read_arg(shape)))

	ellipse = Ellipse(x, y, lx, ly, rot)
	return ellipse


def circle_maker(shape):
	x = 0
	y = 0
	l = 0
	rot = 0

	shape = move_string("(", shape)

	x = int(read_arg(shape))
	shape = move_string(" ",shape)
	
	y = int(read_arg(shape))
	shape = move_string(" ",shape)
	
	l = int(read_arg(shape))
	shape = move_string(" ",shape)

	rot = math.radians(float(read_arg(shape)))

	circle = Circle(x, y, l, rot)
	return circle


def rect3d_maker(shape):
	x = 0
	y = 0
	z = 0
	lx = 0
	ly = 0
	lz = 0
	rot = 0

	shape = move_string("(", shape)

	x = int(read_arg(shape))
	shape = move_string(" ",shape)
	
	y = int(read_arg(shape))
	shape = move_string(" ",shape)

	z = int(read_arg(shape))
	shape = move_string(" ",shape)
	
	lx = int(read_arg(shape))
	shape = move_string(" ",shape)

	ly = int(read_arg(shape))
	shape = move_string(" ",shape)

	lz = int(read_arg(shape))
	shape = move_string(" ",shape)

	rot = math.radians(float(read_arg(shape)))

	rect3d = Rectangle3D(x, y, z, lx, ly, lz, rot)
	return rect3d


def square3d_maker(shape):
	x = 0
	y = 0
	z = 0
	l = 0
	rot = 0
	
	shape = move_string("(", shape)

	x = int(read_arg(shape))
	shape = move_string(" ",shape)
	
	y = int(read_arg(shape))
	shape = move_string(" ",shape)
	
	z = int(read_arg(shape))
	shape = move_string(" ",shape)

	l = int(read_arg(shape))
	shape = move_string(" ",shape)

	rot = math.radians(float(read_arg(shape)))

	square3d = Square3D(x, y, z, l, rot)
	return square3d

def ellipse3d_maker(shape):
	x = 0
	y = 0
	z = 0
	lx = 0
	ly = 0
	lz = 0
	rot = 0
	
	shape = move_string("(", shape)

	x = int(read_arg(shape))
	shape = move_string(" ",shape)
	
	y = int(read_arg(shape))
	shape = move_string(" ",shape)

	z = int(read_arg(shape))
	shape = move_string(" ",shape)

	lx = int(read_arg(shape))
	shape = move_string(" ",shape)

	ly = int(read_arg(shape))
	shape = move_string(" ",shape)

	lz = int(read_arg(shape))
	shape = move_string(" ",shape)

	rot = math.radians(float(read_arg(shape)))

	ellipse3d = Ellipse3D(x, y, z, lx, ly, lz, rot)
	return ellipse3d


def circle3d_maker(shape):
	x = 0
	y = 0
	z = 0
	l = 0
	rot = 0

	shape = move_string("(", shape)

	x = int(read_arg(shape))
	shape = move_string(" ", shape)
	
	y = int(read_arg(shape))
	shape = move_string(" ",shape)
	
	z = int(read_arg(shape))
	shape = move_string(" ",shape)

	l = int(read_arg(shape))
	shape = move_string(" ",shape)

	rot = math.radians(float(read_arg(shape)))

	circle3d = Circle3D(x, y, z, l, rot)
	return circle3d

#parses the shape information and creates objects for each
def parse_shapes(shapes):
	shape_list = []
	while(shapes.find("\n") != -1):
		ind = shapes.find("\n")
		line = shapes[:ind]
		if(line.find("rect") != -1):
			if(line.find("3d") != -1):
				shape_list.append(rect3d_maker(line))
			else:
				shape_list.append(rect_maker(line))
		elif(line.find("ellipse") != -1):
			if(line.find("3d") != -1):
				shape_list.append(ellipse3d_maker(line))
			else:
				shape_list.append(ellipse_maker(line))
		elif(line.find("square") != -1):
			if(line.find("3d") != -1):
				shape_list.append(square3d_maker(line))
			else:
				shape_list.append(square_maker(line))
		elif(line.find("circle") != -1):
			if(line.find("3d") != -1):
				shape_list.append(circle3d_maker(line))
			else:
				shape_list.append(circle_maker(line))
		shapes = shapes[(ind+1):]

	return shape_list


#print parse_shapes(shapes)

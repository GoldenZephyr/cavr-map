#!/usr/bin/env python
import numpy as np 
from collections import namedtuple 
import math
from math import ceil
from shape_lib import *
from parse_header import *
import argparse

Point = namedtuple('Point', 'x y')

def write2file(fn, header, arr):
	fo = open(fn, 'w')
	fo.write('ncols	%d\n' % header.ncols)
	fo.write('nrows	%d\n' % header.nrows)
	fo.write('xllcenter	%f\n' % header.xllcenter)
	fo.write('yllcenter 	%f\n' % header.yllcenter)
	fo.write('cellsize	%f\n' % header.cellsize)
	fo.write('nodata_value	%d\n' % header.nodata_value)

	# This loop write the contents of arr to the output text file.
	# The output is a grid of numbers separated by spaces
	for ii in xrange(len(arr)):
		fo.writelines(map(lambda x: str(x) + ' ', arr[ii]))
		fo.write('\n')
	fo.close()

def add_to_array(shape, array):
	"""Adds the shape to the map array. """

	shape.dx = shape.dx - 1 
	shape.dy = shape.dy - 1
# When the object is inserted into the array map, it gets padded by 1 cell on each side. Therefore, to be consistent with the input shape size, we need to compensate by subtracting one here.

	# Makes a list of all the integer x coordinates in the shape
	# Ensures that all coordinates are positive
	x_coords = range(max(int(round(shape.x - shape.dx)), 1), int(round(shape.x + shape.dx + 1)))
	y_coords = range(max(int(round(shape.y - shape.dy)), 1), int(round(shape.y + shape.dy + 1)))

	for x in x_coords:
		for y in y_coords:
			cpoint = Point(x - shape.x, y - shape.y)
			cp1 = local_rotate(cpoint, shape.rot) # c', i.e. after rotation
			cp2 = Point(int(round(cp1.x + shape.x)), int(round(cp1.y + shape.y))) # c'', i.e. after rotation and translation

			num = 15 
			array[cp2.x][cp2.y] = num
			# The rounding causes some points on the interior of the shape to be considered empty, so we fill in not only the point, but the neighbor points in the 4 cardinal directions
			array[cp2.x + 1][cp2.y] = num
			array[cp2.x][cp2.y + 1] = num
			array[cp2.x - 1][cp2.y] = num
			array[cp2.x][cp2.y - 1] = num	

def local_rotate(pt, rot):
	"""Rotates the point pt by the specified amount around the origin"""
	pt_arr = np.array([[pt.x],[pt.y]])
	rot_arr = np.array([[math.cos(rot), -math.sin(rot)],[math.sin(rot), math.cos(rot)]])
	out_arr = rot_arr.dot(pt_arr)
	return Point(out_arr[0][0], out_arr[1][0])

def add_shapes(shape_list, arr):
	"""Adds the list of shapes shape_list to the array arr. """
	for shape in shape_list:
		add_to_array(shape,arr)


def parse_input_body(fo):
	shapes_txt = get_shape_data(fo)
	shapes_list = parse_shapes(shapes_txt)
	return shapes_list


if __name__ == '__main__':
#	base_matrix = np.ones((20,20))  - 10000
#	rect1 = Rectangle(10, 10, 5, 5, 0)
#	add_to_array(rect1, base_matrix)
#	fn = open('testout.txt', 'w')
#	write2file(fn, base_matrix)
	parser = argparse.ArgumentParser(description='Generate ascii map from input file')
	parser.add_argument('--input', dest='input_name', help='Name of the input text file. Defaults to input.txt')
	parser.add_argument('--output', dest='output_name', help='Name of the output .asc file. Defaults to output.asc')
	args = parser.parse_args()
	input_name = args.input_name
	if not input_name:
		input_name = 'input.txt'
	output_name = args.output_name
	if not output_name:
		output_name = 'output.asc'	
	fo = open(input_name, 'a+rw')
	head = read_header_data(fo)

	base_matrix = np.ones((head.nrows, head.ncols - 1)) - 1
	# NOTE: the head.ncols - 1 is to fix an off by one error in map_prior.py, and needs  to be removed when that script gets fixed

	shapes_list = parse_input_body(fo)
	add_shapes(shapes_list, base_matrix)
	write2file(output_name, head, base_matrix)
# TODO: Add ability to add shapes to existing ascii input
# TODO: Set the depth based on SOMETHING
# TODO: Add ellipse
# TODO: Add 3d ellipses
# TODO: Make the parsing more robust (recognize spaces in addition to tabs)

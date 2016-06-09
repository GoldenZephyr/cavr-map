#!/usr/bin/env python
import numpy as np 
from collections import namedtuple 
import math
from math import ceil
from shape_lib import *
from parse_header import *

Point = namedtuple('Point', 'x y')

def write2file(fn, arr):
	for ii in xrange(len(arr)):
		fn.writelines(map(lambda x: str(int(x)) + ' ', arr[ii]))
		fn.write('\n')
	fn.close()

def add_to_array(shape, array):
	"""Adds the shape to the map array. """

	shape.dx = shape.dx - 1 
	shape.dy = shape.dy - 1
# When the object is inserted into the array map, it gets padded by 1 cell on each side. Therefore, to be consistent with the input shape size, we need to compensate by subtracting one here.

	# Makes a list of all the integer x coordinates in the shape
	x_coords = range(int(round(shape.x - shape.dx)), int(round(shape.x + shape.dx + 1)))
	y_coords = range(int(round(shape.y - shape.dy)), int(round(shape.y + shape.dy + 1)))

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


def parse_input_file(fn):
	fo = open(fn, 'r+')
	shapes_txt = get_shape_data(fo)
	shapes_list = parse_shapes(shapes_txt)
	return shapes_list


if __name__ == '__main__':
#	base_matrix = np.ones((20,20))  - 10000
#	rect1 = Rectangle(10, 10, 5, 5, 0)
#	add_to_array(rect1, base_matrix)
#	fn = open('testout.txt', 'w')
#	write2file(fn, base_matrix)
	base_matrix = np.ones((50,50)) - 10000
	file_name = 'atest_in.txt'
	shapes_list = parse_input_file(file_name)
	add_shapes(shapes_list, base_matrix)
	fn = open('testout.txt','w')
	write2file(fn, base_matrix)
# TODO: Need to add command line argument support for the input and output file names
# TODO: Need write the header into the file as well
# TODO: Fix behavior of negative numbers inserted into matrix (e.g. a square centered at 0,0)
# TODO: Add ellipse
# TODO: Add 3d ellipses
# TODO: Set the depth based on SOMETHING

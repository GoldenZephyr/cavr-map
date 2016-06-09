#!/usr/bin/python

import numpy as np

filename = 'test.txt'
fo = open(filename, 'r+')

def getHeaderData(data):
    ind = data.find("\t")
    data = data[(ind+1):-1]
    return float(data)

def writeHeaderData():
    col = fo.readline()
    row = fo.readline()
    cellsize = fo.readline()
    nodata = fo.readline()

    fn = open('test_new.txt', 'w')

    fn.write(str(getHeaderData(col)) + "\n")
    fn.write(str(getHeaderData(row)) + "\n")
    fn.write(str(getHeaderData(cellsize)) + "\n")
    fn.write(str(getHeaderData(nodata)) + "\n")

def getShapeData():
    data = fo.read()
    ind = data.find("<")
    data = data[(ind+15):]
    ind = data.find("<")
    data = data[:-13]
    fn = open('shape_data.txt', 'w')
    fn.write(data)

writeHeaderData()
getShapeData()

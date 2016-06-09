#!/usr/bin/python

import numpy as np

def getHeaderData(data):
    ind = data.find("\t")
    data = data[(ind+1):-1]
    return float(data)

filename = 'test.txt'

fo = open(filename, 'r+')

col = fo.readline()
row = fo.readline()
cellsize = fo.readline()
nodata = fo.readline()

fn = open('test_new.txt', 'w')

fn.write(str(getHeaderData(col)) + "\n")
fn.write(str(getHeaderData(row)) + "\n")
fn.write(str(getHeaderData(cellsize)) + "\n")
fn.write(str(getHeaderData(nodata)) + "\n")



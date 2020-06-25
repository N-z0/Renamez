#!/usr/bin/env python3
#coding: utf-8
### 1st line allows to execute this script by typing only its name in terminal, with no need to precede it with the python command
### 2nd line declaring source code charset should be not necessary but for exemple pydoc request it



__doc__ = "This module concern arcs ellipses circles."#information describing the purpose of this module
__status__ = "Development"#should be one of 'Prototype' 'Development' 'Production' 'Deprecated' 'Release'
__version__ = "2.0.0"# version number,date or about last modification made compared to the previous version
__license__ = "public domain"# ref to an official existing License
#__copyright__ = "Copyright 2000, The X Project"
__date__ = "2016"#started creation date / year month day
__author__ = "N-zo syslog@laposte.net"#the creator origin of this prog,
__maintainer__ = "Nzo"#person who curently makes improvements, replacing the author
__credits__ = []#passed mainteners and any other helpers
__contact__ = "syslog@laposte.net"# current contact adress for more info about this file



### import the required modules
from math import sin,cos,pi



def get_arc_polygon(resolution,size=[1,1],arc=[0,1]):
	"""resolution is the quantity of polygon points
	horizontal and vertical size are requested
	arc give the starting and ending angles"""
	polygon=[]
	for increment in range(resolution+1):
		inc= arc[1]*(increment/resolution)
		angl=(arc[0]+inc)*pi*2
		polygon.append( (size[0]*sin(angl),size[1]*cos(angl)) )
	return polygon


def get_ellipse_polygon(resolution,size=[1,1]):
	"""resolution is the quantity of polygon points
	horizontal and vertical size are requested"""
	polygon=[]
	for increment in range(resolution):
		angl= pi*2*(increment/resolution)
		polygon.append( (size[0]*sin(angl),size[1]*cos(angl)) )
	return polygon


def get_circle_polygon(resolution,size=1):
	"""resolution is the quantity of polygon points
	and size of circle is optional"""
	polygon=[]
	for increment in range(resolution):
		angl= pi*2*(increment/resolution)
		polygon.append( (size*sin(angl),size*cos(angl)) )
	return polygon

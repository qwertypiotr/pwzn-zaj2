# -*- coding: utf-8 -*-


def xrange(start_stop, stop=None, step=None):
	"""
	Funkcja która działa jak funkcja range (wbudowana i z poprzednich zajęć)
	która działa dla liczb całkowitych.
	"""
	if step==None:
		if stop==None:
			stop=start_stop
			start_stop=0
			step=1
		else:
			step=1
			
			
	while start_stop<stop:
		yield start_stop
		start_stop+=step
	

xrange(2,9,2)


		

# -*- coding: utf-8 -*-

from math import *

b = [-1, -1, -1] # point first
a = [1, -1, -1] 
c = [1, 1, -1]

def vector (point_1, point_2):
	comp_x = point_2[0] - point_1[0]
	comp_y = point_2[1] - point_1[1]
	comp_z = point_2[2] - point_1[2]

	vector = [comp_x, comp_y, comp_z]
	return vector

print vector(b,a)

print vector(a,c)

def mult_vector(vector_a, vector_b):
	
	result_x = vector_a[1]*vector_b[2] - vector_a[2]*vector_b[1]
	result_y = vector_a[2]*vector_b[0] - vector_a[0]*vector_b[2]
	result_z = vector_a[0]*vector_b[1] - vector_a[1]*vector_b[0]

	result = [result_x, result_y, result_z]
	return result

def normalize(sl_vector):
	length = sqrt((sl_vector[0]*sl_vector[0])+(sl_vector[1]*sl_vector[1])+(sl_vector[2]*sl_vector[2]))

	try:
		result_x = sl_vector[0]/length
		result_y = sl_vector[1]/length
		result_z = sl_vector[2]/length

		result_vector = [result_x, result_y, result_z]
		return result_vector
	except:
		"Erro na hora de dividir para compor o vetor unitário"

def calc_normal(point_one, point_two, point_three):
	vector_one = vector(point_one, point_two)
	vector_two = vector(point_two, point_three)
	result = mult_vector(vector_two,vector_one)
	result = normalize(result)
	return result

def main():
	#test = mult_vector(vector(a,c),vector(b,a))	
	#print normalize(test)
	print calc_normal(b,a,c)

if __name__ == "__main__":
	main()


#print mult_vector(vector(b,a),vector(a,c))

#print mult_vector(vector(a,c),vector(b,a))
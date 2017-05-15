from glut_loader import *
from matrix_opengl import *

def pairs(faces):
	array = []
	for i in faces:
		
		index_i = faces.index(i)
		for j in faces:
			
			index_j = faces.index(j)
			if i!=j:
				#break
				a = compare(i,j)
				
			#print (index_i,index_j)
				if len(a)==2:
					c = (index_i,index_j)
					array.append(c)
	return array

def make_graph(faces):
	graph={}
	for i in range(len(faces)):
		graph[i] = []
	list = pairs(faces)
	for i in list:
		# i = (0,1)
		i1 = i[0]
		i2 = i[1]			
		graph[i1].append(i2)
	return graph
	



def main():
	#results= loader('icosahedron.ply')
	results= loader('dodecahedron.ply')
	faces = results[3]
	r = make_graph(faces)
	#r =pairs(faces)
	print r


if __name__ =='__main__':
	main()

from glut_loader import *

results = loader('cube.ply')
number_of_vertex = results[0]
number_of_faces = results[1]
number_of_faces = int(number_of_faces)
vertex=results[2]
faces=results[3]
#print number_of_faces
#print faces

def create_graph(n_instance,f):
	graph = {}
	i=0
	while(i<n_instance):
		graph[i]=faces[i]
		#print i
		#print faces[i]
		i+=1
	print graph

create_graph(number_of_faces,faces)
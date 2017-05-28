from glut_loader import *
#from main import *
from make_graph import *

#results = loader('cube.ply')
#results = loader('tetrahedron.ply')
results = loader('octahedron.ply')
number_of_vertex = results[0]
number_of_faces = results[1]
vertex=results[2]
faces=results[3]

graph_cube = {0 : [2,3,4,5],
		 1 : [2,3,4,5],
		 2 : [0,1,4,5],
		 3 : [0,1,4,5],
		 4 : [0,1,2,3],
		 5 : [0,1,2,3],
		}

graph_tetrahedron = {0: [1,2,3],
		1: [0,2,3],
		2: [0,1,3],
		3: [0,1,2]
		}

graph_octahedron = {0: [1,3,4],
		1: [0,2,5],
		2: [1,3,6],
		3: [0,2,7],
		4: [0,5,7],
		5: [1,4,6],
		6: [2,5,7],
		7: [3,4,6],
		}

graph_icosahedron = make_graph(faces)

def dfs_iter(graph, root):
	visited = []
	stack =[root,]
	#pai = None
	while stack:
		
			
		node = stack.pop()
		#print (pai,node)

		if node not in visited:
			visited.append(node)
			for x in graph[node]:
				if x not in visited:
					stack.append(x)
			#stack.extend([x for x in graph[node] if x not in visited])
		
		#print visited
		print node
		print stack	
	return visited

edges =[]
def dfs(graph,root,visited=None):

	if visited is None:
		visited=[]
	
	if root in visited:
		return
	visited.append(root)
	
	for x in graph[root]:

		if x not in visited:
			edge = (root,x)
			edges.append(edge)
			#print edge
			dfs(graph,x,visited)
	#print visited
	#print edges

	return visited,edges


def create_face_vector(vector_of_faces,dfs_result):
	face_vector_result=[]
	for i in dfs_result:
		face_vector_result.append(vector_of_faces[i])
	return face_vector_result


def depht_fs(graph,root):
	global edges
	edges =[]
	r = dfs(graph,root)
	return r
#for i in [0,1,2,3,4,5]:
	#print depht_fs(graph_cube,i)

r = depht_fs(graph_cube,3)

#result= create_face_vector(faces,r[0])
#print result
#print a
#for i in a:
#	print faces[i]
#print compare(faces[3],faces[5])

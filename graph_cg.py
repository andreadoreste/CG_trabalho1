from glut_loader import *
from make_graph import *

#Depth First Search
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
			dfs(graph,x,visited)

	return visited,edges


def create_face_vector(vector_of_faces,dfs_result):
	face_vector_result=[]
	for i in dfs_result:
		face_vector_result.append(vector_of_faces[i])
	return face_vector_result

#Depth First Search
def depht_fs(graph,root):
	global edges
	edges =[]
	r = dfs(graph,root)
	return r

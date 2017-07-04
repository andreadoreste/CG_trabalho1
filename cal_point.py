from numpy import transpose
from geometry import Point, Polygon
	

#This function find the points from the a specified matrix	
def calc_vertex(matrix,point):
	px = point[0]
	py = point[1]
	pz = point[2]

	xp = matrix[0][0]*px + matrix[0][1]*py + matrix[0][2]*pz + matrix[0][3]
	yp = matrix[1][0]*px + matrix[1][1]*py + matrix[1][2]*pz + matrix[1][3]
	zp = matrix[2][0]*px + matrix[2][1]*py + matrix[2][2]*pz + matrix[2][3]
	wp = matrix[3][0]*px + matrix[3][1]*py + matrix[3][2]*pz + matrix[3][3]
	
	xp = xp/wp
	yp = yp/wp
	zp = zp/wp

	return [xp,yp,zp]

def calc_all_vertex(vertex,faces,tr_matrix):
	#new_vertex_faces will be something like [polygon1,polygon2,polygon3,...,polygonN]
	new_vertex_faces = []
	
	size = len(faces)
	
	#faces will be something like [[0,1,2,3],[5,4,7,6]]
	for f in faces:
		#f something like [0,1,2,3]
		fp = []
		f_index = faces.index(f)
		
		for v in f:
		
			tr_matrix_i = tr_matrix[f_index]
			#it's necessary transpose the matrix
			tr_matrix_i = tr_matrix_i.transpose()
			tr_matrix_i = tr_matrix_i.tolist()
			#new_vertex is new vertex coordinates with transformations 
			new_vertex=calc_vertex(tr_matrix_i,vertex[v])
				
			p = Point(new_vertex[0],new_vertex[1],new_vertex[2])
			fp.append(p)
			
		face = Polygon(fp)
		new_vertex_faces.append(face)
	return new_vertex_faces

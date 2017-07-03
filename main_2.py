from numpy import *
#from geometry import *
#from matrix import *
#import matrix as c_matrix

from normal_vector import *
from glut_loader import *
from matrix_opengl import *
from graph_cg import *
from geometry import *

global colors
colors = [(0.0,1.0,0.0,1.0),(0.0,0.0,1.0,1.0),(0.0,1.0,1.0,1.0),(1.0,1.0,1.0,1.0), 
            (1.0,1.0,0.0,1.0),(1.0,0.0,0.0,1.0),(1.000, 0.412, 0.706,1.0),(1.000, 0.388, 0.278, 1.0), 
            (0.780, 0.082, 0.522, 1.0),(1.000, 0.647, 0.000, 1.0),(1.000, 0.855, 0.725, 1.0),(0.902, 0.902, 0.980, 1.0),
            (0.282, 0.239, 0.545, 1.0),(0.498, 1.000, 0.000, 1.0),(0.957, 0.643, 0.376, 1.0),(1.000, 0.753, 0.796, 1.0),
            (0.000, 0.980, 0.604, 1.0), (0.000, 0.000, 0.502, 1.0), (0.961, 0.961, 0.863,1.0), (0.753, 0.753, 0.753,1.0)]


def opened_cube(vertex,faces,initial_face, ang=90):
    
    graph = make_graph(faces)

    ##print graph

    n_faces =len(faces)
    

    #<DFS>

    #depth_fs returns an array
    #depth_fs[0] -> path 
    #depth_fs[1] -> neighbors
    DFS = depht_fs(graph,initial_face)
    #DFS = depht_fs(graph_octahedron,initial_face)
    #faces vertex from the DFS path
    path = DFS[0]
    print path
    DFS_faces_vector = create_face_vector(faces,path)
    dfs_parents = DFS[1]
    #</DFS>

    #Create an array with an identity matrix for each face
    faces_matrix = []
    for i in range(n_faces):
        faces_matrix.append(matrix(identity(4)))

    #Start drawing the faces
    face_i = path[0]    
    for face in DFS_faces_vector:
        
        glPushMatrix()  
        
        index = DFS_faces_vector.index(face)
        it = faces.index(face)
        glColor4fv(colors[it])

        #Doesn't need to apply any transformations at the first face
        if face!=DFS_faces_vector[0]:
            #print 'vertex',len(vertex)
            #print vertex 
            #Array pair = [face n-1, face n]
            pair = dfs_parents.pop(0)
            #print 'pair',pair
            #face being modificated
            face_i = pair[1]
            face_prev = pair[0]
            #Array f1,f2 = faces[n]=[p1, p2, p3, p4]
            # Each p is a vertex of the face    
            f1 = faces[pair[0]] #face 1
            f2 = faces[pair[1]] #face 2

            #Calculate the normal array
            #point_x1 returns a array with the coordinates like [-1,1,1]
            point_a1 = vertex[f1[0]]

            # From a Array to a Point object
            #point_a1 = Point(point_a1[0],point_a1[1],point_a1[2])

            point_b1 = vertex[f1[1]]
            #point_b1 = Point(point_b1[0],point_b1[1],point_b1[2])

            point_c1 = vertex[f1[2]]
            #point_c1 = Point(point_c1[0],point_c1[1],point_c1[2])

            normal_vec_face_anterior = calc_normal(point_a1,point_b1,point_c1)
            ##print normal_vec_face_anterior

            point_a2 = vertex[f2[0]]
            #point_a2 = Point(point_a2[0],point_a2[1],point_a2[2])

            point_b2 = vertex[f2[1]]
            #point_b2 = Point(point_b2[0],point_b2[1],point_b2[2])

            point_c2 = vertex[f2[2]]
            #point_c2 = Point(point_c2[0],point_c2[1],point_c2[2])

            normal_vec_face_atual = calc_normal(point_a2,point_b2,point_c2)
            ##print normal_vec_face_atual

            cross_product = cross(normal_vec_face_atual,normal_vec_face_anterior)
            cross_product= cross_product.tolist()
            #print 'cross product',cross_product
            dot_product = dot(normal_vec_face_atual, normal_vec_face_anterior)
            
            #Find the angle
            angle = arccos(dot_product)
            angle = angle*180/pi
            
            #Finding the edge
            edge = compare(f1,f2)
            
            point_1 = edge[0]
            point_1 = vertex[point_1]
            #print 'point_1',point_1
            tr = translateAndRotate(angle,point_1,cross_product)            
            tr = matrix(tr)
            
            comb = tr*faces_matrix[face_prev]
            
            faces_matrix[face_i] = comb
            glMultMatrixf(comb.view(type=ndarray))
                    
        
        #desenha
        
        glPushMatrix()
        glBegin(GL_POLYGON)

        for vert in face:
            #That's the place for Texture Coordinates 
            glVertex3fv(vertex[vert])
            
        glEnd()
        glPopMatrix()
        #m = glGetDoublev(GL_MODELVIEW_MATRIX)
        #m = matrix(m)
        #print 'm'
        #print m
        
        glPopMatrix()
    
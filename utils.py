import numpy as np

def getPerspectiveTransform(view1_4_pts, view2_4_pts):
    '''
    source https://math.stackexchange.com/questions/494238/how-to-compute-homography-matrix-h-from-corresponding-points-2d-2d-planar-homog
    '''
    # loop through the 4 correspondences and create assemble matrix
    a_list = []
    for i in range(4):
        p1 = np.matrix([view1_4_pts[i][0,0], view1_4_pts[i][0,1], 1])
        p2 = np.matrix([view2_4_pts[i][0,0], view2_4_pts[i][0,1], 1])

        a2 = [0, 0, 0, -p2.item(2) * p1.item(0), -p2.item(2) * p1.item(1), -p2.item(2) * p1.item(2),
              p2.item(1) * p1.item(0), p2.item(1) * p1.item(1), p2.item(1) * p1.item(2)]
        a1 = [-p2.item(2) * p1.item(0), -p2.item(2) * p1.item(1), -p2.item(2) * p1.item(2), 0, 0, 0,
              p2.item(0) * p1.item(0), p2.item(0) * p1.item(1), p2.item(0) * p1.item(2)]
			  
        a_list.append(a1)
        a_list.append(a2)

    matrix_A = np.matrix(a_list)

    # svd decomposition
    u, s, v = np.linalg.svd(matrix_A)

    # reshape the min singular value into 3x3 matrix
    h = np.reshape(v[8], (3, 3))

    # normalize h
    h = (1/h.item(8)) * h
    return h
'''
Matrix forms

K (intrensic camera_matrix)= 
[fx   0   cx]
[0    fy  cy]
[0    0   1 ]

D (distortion coeffs)= [k1,k2,p1,p2,k2,...,kn]

R (rotation matrix)=
[nx  ox  ax]
[ny  oy  ay]
[nz  oz  az]

P (projection matrix)=
[f   0   cx   T*f]
[0   f   cy   0  ]
[0   0   1    0  ]

Q (reprojection matrix)*=
[1   0   0      -cx       ]
[0   1   0      -cy       ]
[0   0   0       f        ]
[0   0   -1/T   (cx-cx')/T]

*: use princeple camera values typacly left
*: term Q44 can be replaced as a simplification with 0 by assuming cx=cx'

'''
import numpy as np

CAMERA_HEIGHT=720
CAMERA_WIDTH=2560


f=676.943238
cx=647.788349
cx_prim=648.575478
cy=353.827153
T=-42.808641/f

Q =np.array([
[1,   0,   0,      -cx       ],
[0,   1,   0,      -cy       ],
[0,   0,   0,       f        ],
[0,   0,   -1/T,   (cx-cx_prim)/T]])


# Left Camera
KL =[
703.450011, 0,          647.788349,
0,          703.626116, 353.827153,
0,          0,          1]

DL = [-0.170735, 0.026153, 0.000810, -0.000514, 0.000000]

RL = [
0.999982,  0.000481, 0.006001,
-0.000471, 0.999999, -0.001531,
-0.006001, 0.001528, 0.999981]

PL = [
676.943238, 0.000000,   648.575478, 0.000000,
0.000000,   676.943238, 358.418819, 0.000000,
0.000000,   0.000000,   1.000000,   0.000000]

# Right Camera
KR = [
705.680682, 0, 652.477770,
0, 704.822725, 360.825493,
0, 0, 1]

DR = [-0.171433, 0.026730, 0.000742, -0.000105, 0.000000]

RR = [
0.999994, -0.000133, 0.003443,
0.000127, 0.999999, 0.001531,
-0.003443, -0.001530, 0.999993]

PR = [
676.943238, 0.000000, 648.575478, -42.808641,
0.000000, 676.943238, 358.418819, 0.000000,
0.000000, 0.000000, 1.000000, 0.000000]


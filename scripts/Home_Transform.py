from sympy import *
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

init_printing(use_unicode=False, wrap_line=False)

##------------------------Variable Definitions------------------------##

#D-H Parameters
alpha, a, d, th = symbols('alpha a d theta')

#Symbolic Joint Variables for UR10
th1, th2, th3, th4, th5, th6 = symbols('th1 th2 th3 th4 th5 th6')


#Defining Parameters as found in Report in Arrays
alpha_array = [0, pi/2, 0, -pi/2, pi/2, 0]
theta_array = [th1, th2, th3, th4, th5, th6]
d_array = [0.085, 0.187, 0, 0, 0.363, 0]
a_array = [0, 0, 0.350, 0, 0, .15175]

##------------Transformation Matrices Definitions--------------------##

Rz = Matrix([[cos(th), -sin(th), 0, 0],
             [sin(th),  cos(th), 0, 0],
             [      0,        0, 1, 0],
             [      0,        0, 0, 1]])

Tz = Matrix([[  1,  0,  0,  0],
             [  0,  1,  0,  0],
             [  0,  0,  1,  d],
             [  0,  0,  0,  1]])

Tx = Matrix([[  1,  0,  0,  a],
             [  0,  1,  0,  0],
             [  0,  0,  1,  0],
             [  0,  0,  0,  1]])

Rx = Matrix([[  1,        0,        0,  0],
             [  0,  cos(alpha), -sin(alpha),  0],
             [  0,  sin(alpha),  cos(alpha),  0],
             [  0,        0,        0,  1]])

##------------Computing Each Row's Transformation Matrix--------------##
T1 = Rz*Tz*Tx*Rx
T2 = Rz*Tz*Tx*Rx
T3 = Rz*Tz*Tx*Rx
T4 = Rz*Tz*Tx*Rx
T5 = Rz*Tz*Tx*Rx
T6= Rz*Tz*Tx*Rx

#Substituting Params into Each Transformation Matrix
T1 = T1.subs(alpha, alpha_array[0]).subs(th, theta_array[0]).subs(d, d_array[0]).subs(a, a_array[0])
T2 = T2.subs(alpha, alpha_array[1]).subs(th, theta_array[1]).subs(d, d_array[1]).subs(a, a_array[1])
T3 = T3.subs(alpha, alpha_array[2]).subs(th, theta_array[2]).subs(d, d_array[2]).subs(a, a_array[2])
T4 = T4.subs(alpha, alpha_array[3]).subs(th, theta_array[3]).subs(d, d_array[3]).subs(a, a_array[3])
T5 = T5.subs(alpha, alpha_array[4]).subs(th, theta_array[4]).subs(d, d_array[4]).subs(a, a_array[4])
T6 = T6.subs(alpha, alpha_array[5]).subs(th, theta_array[5]).subs(d, d_array[5]).subs(a, a_array[5])

##----------Defining Transformation Matrices wrt Zero Frame-----------##
H0_1 = T1
H0_2 = T1*T2
H0_3 = T1*T2*T3
H0_4 = T1*T2*T3*T4
H0_5 = T1*T2*T3*T4*T5
H0_6 = T1*T2*T3*T4*T5*T6

pprint(H0_6)


Home_Transform = H0_6.evalf(5, subs = {th1 :0, th2 :0, th3 : 0, th4 : 0, th5 : 0, th6 : 0})

pprint(Home_Transform)

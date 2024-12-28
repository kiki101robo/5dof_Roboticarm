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

##----------------------Extracting P from H0_6------------------------##
P = Matrix([[H0_6[3]], [H0_6[7]], [H0_6[11]]])

##-----------Computing General Form of Partial Derivatives------------##

Par1 = diff(P, th1)
Par2 = diff(P, th2)
Par3 = diff(P, th3)
Par4 = diff(P, th4)
Par5 = diff(P, th5)
Par6 = diff(P, th6)

##-----------------Extracting Z from each H Matrix--------------------##
Z0_1 = Matrix([[H0_1[2]], [H0_1[6]], [H0_1[10]]])
Z0_2 = Matrix([[H0_2[2]], [H0_2[6]], [H0_2[10]]])
Z0_3 = Matrix([[H0_3[2]], [H0_3[6]], [H0_3[10]]])
Z0_4 = Matrix([[H0_4[2]], [H0_4[6]], [H0_4[10]]])
Z0_5 = Matrix([[H0_5[2]], [H0_5[6]], [H0_5[10]]])
Z0_6 = Matrix([[H0_6[2]], [H0_6[6]], [H0_6[10]]])

##-------------------Forming Jacobian Matrix---------------------##

#Components
J1 = Matrix([[Par1], [Z0_1]])
J2 = Matrix([[Par2], [Z0_2]])
J3 = Matrix([[Par3], [Z0_3]])
J4 = Matrix([[Par4], [Z0_4]])
J5 = Matrix([[Par5], [Z0_5]])
J6 = Matrix([[Par6], [Z0_6]])

#Full Jacobian
J = Matrix([[J1, J2, J3, J4, J5, J6]])
J_initial = J.evalf(5, subs = {th1 :0, th2 :0, th3 : 0, th4 : 0, th5 : 0, th6 : 0})
print("J :")
pprint(J)
pprint(J_initial)

##-------------------Plotting the Circle Code---------------------##
r=0.10

#Defining my initial joint angles.
q1 = 0.0002
q2 = 0.0001
q3 = -0.0001
q4 = 0.0001
q5 = 0.0004
q6 = 0.0000

q1_values = []
q2_values = []
q3_values = []
q4_values = []
q5_values = []
q6_values = []

#Plotting variables
X = []
Y =[]
Z =[]

time = np.linspace(0, 20, num=20)
dt = 20 / 200
for t in time:
    #Define components of X_Dot
    Vx = ((2*pi*r)/20)*cos((2*pi*t)/20)
    Vy = 0.0
    Vz = -((2*pi*r)/20)*sin((2*pi*t)/20)
    omega_x = 0.0
    omega_y = 0.0
    omega_z = 0.0

    #Formulate X_Dot
    X_dot = Matrix([[Vx], [Vy], [Vz], [omega_x], [omega_y], [omega_z]])

    #Substitude Joint Angles Jacobian Matrix
    J_Applied = J.subs({th1: q1, th2: q2, th3: q3, th4: q4, th5: q5, th6: q6})

    #Calculate q_dot
    q_dot = (J_Applied.inv() * X_dot).evalf()

    #Extracting Elements of q_dot
    q1_dot = q_dot[0]
    q2_dot = q_dot[1]
    q3_dot = q_dot[2]
    q4_dot = q_dot[3]
    q5_dot = q_dot[4]
    q6_dot = q_dot[5]

    #Numerical Integration of Each Joint Angle
    q1 = q1 + q1_dot * dt
    q2 = q2 + q2_dot * dt
    q3 = q3 + q3_dot * dt
    q4 = q4 + q4_dot * dt
    q5 = q5 + q5_dot * dt
    q6 = q6 + q6_dot * dt

    q1_values.append(q1)
    q2_values.append(q2)
    q3_values.append(q3)
    q4_values.append(q4)
    q5_values.append(q5)
    q6_values.append(q6)

    #Substitude Joint Angles into Final Transformation Matrix
    H0_6_Applied = H0_6.subs({th1: q1, th2: q2, th3: q3, th4: q4, th5: q5, th6: q6})

    # #Saving For Plotting
    X.append(H0_6_Applied[3])
    Y.append(H0_6_Applied[7])
    Z.append(H0_6_Applied[11])
print("q1")
print(q1_values)
print("q2")
print(q2_values)
print("q3")
print(q3_values)
print("q4")
print(q4_values)
print("q5")
print(q5_values)
print("q6")
print(q6_values)

plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 3D Plot (X, Y, Z)
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(X, Y, Z, marker='o')
ax1.set_xlabel('X (mm)')
ax1.set_ylabel('Y (mm)')
ax1.set_zlabel('Z (mm)')
ax1.set_title('Trajectory of End-Effector in 3D')

# 2D Plot (X, Z)
ax2.scatter(X, Z, marker='o')
ax2.set_xlabel('X (mm)')
ax2.set_ylabel('Z (mm)')
ax2.set_title('Trajectory of End-Effector in X-Z plane')

plt.tight_layout()
plt.show()

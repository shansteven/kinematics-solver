# kinematics-solver
Program to automatically solve a kinematics problem using a known system of equations.

Quantity | Variable
v | Initial Velocity
f | Final Velocity
a | Acceleration
t | Time
x | Displacement

Equations:
* f = v+a*t
* x = v*t+(a*t^2)/2
* v = f-a*t
* t = (f-v)/a
* a = (f-v)/t
* t = (sqrt(2*a*x+v^2)-v)/a
* x = ((f+v)/2)*t
* t = (2*x)/(f+v)
* f = (2*x)/t-v
* v = (2*x)/t-f
* v = (x-(a*t^2)/2)/t
* a = (2*x-2*v*t)/t^2
* f = sqrt(v^2+2*a*x)
* v = sqrt(f^2-2*a*x)
* a = (f^2-v^2)/(2*x)
* x = (f^2-v^2)/(2*a)

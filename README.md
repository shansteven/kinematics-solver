# kinematics-solver

Part of New Providence High School AP Physics C final project.

Program to automatically solve a kinematics problem using a known system of equations. Given any of the three following quantities, the program can solve for the remaining two quantities. The program also converts between units and lists the steps to solve the system.

**Designed to be run with Python 3**

Example:

<img src="https://github.com/shansteven/kinematics-solver/blob/master/example.png">

<table>
  <tr>
    <td>Variable</td><td>Quantity</td>
  <tr>
    <td>v</td><td>Initial Velocity</td>
  <tr>
    <td>f</td><td>Final Velocity</td>
  <tr>
    <td>a</td><td>Acceleration</td>
  <tr>
    <td>t</td><td>Time</td>
  <tr>
    <td>x</td><td>Displacement</td>
   </tr>
</table>

<table>
<tr><td>Equation</td></tr>
<tr><td>f = v+a*t</td></tr>
<tr><td>x = v*t+(a*t^2)/2</td></tr>
<tr><td>v = f-a*t</td></tr>
<tr><td>t = (f-v)/a</td></tr>
<tr><td>a = (f-v)/t</td></tr>
<tr><td>t = (sqrt(2*a*x+v^2)-v)/a</td></tr>
<tr><td>x = ((f+v)/2)*t</td></tr>
<tr><td>t = (2*x)/(f+v)</td></tr>
<tr><td>f = (2*x)/t-v</td></tr>
<tr><td>v = (2*x)/t-f</td></tr>
<tr><td>v = (x-(a*t^2)/2)/t</td></tr>
<tr><td>a = (2*x-2*v*t)/t^2</td></tr>
<tr><td>f = sqrt(v^2+2*a*x)</td></tr>
<tr><td>v = sqrt(f^2-2*a*x)</td></tr>
<tr><td>a = (f^2-v^2)/(2*x)</td></tr>
<tr><td>x = (f^2-v^2)/(2*a)</td></tr>
</table>

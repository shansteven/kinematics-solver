import math
import re
import os
print("September 16")
class kinematics:
	name = "Kinematics"
	variables = [
		["v", "Initial velocity", "mm/s"],
		["f", "Final velocity", "mm/s"],
		["a", "Acceleration", "mm/s^2"],
		["t", "Time", "s"],
		["x", "Displacement", "mm"]
	]
	# equations = [
# 		["f", "v+a*t"],
# 		["x", "v*t+(a*t^2)/2"],
# 		["v", "f-a*t"],
# 		["t", "(f-v)/a"],
# 		["a", "(f-v)/t"],
# 		["t", "([2*a*x+v^2]-v)/a"],
# 		["x", "((f+v)/2)*t"],
# 		["t", "(2*x)/(f+v)"],
# 		["f", "(2*x)/t-v"],
# 		["v", "(2*x)/t-f"],
# 		["v", "(x-(a*t^2)/2)/t"],
# 		["a", "(2*x-2*v*t)/t^2"],
# 		["f", "[v^2+2*a*x]"],
# 		["v", "[f^2-2*a*x]"],
# 		["a", "(f^2-v^2)/(2*x)"],
# 		["x", "(f^2-v^2)/(2*a)"]
# 	]
	equations = [
		["f=v+a*t"],
		["x=v*t+(1/2)*a*t^2"],
		["f^2=v^2+2*a*x"]
	]

conversions = {
	"mm": ("mm", 1.0),
	"m": ("mm", 1000.0),
	"cm": ("mm", 10.0),
	"in": ("mm", 25.4),
	"ft": ("mm", 304.8),
	"yd": ("mm", 914.4),
	"mi": ("mm", 1609000.0),
	"sec": ("s", 1.0),
	"s": ("s", 1.0),
	"min": ("s", 60),
	"hr": ("s", 3600),
}

map = [kinematics]

class cls():
	def __init__ (self, index = 0):
		self.variables = map[index].variables
		self.equations = map[index].equations

def find_nums (equation, variables, i):
	if i == 0:
		return False
	preg = re.compile("^[a-z]$")
	num_preg = re.compile("^[0-9\.~]$")
	x = [0,0]
	x1 = 0
	if preg.match(equation[i-1]):
		x1 = float(variables[equation[i-1]].replace("~","-"))
		x[0] = i-1
	else:
		j = 1
		x1 = ""
		while i - j >= 0 and num_preg.match(equation[i-j]):
			x1 = equation[i-j] + x1
			x[0] = i - j
			j += 1
		x1 = float(x1.replace("~", "-"))

	x2 = 0
	if preg.match(equation[i+1]):
		x2 = float(variables[equation[i+1]].replace("~","-"))
		x[1] = i+1
	else:
		j = 1
		x2 = ""
		while i + j < len(equation) and num_preg.match(equation[i+j]):
			x2 += equation[i+j]
			x[1] = i + j
			j += 1
		x2 = float(x2.replace("~", "-"))
	return [x1, x2, x[0], x[1]]

def guess_value (left, right, var, min, max, q, delta, derivative):
	variables = q
	variables[var] = "{:.5f}".format(float(left+right)/2.0)
	if typeof(left) == "string":
		left = eval_expression(left, variables)
	if typeof(right) == "string":
		right = eval_expression(right, variables)



def eval (j, q):
	global variables
	variables_list = re.findall("[a-z]", j)
	temp = []
	for x in variables_list:
		if x not in temp:
			temp.append(x)
	variables_list = temp
	remainder = len(variables_list)
	variables_found = []
	for x in variables_list:
		if q[x] is not False:
			remainder -= 1
			variables_found.append(x)

	if remainder == 1:
		var = [x for x in variables_list if x not in variables_found][0]
		equals_index = j.find("=")
		if equals_index != -1:
			part1 = j[0:equals_index]
			part2 = j[equals_index+1:]

			val1 = part1 if part1.find(var) == -1 else eval_expression(part1, q)
			val2 = part2 if part2.find(var) == -1 else eval_expression(part2, q)




	return False

def eval_expression (equation, variables,sqrt=False):
	equation = equation.lower()
	if equation == "":
		return 0
	equation = list(equation)
	paren = 0
	paren_i = 0
	bracket = 0
	bracket_i = 0
	i = 0
	cond = len(equation)
	indices_paren = []
	indices_bracket = []
	preg = re.compile("^[a-z]$")
	num_preg = re.compile("^[0-9\.]$")
	while i < cond:
		if preg.match(equation[i]) and variables[equation[i]] is False:
			return False
		if equation[i] == "(" and bracket == 0:
			if paren == 0:
				paren_i = i
			paren += 1
		elif equation[i] == ")":
			paren -= 1
			if paren == 0:
				equation[paren_i] = "".join(equation[paren_i+1:i])
				equation[paren_i+1:i+1] = []
				i = paren_i
				indices_paren.append(paren_i)
		elif equation[i] == "[" and paren == 0:
			if bracket == 0:
				bracket_i = i
			bracket += 1
		elif equation[i] == "]":
			bracket -= 1
			if bracket == 0:
				equation[bracket_i] = "".join(equation[bracket_i+1:i])
				equation[bracket_i+1:i+1] = []
				i = bracket_i
				indices_bracket.append(bracket_i)
		i += 1
		cond = len(equation)
	equation = [(eval(j, variables) if i in indices_paren else (eval(j,variables,True) if i in indices_bracket else j)) for i, j in enumerate(equation)]
	for i,j in enumerate(equation):
		equation[i:i+1] = list(j)

	i = 0
	cond = len(equation)
	while i < cond:
		if equation[i] == "^":
			nums = find_nums(equation, variables, i)
			if nums is False:
				return False
			value = "{:.5f}".format(math.pow(nums[0], nums[1]))
			equation[nums[2] + 1: nums[3] + 1] = []
			equation[nums[2]:nums[2]+1] = list(value)
			i = nums[2]
		i += 1
		cond = len(equation)

	i = 0
	cond = len(equation)
	while i < cond:
		if equation[i] == "*" or equation[i] == "/":
			nums = find_nums(equation, variables, i)
			if nums is False:
				return False
			value = nums[0]
			if equation[i] == "*":
				value *= nums[1]
			else:
				if float(nums[1]) < 0.00002:
					return False
				value /= nums[1]
			value = "{:.5f}".format(value).replace("-","~")
			equation[nums[2] + 1: nums[3] + 1] = []
			equation[nums[2]:nums[2]+1] = list(value)
			i = nums[2]
		i += 1
		cond = len(equation)

	i = 0
	cond = len(equation)
	while i < cond:
		if equation[i] == "+" or equation[i] == "-":
			nums = find_nums(equation, variables, i)
			if nums is False:
				return False
			value = nums[0]
			if equation[i] == "+":
				value += nums[1]
			else:
				value -= nums[1]
			value = "{:.5f}".format(value).replace("-","~")
			equation[nums[2] + 1: nums[3] + 1] = []
			equation[nums[2]:nums[2]+1] = list(value)
			i = nums[2]
		i += 1
		cond = len(equation)
	result = "".join(equation)
	if sqrt:
		result = "{:.5f}".format(math.sqrt(float("".join(equation))))
	return result

variables = {}
os.system('clear')

separator_line = "#######################"
print separator_line
print "#       Options       #"
print "#######################"
# print "# 1.) Kinematics      #"
for i in range(0, len(map)):
	map_label = "{:.0f}".format(i+1) + ".) " + map[i].name
	map_label_len = len(map_label)
	if map_label_len > len(separator_line) + 4:
		map_label = map_label[0:(len(separator_line)-4)]
	print "# " + map_label + "".join([" " for x in range(0, len(separator_line) - 4 - map_label_len)]) + " #"
print "#######################\n"

input = raw_input("Option #: ")
flag = False
try:
	input = int(input) - 1
except ValueError:
	flag = True
while flag is True or input < 0 or input >= len(map):
	print "\nInvalid option."
	input = raw_input("Try again: ")
	try:
		input = int(input) - 1
		flag = False
	except ValueError:
		flag = True
print "\n"
print separator_line
print map[input].name + " Solver:\n"
constants = cls(input)

for i in range(0, len(map[input].equations)):
	j = constants.equations[i]
	constants.equations[i][0] = j[0].lower()
	temp = re.findall("[a-z]", constants.equations[i][0])
	index = 0
	for x in range(0, len(temp)):
		if x == 0:
			constants.equations[i].insert(0, temp[x])
		else:
			constants.equations.append([temp[x], constants.equations[i][1]])

eqs = constants.equations
ignore_units = False
conversion_coeffs = []
units = []

for j,i in enumerate(constants.variables):
	flag = False
	question = i[1]
	i = i[0]
	while flag is False:
		variables[i] = raw_input(question + ": ").replace("-","~").lower()
		if variables[i] == "":
			variables[i] = False
			flag = True
			conversion_coeffs.append(1)
		else:
			value = variables[i]
			variables[i] = list(re.findall("[~]?[0-9]+[\.]?[0-9]*", variables[i]))
			if len(variables[i]) == 1:
				flag = True
				variables[i] = variables[i][0]
				if ignore_units is False:
					temp = list(re.findall("(mph|([a-z]+/[a-z]+[\^]?[0-9]?)|[a-z]+[\^]?[0-9]?)", value))
					if len(temp) != 1:
						ignore_units = True
						conversion_coeffs.append(1)
					else:
						temp = temp[0][0]
						if temp == "mph":
							temp = "mi/hr"
						slash_index = temp.find("/")
						if slash_index != -1:
							bk = variables[i]
							try:
								conversion = 1
								caret_index = temp.find("^")
								if caret_index == -1:
									conversion = conversions[temp[0:slash_index]][1] / conversions[temp[slash_index+1:]][1]
									units.extend([temp[0:slash_index], temp[slash_index+1:]])
								elif caret_index < slash_index:
									conversion = math.pow(conversions[temp[0:caret_index]][1], int(temp[caret_index+1:caret_index+2])) / conversions[temp[slash_index+1:]][1]
									units.extend([temp[0:caret_index], temp[slash_index+1:]])
								else:
									conversion = conversions[temp[0:slash_index]][1] / math.pow(conversions[temp[slash_index+1:caret_index]][1], int(temp[caret_index+1:caret_index+2]))
									units.extend([temp[0:slash_index], temp[slash_index+1:caret_index]])
								variables[i] = "{:.5f}".format(float(variables[i].replace("~", "-")) * conversion).replace("-", "~")
								constants.variables[j][2] = temp
								conversion_coeffs.append(conversion)
							except ValueError:
								variables[i] = bk
								ignore_units = True
								conversion_coeffs[-1] = 1
						else:
							bk = variables[i]
							try:
								conversion = 1
								caret_index = temp.find("^")
								if caret_index != -1:
									conversion = math.pow(conversions[temp[0:caret_index]][1],int(temp[caret_index+1:]))
									units.append(temp[0:caret_index])
								else:
									conversion = conversions[temp][1]
									units.append(temp)
								variables[i] = "{:.5f}".format(float(variables[i].replace("~", "-")) * conversion).replace("-", "~")
								constants.variables[j][2] = temp
								conversion_coeffs.append(conversion)
							except ValueError:
								variables[i] = bk
								ignore_units = True
								conversion_coeffs[-1] = 1
				else:
					conversion_coeffs.append(1)

temp = {}
for x,y in conversions.iteritems():
	temp[y[0]] = y[0]
for i in units:
	temp[conversions[i][0]] = i
for i in variables.iteritems():
	if i[1] is False:
		j = 0
		for z,x in enumerate(constants.variables):
			if x[0] == i[0]:
				j = z
				break
		default_unit = constants.variables[j][2]
		slash_index = default_unit.find("/")
		caret_index = default_unit.find("^")
		conversion = 1
		if slash_index == -1:
			if caret_index == -1:
				default_unit = temp[default_unit]
				conversion = conversions[default_unit][1]
			else:
				t = temp[default_unit[0:caret_index]]
				default_unit[0:caret_index] = t
				conversion = math.pow(conversions[t][1], int(default_unit[caret_index+1:]))
		else:
			if caret_index == -1:
				conversion = conversions[temp[default_unit[:slash_index]]][1] / conversions[temp[default_unit[slash_index+1:]]][1]
				default_unit = temp[default_unit[:slash_index]] + "/" + temp[default_unit[slash_index+1:]]
			elif caret_index < slash_index:
				conversion = math.pow(conversions[temp[default_unit[:caret_index]]][1], int(default_unit[caret_index+1:caret_index+2])) / conversions[temp[default_unit[slash_index+1:]]][1]
				default_unit = temp[default_unit[:caret_index]] + default_unit[caret_index:caret_index+2] + "/" + temp[default_unit[slash_index+1:]]
			else:
				conversion = conversions[temp[default_unit[:slash_index]]][1] / math.pow(conversions[temp[default_unit[slash_index+1:caret_index]]][1], int(default_unit[caret_index+1:caret_index+2]))
				default_unit = temp[default_unit[:slash_index]] + "/" + temp[default_unit[slash_index+1:caret_index]] + default_unit[caret_index:]
		conversion_coeffs[j] = conversion
		constants.variables[j][2] = default_unit

print "\n--------------------------------------------------------------------------"

progress = 1
count = 1
impossible = False
while progress != 0:
	progress = 0
	for i,j in enumerate(eqs):
		if variables[j[0]] is False:
			expression = eval(j[1], variables)
			if variables[j[0]] is not False and expression is not False and math.fabs(float(expression.replace("~","-")) - float(variables[j[0]].replace("~","-"))) > 0.2:
				impossible = True
				progress = 0
				break
			if expression is not False:
				progress += 1
				print str(count) + ".) Calculate ", j[0], " to be ", expression, " with the expression ", j[1]
				count += 1
				variables[j[0]] = expression
				del eqs[i]
				break

print "--------------------------------------------------------------------------\n"

if ignore_units is True:
	print "Warning: Default units were used.\n"

if impossible is True or (variables["t"] is False or variables["t"][0] == "~"):
	print "This is impossible."
else:
	for i,n in enumerate(constants.variables):
		print n[1] + ": " + ("{:.5f}".format(float(variables[n[0]].replace("~","-")) / conversion_coeffs[i]) if variables[n[0]] is not False else "N/A") + " " + n[2]

print "\n"

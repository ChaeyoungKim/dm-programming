dic_set = {}
dic_rel = {}

def create_set():
	name = input("    Enter set name : ")
	elements = input("    Enter elements (repeat until finished) : ")
	s1 = set([])
	elements = elements.split()
	for i in elements:
		j = int(i)
		s1 = s1.union(set([j]))
#	print("%s = " %name, s1)
	dic_set[name] = s1
	print("    Saved successfully.")

def show_set():
	while True:
		name = input("    Enter set name : ")
		if name not in dic_set:
			print("    There is no such set. Enter again.")
		else:
			print(dic_set[name])
			break

def cartesian_product():
	s1 = input("    Enter set name : ")
	s2 = input("    Enter set name : ")
	name = input("    Enter name of Cartesian product : ")
	l1 = list(dic_set[s1])
	l2 = list(dic_set[s2])
	cartesian = []
	for i in l1:
		for j in l2:
			cartesian.append((i,j))
	print("%s = " %name, cartesian)
	dic_set[name] = cartesian

def create_relation():
	name = input("    Enter name of relation : ")
	while True:
		elements = input("    Enter pairs (repeat until finished) : ")
		elements = elements.split()
		l1 = []
		l2 = []
		relation = []
		i = 1
		for element in elements:
			element = int(element)
			if i%2 == 1:
				l1.append(element)
				i += 1
			else:
				l2.append(element)
				i += 1
		if len(l1) != len(l2):
			print("    Not matching pair. Enter an even number of numbers.")
		else:
			break
	for j in range(1,len(l1)+1):
		relation.append((l1[j-1],l2[j-1]))
	dic_rel[name] = relation
	print(relation)

def check_equivalence():
	print("    Determine if a relation is an equivalence relation or not.")
	while True :
		name = input("    Enter name of relation : ")
		if name not in dic_rel :
			print("    There is no such relation. Enter again.")
		else :
			r1 = list(dic_rel[name])
			s1 = set([])
			for j in range(0,len(r1)):
				for k in range(0,2):
					s1.add(r1[j][k])
			rel_matrix = [[0 for x in range(0,len(s1))] for x in range(0,len(s1))]
			square_matrix = [[0 for x in range(0,len(s1))] for x in range(0,len(s1))]
			sl1= list(s1)
			for j in range(0,len(r1)):
				for l in range(0,len(sl1)):
					for m in range(0,len(sl1)):
						if r1[j][0] == sl1[l] and r1[j][1] == sl1[m]:
							rel_matrix[l][m] = 1

#			print(rel_matrix)

			j = 0
			while j < len(sl1):
				if rel_matrix[j][j] != 1:
					print(" -> Not reflexive. Therefore not equivalent")
					return
				j += 1

			for j in range(0,len(s1)):
				for k in range(0,len(s1)):
					if rel_matrix[j][k] != rel_matrix[k][j]:
						print(" -> Not symmetric. Therefore not equivalent")
						return

			for j in range(0,len(s1)):
				for k in range(0,len(s1)):
					sum = 0	
					for l in range(0,len(s1)):
						sum += rel_matrix[j][l]*rel_matrix[l][k]
					if sum>=1:
						sum = 1
					square_matrix[j][k] = sum
	#		print(square_matrix)

			for j in range(0,len(s1)):
				for k in range(0,len(s1)):
					if square_matrix[j][k] == 1:
						if rel_matrix[j][k] != 1:
							print(" -> Not transitive. Therefore not equivalent")
							return

			print(" -> Equivalent")
			return

print("""
 1. Create a set
 2. Show elements of a set
 3. Create a Cartesian product of two sets
 4. Create a relation between two sets
 5. Check if a relation is an equivalence relation
 """)
number = True
while number:
	number = int(input("\n * Enter a number : "))
	if number == 1:
		create_set()
	elif number == 2:
		show_set()
	elif number == 3:
		cartesian_product()
	elif number == 4:
		create_relation()
	elif number == 5:
		check_equivalence()
	else:
		print("    Not valid choice. Try again.")
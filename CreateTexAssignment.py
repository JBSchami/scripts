## Gather required information to build document skeleton
mainMenu = {}
mainMenu['1'] = "COMP5361"
mainMenu['2'] = "COMP5461"

typeMenu = {}
typeMenu['1'] = "Theory Assignment"
typeMenu['2'] = "Programming Assignment"

author = "Jonathan B. Schami - 40050610"

while True:
	print("Create assignment selection for which course?")
	options = mainMenu.keys()
	for entry in options:
		print (entry, mainMenu[entry])

	selection = input("Select course:")
	if selection == '1':
		courseCode = "COMP\\ 5361"
		courseID = "COMP5361"
		courseInstructor = "Grahne"
		courseTime = "5:45"
		break
	elif selection == '2':
		courseCode = "COMP\\ 5461"
		courseID = "COMP5461"
		courseInstructor = "Goswami"
		courseTime = "5:45"
		break
	else:
		print ("Selection invalid")

while True:
	print ("What type of assignment would you like to create?")
	options = typeMenu.keys()
	for entry in options:
		print (entry, typeMenu[entry])

	selection = input("Select Assignment Type: ")
	if selection == '1':
		assignmentNumber = input("Assignment number: ")
		assignmentType = "TA"
		assingmentTitle = "Theory Assignment\\ \\#%s" % assignmentNumber
		break
	elif selection == '2':
		assignmentNumber = input("Assignment number: ")
		assignmentType = "PA"
		assingmentTitle = "Programming Assignment\\ \\#%s" % assignmentNumber
		break
	else:
		print ("Selection invalid")

assignmentDueMonth = input("Assignment due month: ")
assignmentDueDay = input("assignment due day: ")
assignmentDueYear = input("Assignment due year: ")
assignmentDueDate = "%s\\ %s,\\ %s" % (assignmentDueMonth, assignmentDueDay, assignmentDueYear)

numberOfProblems = input("Number of questions in assignment: ")

newFileName = "%s_%s%s.tex" % (courseID, assignmentType, assignmentNumber)

with open(newFileName, "w") as f1:
	with open("C:\\Scripts\\part1.tex") as p1:
		for line in p1:
			f1.write(line)

		f1.write("\n")
		f1.write("\\newcommand{\\hmwkTitle}{%s}\n" % assingmentTitle)
		f1.write("\\newcommand{\\hmwkDueDate}{%s}\n" % assignmentDueDate)
		f1.write("\\newcommand{\\hmwkClass}{%s}\n" % courseCode)
		f1.write("\\newcommand{\\hmwkClassTime}{%s}\n" % courseTime)
		f1.write("\\newcommand{\\hmwkClassInstructor}{%s}\n" % courseInstructor)
		f1.write("\\newcommand{\\hmwkAuthorName}{%s}\n" % author)

		p1.close()

	with open("C:\\Scripts\\part2.tex") as p2:
		for line in p2:
			f1.write(line)
		p2.close()

	for x in range(0,int(numberOfProblems)):
		newProblemName = "%s_%s%s_Q%d.tex" % (courseID, assignmentType, assignmentNumber,x+1)
		with open(newProblemName, "w") as question:
			question.write("\\begin{homeworkProblem}\n\n")
			question.write("\\end{homeworkProblem}")
			question.close()
		f1.write("\n \\input{%s}" %newProblemName)

	f1.write("\n\\end{document}")
	f1.close()




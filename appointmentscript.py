import csv


# EAB columns include
#
# Student Name
# Student ID
# Majors
# Start Date
# Start Time
# Appointment Comment
# Cancelled

student_data = []

with open('input.csv', mode = 'r') as file:
	csvFile = csv.reader(file)
	for lines in csvFile:
		student_data.append(lines)

# creating csv header
output_data = [["Index", "First Name", "Last Name","Student ID", 
				"Major", "Appointment Date","Start Time","Appointment Comment"
				,"Cancelled?","Course Agreement Title","Prepped?"]]

del student_data[0] # removing header from EAB

cancelled_students = []

i = 1 # represents index or student number

for student in student_data: # loops through all students

	if student[6] == "Yes": # they cancelled
		cancelled_students.append(student)
		student_data.remove(student)

	else: # they didnt cancel
		lastName = student[0].split(", ")[0]
		firstName = student[0].split(", ")[1]
		ID = student[1]
		major = student[2]
		date = student[3]
		time = student[4]
		comment = student[5]
		cancelled = student[6]
		cat = str(firstName+"_"+lastName.split()[0]+"_"+ID+"_FA25")

		output_data.append([i,firstName,lastName,ID,major,date,time,comment
							,cancelled,cat])

		i+=1

while i <=13:
	output_data.append([i])
	i+=1

for student in cancelled_students:
	lastName = student[0].split(", ")[0]
	firstName = student[0].split(", ")[1]
	ID = student[1]
	major = student[2]
	date = student[3]
	time = student[4]
	comment = student[5]
	cancelled = student[6]
	cat = str(firstName+"_"+lastName.split()[0]+"_"+ID+"_FA25")

	output_data.append([i,firstName,lastName,ID,major,date,time,comment
						,cancelled,cat])


with open('output.csv','w',newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(output_data)
def assign_grd():
	
	grade = int(input("Enter your score: "))
	
	if grade < 0 or grade > 100:
		print("Invalid input, try again.")
	elif grade >= 90:
		print("grade: A")
	elif grade >= 80:
		print("grade: B")
	elif grade >= 70:
		print("grade: C")
	elif grade >= 60:
		print("grade: D")
	else:
		print("grade: F")
		
assign_grd()
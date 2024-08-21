last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
# Create a list of subjects
subjects = ["physics", "calculus", "poetry", "history"]

# Create a list of grades
grades = [98, 97, 85, 88]

# Create a 2D list for gradebook
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], 
["history", 88]]

# Add computer science
gradebook.append(["computer_science", 100])

# Add visual arts
gradebook.append(["visual arts", 93])

# Update visual art grade
gradebook[-1][-1] = 98

# Remove poetry grade
gradebook[2].remove(85) 

# Add Pass on poetry
gradebook[2].append("Pass")

#Combine both 2D lists
full_gradebook = last_semester_gradebook + gradebook

# Print full gradebook
print(full_gradebook)

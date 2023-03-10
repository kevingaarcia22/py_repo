# Define a function to calculate the average grade
def calculate_grade(exam_scores, hw_assignments):
    # Calculate the weighted average of the exam scores (70%) and homework assignments (30%)
    exam_weight = 0.7
    hw_weight = 0.3
    exam_average = sum(exam_scores) / len(exam_scores)
    hw_average = sum(hw_assignments) / len(hw_assignments)
    grade = (exam_average * exam_weight) + (hw_average * hw_weight)

    # Round the grade to two decimal places and return it
    return round(grade, 2)

# Prompt the user for their exam scores and homework assignments
exam_scores = []
hw_assignments = []
num_exams = int(input("Enter the number of exams: "))
num_hw = int(input("Enter the number of homework assignments: "))

for i in range(num_exams):
    score = float(input(f"Enter exam score {i+1}: "))
    exam_scores.append(score)

for i in range(num_hw):
    score = float(input(f"Enter homework assignment score {i+1}: "))
    hw_assignments.append(score)

# Calculate and output the average grade
average_grade = calculate_grade(exam_scores, hw_assignments)
print(f"Your average grade is: {average_grade}")

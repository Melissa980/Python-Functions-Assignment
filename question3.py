#Question 3 Task 1
def calculate_average_grade(grades):
    if not grades:
        return None
    total = sum(grades)
    return total / len(grades)

#Question 3 Task 2
def find_highest_and_lowest_grades(grades):
    if not grades:
        return None, None
    highest_grade = max(grades)
    lowest_grade = min(grades)
    return highest_grade, lowest_grade

#Question 3 Task 3
def categorize_grades(grades):
    if not grades:
        return None
    letter_grades = []
    for grade in grades:
        if grade >= 90:
            letter_grades.append('A')
        elif grade >= 80:
            letter_grades.append('B')
        elif grade >= 70:
            letter_grades.append('C')
        elif grade >= 60:
            letter_grades.append('D')
        else:
            letter_grades.append('F')
    return letter_grades


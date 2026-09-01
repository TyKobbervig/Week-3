def calculate_average(score_1, score_2, score_3) :
    total = score_1 + score_2 + score_3
    average = total / 3
    return average

def get_status(average):
    if average >= 60:
        return "passing"
    return "not passing"

def show_result(student_name, average, status):
    print("student:", student_name)
    print("Average:", average)
    print("Status:", status)
    
student_name = "Ty"
average = calculate_average(80, 75, 90)
status = get_status(average)
show_result(student_name, average, status)
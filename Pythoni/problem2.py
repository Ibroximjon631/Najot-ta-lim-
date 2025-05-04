def update_student_score(students:dict,student_name:str,score:int):
    if student_name in students.keys():
        students[student_name].append(score)
    else:
        students[student_name]=(score)
    return  students

def countStudents(students: List[int], sandwiches: List[int]) -> int:
    c = 0

    for i in range(len(students)):
        if students[i] == sandwiches[i]:
            students.pop(0)
            sandwiches.pop()
            c += 1
        else:
            temp = students.pop(0)
            students.append(temp)
        
    return c

print(countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))
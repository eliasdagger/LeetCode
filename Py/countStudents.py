# LeetCode 1700 - Number of Students Unable to Eat Lunch (Easy)
#
# Students are queued up for lunch, and sandwiches are stacked on a counter. Each
# is either square (0) or circular (1).
#
# Repeatedly: the student at the front of the queue looks at the sandwich on top
# of the stack. If they want that kind, they take it and leave; if not, they go to
# the back of the queue. This continues until nobody left in the queue wants the
# sandwich on top.
#
# Given students (the queue, front first) and sandwiches (the stack, top first),
# return how many students end up unable to eat.
#
# Example: students = [1,1,0,0], sandwiches = [0,1,0,1]  ->  0
#          students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]  ->  3


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
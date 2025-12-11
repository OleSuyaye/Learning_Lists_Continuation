four_west_marks = [89, 46, 78, 69, 66, 97, 22, 13, 56, 86]
four_east_marks = [78, 55, 48, 77, 33, 55, 56, 89, 78, 33]
four_south_marks = [67, 76, 33, 11, 77, 86, 90, 33, 55, 24]

def max_digit (x):
    max_number = x[0]
    for i in x:
        if i > max_number:
            max_number = i
    return max_number

def min_digit (x):
    min_number = x[0]
    for i in x:
        if i < min_number:
            min_number = i
    return min_number

print(f"The highest marks in 4W is {max_digit(four_west_marks)}, "
      f"and the lowest marks is {min_digit(four_west_marks)}")
print(f"The highest marks in 4E is {max_digit(four_east_marks)}, "
      f"and the lowest marks is {min_digit(four_east_marks)}")
print(f"The highest marks in 4S is {max_digit(four_south_marks)}, "
      f"and the lowest marks is {min_digit(four_south_marks)}")

def average (x):
    total = 0
    for i in x:
        total = total + i
    average_marks = total / len(x)
    return average_marks

print(f"The average marks of 4W, 4E, and 4S are as follows: 4W: {average(four_west_marks)},"
      f" 4E: {average(four_east_marks)},"
      f" 4S: {average(four_south_marks)}.")

#Class with the highest average
four_west_average = average(four_west_marks)
four_east_average = average(four_east_marks)
four_south_average = average(four_south_marks)

if four_west_average > four_east_average and four_west_average > four_south_average:
    print(f"4W has the highest average of {four_west_average}")
elif four_east_average > four_west_average and four_east_average > four_south_average:
    print(f"4E has the highest average of {four_east_average}")
else:
    print(f"4S has the highest average of {four_south_average}")

#Sorting the marks
def marks_sorting(x):
    sorted_marks = sorted(x)
    return sorted_marks

print(marks_sorting(four_west_marks))
print(marks_sorting(four_east_marks))
print(marks_sorting(four_south_marks))

four_west_marks.sort()
print(four_west_marks)

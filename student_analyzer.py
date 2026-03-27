marks = [45, 67, 89, 32, 76]

Sum = 0
Max = marks[0]
filtered = []

for value in marks:
    Sum = Sum + value
    
    if Max < value:
        Max = value
        
    if value > 60:
        filtered.append(value)

Avg = Sum / len(marks)

print("Average marks is:", Avg)
print("Highest marks is:", Max)
print("Marks greater than 60:", filtered)

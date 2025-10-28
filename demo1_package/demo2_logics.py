student_details={
    "studentName":"john", 
    "studentId":999,
     "marks":[30,40,50,60]
}

print(student_details["marks"])

marks_output=student_details["marks"]


for a in range(0,len(marks_output)):
    print(marks_output[a])

print("-" * 10)

total=0
for mark in marks_output:
    total =total+mark
    
print(total)

print("-" * 10)

data=[40,595,883,58,5885,39,333]

for a in data:
    if a==883:
        print("Yes it is present",a)
        break


check=True
print(10>5)



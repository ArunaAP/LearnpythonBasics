
employee_file = open("employee.txt", "r") # r - read / w - write / a - append(can modified any info) / r+ - read & write

print(employee_file.readable()) #true or false
#print(employee_file.read())


print(employee_file.readline()) #print line
print(employee_file.readline()) # by line

print(employee_file.readlines()) # print like list 


#using for loop
for employee in employee_file.readlines():
    print(employee)

employee_file.close()

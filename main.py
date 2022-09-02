#question1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# sorting the List
ages.sort()
print(ages)

# Finding the min and max age
minage=ages[0]
maxage=ages[-1]
print(minage)
print(maxage)

# Appending the min and max age to the list

ages.append(minage)
ages.append(maxage)
print(ages)

# Median Calculation
n= len(ages)
median=0
if(n%2==0):
    median = (ages[(n-1)//2]+ages[(n//2)])/2.0
else:
    median = (ages[n//2])/2
print(median)

# Average Calculation
average = sum(ages)//n
print(average)

# Range Calculation
Range = maxage - minage
print(Range)
print(".................................................................")
#question2
#creating a empty dictionary
dog = {}
print(dog)

# Adding Values to dictionary
dog = {
  "name": "Leo",
  "color": "Gold",
  "breed": "Golden Retriever",
  "Legs": 4 ,
  "age": 2
}
print(dog)

# Creating a student dictionary with keys and values
Student = {
    "first_name": "Siva Sai",
    "last_name": "Annem",
    "gender": "Male",
    "age": 24,
    "marital status":"Single",
    "skills":["Badminton","Cricket"],
    "country":"India",
    "city":"Hyderabad",
    "address":"kansas",
}
print(Student)

# Finding Length
print(len(Student))

#getting the value of skills
print(Student["skills"])

#getting the type of student skills
print(type(Student["skills"]))

#modifying the skills by adding two values
Student.update({"skills": ["Cricket","Football"]})
print(Student["skills"])

#getting the dictinory keys as a list
print(list(Student.keys()))

#getting the dictinory values as a list
print(list(Student.values()))
print(".................................................................")
#question3
# creating a tuple of sisters and brothers
Sisters = ("Kathya","Vidhya")
Brothers = ("Shree","Sai")

#Joining brothers and sisters tuples and assigning it to siblings
Siblings = Sisters+Brothers
print(Siblings)

#finding the length of the siblings
print(len(Siblings))

# modifying the siblings tuple
m = list(Siblings)
m.append("Viswanatha")
m.append("Jyothi")
family_members = tuple(m)
print(family_members)
print(".................................................................")

#question4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))# print of it_companies length

#Insert Twitter company to the it_companies set
it_companies.add("Twitter")
print(it_companies)

#Insert Multiple IT Companies to it_companies set
it_companies.update({"Mindtree","Capgemini"})
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("Mindtree")
print(it_companies)

#If the item to remove does not exist, remove() will raise an error where as discard() does not raise an error

#Join A and B
print(A.union(B))

# A intersection B
print(A.intersection(B))

# A subset B
print(A.issubset(B))

# A disjoint B
print(A.isdisjoint(B))

#Join A with B
print(A.union(B))

#join B with A
print(B.union(A))

#symmetric difference between A and B

print(A.symmetric_difference(B))

#Delete the sets
del A,B

#Convert the ages to a set and compare the length of the list and the set.
ages = set(age)
print(ages)
listlen=len(age)
setlen=len(ages)

print(listlen == setlen)
print(".................................................................")

#question5
r=input("Enter radius")
rad=int(r)
_area_of_circle_= 3.14*rad**2
_circum_of_circle_= 2*3.14*rad
print(_area_of_circle_)
print(_circum_of_circle_)
print(".................................................................")

#question6
# Given string
str ='I am a teacher and I love to inspire and teach people'

# splitting to words
list=str.split()
uniquewords = set(list) # set contains only unigue words
print("count of uniquewords:",len(uniquewords))
print(uniquewords)
print(".................................................................")

#question7
print("Name\t\t"+"Age\t\t"+"Country\t"+"\tCity\nAsabeneh\t"+"250\t\t"+"Finland\t\t"+"Helsink")
print(".................................................................")

#question8

# Given radius
radius = 10
# Area Calculation
area = 3.14*radius**2
# Displaying the output using String formatting
print("The area of circle with radius %d is %d meters square" %(radius,area))
print(".................................................................")

#question9
print("Enter the number of students")
n = int(input())
inputlist = []
output = []
print("Enter the weights in pounds")
for i in range(n):
    a = int(input())
    inputlist.append(a)
print("Given weights in lbs", inputlist)
for i in inputlist:
    b = (1/2.205)*i
    b = round(b, 2)
    output.append(b)
print(output)
print(".................................................................")






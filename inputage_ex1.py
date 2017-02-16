import datetime
today=datetime.date.today().year
birthday=input("did you have your birthday yet?(y/n): ")
age=int(input("what is your age: "))
assert age>=0, "Age has to be greater than 0"
if birthday=='y':
    yearborn=today-age
else:
    yearborn=today-age-1
year=yearborn+100
print 'you will turn 100 in: '+ str(year)
number=int(input("number; "))
for x in range(number):
    print (number*(str(number)))+'\n'

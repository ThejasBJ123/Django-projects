


model.py
admin.py


python manage.py shell

## 1)	Write a command to retrieve all the records from the table
from myapp.models import student
student.objects.all()
>>> exit()


## 2)	Write a command to retrieve all the records where the ID is equal to 1 from the table.
>>> student.objects.get(id=1)
>>> student.objects.filter(id=1)


## 3)	Write a command to retrieve all the records where the marks are greater than 40from the table.


student.objects.filter(marks__gt=40)

## 4)	 Write a command to retrieve all the records wher


## 5)	e the marks are less than 40 from the table.
student.objects.filter(marks__lt=40)

## 6)	e the marks are exat 40 from the table.
student.objects.filter(marks__exact=40)


## 7) 7)	Write a command to retrieve all the records where the marks are greater than or equal to 50 from the table.

student.objects.filter(marks__gte=40)

## 8)	Write a command to retrieve all the records where the marks are less than or equal to 50 from the table.
student.objects.filter(marks__lte=40)


## 9)	 Write a command to retrieve all the records where the name starts with "r" from the table

student.objects.filter(marks__lte=40)



## 10)	Write a command to retrieve all the records where the name ends with "a" from the table.
student.objects.filter(name__startswith="a")


## 11)	 Write a command to retrieve all the records where the ID is equal to 1, 2, or 3 from the table.
student.objects.filter(name__startswith="r")

student.objects.filter(name__endswith="a")

student.objects.filter(name__endswith="a" or "A")


student.objects.filter(id__in=[1,2,3])

##  12)	 Write a command to retrieve all the records where the marks are between 50 and 100 from the table. 

student.objects.filter(marks__range=[50,100])


form django.db.models import*

student.objects.aggregate(Avg('marks'))
student.objects.aggregate(Max('marks'))
student.objects.aggregate(Min('marks'))



## 16)	 Write a command to calculate the sum of all marks from the table.
student.objects.aggregate(Sum('marks'))


## 17)	Write a command to count the number of records in the table.

student.objects.aggregate(Count('marks'))

## 18)	Write a command to retrieve all the records sorted by name in ascending order from the table.
student.objects.all().order_by('name')

## 19)	Write a command to retrieve all the records sorted by name in descending order from the table
student.objects.all().order_by('-name')



>>> student.objects.create(name="sowmya", age=22, marks=47, place="bang")
<student: sowmya>


>>> student.objects.filter(name="sowmya").update(age=23)
1
>>> s=student.objects.filter(name="sowmya")
>>> print(s)
<QuerySet [<student: sowmya>]>


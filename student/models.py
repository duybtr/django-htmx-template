from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 10)
    age = models.DecimalField(max_digits = 7, decimal_places = 0)
    major = models.CharField(max_length = 50)
    profile_image = models.FileField(null=True, blank=True)

# call manually
def load_students():
    students = []
    students.append(Student(first_name='Joe', last_name='Johnson', gender='Male', age=22, major='Art'))
    students.append(Student(first_name='John', last_name='Doe', gender='Male', age=25, major='History'))
    students.append(Student(first_name='James', last_name='Tyler', gender='Male', age=30, major='Digital Art'))
    students.append(Student(first_name='Conrad', last_name='Well', gender='Male', age=27, major='Biology'))
    students.append(Student(first_name='Fred', last_name='Wells', gender='Male', age=25, major='Computer Engineering'))
    students.append(Student(first_name='George', last_name='Benson', gender='Male', age=25, major='Film'))
    students.append(Student(first_name='Jack', last_name='Hugh', gender='Male', age=21, major='Theater'))
    students.append(Student(first_name='Mary', last_name='Jay', gender='Female', age=21, major='Theater'))
    students.append(Student(first_name='Catherine', last_name='Moore', gender='Female', age=28, major='Computer Science'))
    students.append(Student(first_name='Elizabeth', last_name='Mendel', gender='Female', age=25, major='Chemistry'))
    student_models = Student.objects.bulk_create(students)
    return student_models
from django.db import models


DEPT_CHOICES = (
   ('CSE', 'CSE'),
   ('EE', 'EE'),
   ('ME', 'ME'),
   ('ECE', 'ECE'),
   ('Civil', 'Civil'),
)

SEM_CHOICE = (
    ('spring', 'spring'),
    ('fall', 'fall'),
    ('summer', 'summer'),
)

SECTION = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)


class Courses(models.Model):
    course_id = models.CharField(unique=True, max_length=20)
    title = models.CharField(max_length=120)
    department = models.CharField(max_length=120, choices=DEPT_CHOICES, default='unknown')
    credits = models.IntegerField()
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:      # this will order  with recent publish_date -> updated -> timestamp
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.course_id + " " + self.title


class Takes(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True, null=True)
    student_id = models.CharField(max_length=20)
    section = models.CharField(max_length=5, choices=SECTION, default='1')
    semester = models.CharField(max_length=20, choices=SEM_CHOICE)
    year = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.student_id + " " + self.course_id.course_id + "  " + self.semester + " " + self.year


class Teaches(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True, null=True)
    teacher_id = models.CharField(max_length=20)
    section = models.CharField(max_length=5, choices=SECTION, default='1')
    semester = models.CharField(max_length=20, choices=SEM_CHOICE, default='unknown')
    year = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.teacher_id + " " + self.semester + " " + self.year


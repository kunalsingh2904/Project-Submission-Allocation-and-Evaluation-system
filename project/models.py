from django.db import models
from courses.models import Courses


P_CHOICES = (
    ('open_project', 'open_project'),
    ('course_assignment', 'course_assignment'),
)


class Assignment(models.Model):
    title = models.CharField(max_length=200, null=False)
    types = models.CharField(max_length=20, choices=P_CHOICES, default='course_assignment')
    total_marks = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    files = models.FileField(upload_to='project/', null=True, blank=True)
    slug = models.SlugField(unique=True)
    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, blank=True, null=True)
    teach_by = models.CharField(max_length=20)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=False)
    semester = models.CharField(max_length=20, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    '''class Meta:
        ordering = ['-updated', '-timestamp']'''

    def __str__(self):
        return self.title + " " + self.teach_by


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submit_by = models.CharField(max_length=20)
    file = models.FileField(upload_to='submission/')
    marks = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.submit_by + " " + str(self.status) + " " + str(self.marks)


class Comments(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    user = models.CharField(default="unknown", max_length=120)
    comment = models.CharField(max_length=2000)
    slugs = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:  # this will order the blogs with recent publish_date -> updated -> timestamp
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.user + " " + self.comment




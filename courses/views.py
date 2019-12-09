from django.shortcuts import render
import string
import random
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User
from .models import Courses, Takes, Teaches
from users.models import UserProfile
from project.models import Assignment


current_year = settings.CURRENT_YEAR
current_sem = settings.CURRENT_SEM


@login_required
def course_list(request):
    users = get_object_or_404(UserProfile, user=request.user)
    if users.types == "student":
        qs = Takes.objects.filter(student_id=request.user.username,  year=current_year, semester=current_sem)
        if len(qs) <= 0:
            qs = None
        temp_name = "courses/course_list.html"
        content = {'context': qs}
        return render(request, temp_name, content)
    else:
        qs = Teaches.objects.filter(teacher_id=request.user.username, year=current_year, semester=current_sem)
        if len(qs) <= 0:
            qs = None
        temp_name = "courses/course_list.html"
        content = {'context': qs}
        return render(request, temp_name, content)

















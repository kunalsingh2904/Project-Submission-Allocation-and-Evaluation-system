from django.shortcuts import render
import string
from django.utils import timezone
import random
from django.http import HttpResponse
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render
from courses.models import Courses
from users.models import UserProfile
from .models import Assignment, Submission, Comments
from .forms import Assignmentform, Submissionform, Evaluationform


current_year = settings.CURRENT_YEAR
current_sem = settings.CURRENT_SEM


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(temp, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(temp)
    qs_exists = Assignment.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4))

        return unique_slug_generator(temp, new_slug=new_slug)
    return slug


def unique_slug_generator_comm(temp, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(temp)
    qs_exists = Comments.objects.filter(slugs=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4))

        return unique_slug_generator_comm(temp, new_slug=new_slug)
    return slug


@login_required
def list_assignment(request, slug):
    course = Courses.objects.get(slug=slug)
    users = get_object_or_404(UserProfile, user=request.user)
    if users.types == "student":
        ass = Assignment.objects.filter(course=course, year=current_year, semester=current_sem)
        if len(ass) == 0:
            ass = None
        temp_name = "project/assignment_list.html"
        content = {'course': course, 'ass': ass}
        return render(request, temp_name, content)
    else:
        ass = Assignment.objects.filter(course=course, year=current_year, semester=current_sem, teach_by=users.user.username)
        if len(ass) == 0:
            ass = None

        temp_name = "project/assignment_list.html"
        content = {'course': course, 'ass': ass, 'types': True}
        return render(request, temp_name, content)


@login_required
def view_assignment(request, slug):
    users = get_object_or_404(UserProfile, user=request.user)
    assignment = Assignment.objects.get(slug=slug)
    comments = Comments.objects.filter(assignment=assignment)
    curr_time = timezone.now()
    if users.types == "student":
        if curr_time <= assignment.end_date:
            submit = True
            sub = Submission.objects.filter(assignment=assignment, submit_by=users.user.username)
            if len(sub) >= 1:
                update = True
            else:
                update = False
        else:
            submit = False
            update = False
        content = {'ass': assignment, 'submit': submit, 'update': update, 'comments': comments}
        temp_name = "project/view_assignment.html"
        return render(request, temp_name, content)
    else:
        types = True
        content = {'ass': assignment, 'type': types, 'comments': comments}
        temp_name = "project/view_assignment.html"
        return render(request, temp_name, content)


@login_required
def create_assignment(request, slug):
    course = Courses.objects.get(slug=slug)
    form = Assignmentform(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.course = course
        obj.semester = current_sem
        obj.year = current_year
        obj.teach_by = request.user.username
        kk = form.cleaned_data.get('title')
        obj.slug = unique_slug_generator(kk)
        obj.save()

        # form = Assignmentform()
        return redirect('/project/ass_list/{}'.format(slug))
    temp_name = 'project/create_assignment.html'
    content = {'form': form}
    return render(request, temp_name, content)


@login_required
def update_assignment(request, slug):
    ass = Assignment.objects.get(slug=slug)
    form = Assignmentform(request.POST or None, request.FILES or None, instance=ass)
    if form.is_valid():
        form.save()
        return redirect('/project/view_ass/{}'.format(slug))
    temp_name = 'project/create_assignment.html'
    content = {'form': form, 'update': True}
    return render(request, temp_name, content)


@login_required
def delete_assignment(request, slug):
    ass = Assignment.objects.get(slug=slug)
    course_slug = ass.course.slug
    temp_name = "project/delete_assignment.html"
    if request.method == "POST":
        ass.delete()
        return redirect('/project/ass_list/{}'.format(course_slug))
    content = {'ass': ass}
    return render(request, temp_name, content)


@login_required
def add_submission(request, slug):
    ass = Assignment.objects.get(slug=slug)
    sub = Submission.objects.filter(assignment=ass, submit_by=request.user.username)
    if len(sub) >= 1:
        submission = sub[0]
        form = Submissionform(request.POST or None, request.FILES or None, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('/project/view_ass/{}'.format(slug))
    else:
        form = Submissionform(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.assignment = ass
            obj.submit_by = request.user.username
            obj.status = False
            obj.save()

            return redirect('/project/view_ass/{}'.format(slug))
    temp_name = 'project/add_submission.html'
    content = {'form': form, 'ass': ass}
    return render(request, temp_name, content)


@login_required
def evaluation(request, slug):
    ass = Assignment.objects.get(slug=slug, teach_by=request.user.username)
    sub = Submission.objects.filter(assignment=ass)
    if len(sub) <= 0:
        sub = None
    temp_name = 'project/submission_list.html'
    content = {'sub': sub, 'ass': ass}
    return render(request, temp_name, content)


@login_required
def submitby(request, slug, submit_by):
    ass = Assignment.objects.get(slug=slug, teach_by=request.user.username)
    sub = Submission.objects.get(assignment=ass, submit_by=submit_by)
    form = Evaluationform(request.POST or None, request.FILES or None, instance=sub)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.status = True
        obj.save()
        return redirect('/project/view_sub/{}'.format(slug))
    temp_name = 'project/view_submission_ind.html'
    content = {'form': form, 'ass': ass, 'sub': sub}
    return render(request, temp_name, content)


@login_required
def viewmarks(request, slug):
    ass = Assignment.objects.get(slug=slug)
    subs = Submission.objects.filter(assignment=ass, submit_by=request.user.username)
    if len(subs) == 0:
        sub = None
    else:
        sub = subs[0]
    temp_name = 'project/view_marks.html'
    content = {'ass': ass, 'sub': sub}
    return render(request, temp_name, content)


@login_required
def add_comment(request, slug):
    comm = request.GET.get('comment', None)
    ass = get_object_or_404(Assignment, slug=slug)
    if comm is not None and comm != "":
        ss = unique_slug_generator_comm(comm)
        Comments.objects.create(assignment=ass, comment=comm, user=request.user.username, slugs=ss)
    return redirect('/project/view_ass/{}'.format(slug))


@login_required
def delete_comment(request, slug, slugs):
    ass = get_object_or_404(Assignment, slug=slug)
    obj = get_object_or_404(Comments, assignment=ass, slugs=slugs)
    obj.delete()
    return redirect('/project/view_ass/{}'.format(slug))


@login_required
def open_project(request):
    ass = Assignment.objects.filter(types='open_project', year=current_year)
    if len(ass) == 0:
        ass = None
    '''users = get_object_or_404(UserProfile, user=request.user)
    if users.types == "student":
        types = False
    else:
        types = True'''
    content = {'ass': ass, 'curr_year': current_year}
    temp_name = 'project/open_project_list.html'
    return render(request, temp_name, content)





























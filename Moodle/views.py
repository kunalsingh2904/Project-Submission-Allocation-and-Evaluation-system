from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from courses.models import Courses, Takes, Teaches
from django.core.mail import send_mail


@login_required
def search_course(request):
    query = request.GET.get('q', None)
    if query is None or query == "":
        return redirect('/courses/')
    else:
        output = Courses.objects.filter(Q(course_id__contains=query) | Q(title__icontains=query) | Q(department__icontains=query))
        content = {'output': output, 'query': query}
        return render(request, 'search.html', content)


def contact_us(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        details = request.POST['detail']
        body = name + "\n" + email + "\n" + details
        send_mail(subject, body, 'help.bloghelp@gmail.com', [email,])
        return render(request, 'thanks.html')
    return render(request, 'contact.html')




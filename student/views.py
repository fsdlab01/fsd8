from django.shortcuts import render
from student.models import Students,Course
from django.http import HttpResponse
# Create your views here.
def register(request):
    if request.method == 'POST':
        sname = request.POST.get('sname')
        cname = request.POST.get('cname')
        students = Students.objects.filter(name=sname).values()
        if students:
            print(students.first())
            sid=students.first()['id']
            s=Students.objects.get(id=sid)
            courses = Course.objects.filter(cname=cname).values()
            if courses:
                cid=courses.first()['id']
                c=Course.objects.get(id=cid)
                s.sce.add(c) 
                return render(request,'register.html', {'message': 
                'Successfully registered'})
            else:
                return render(request,'register.html',{'message': 
            'Course not found'})
        else:
            return render(request,'register.html',{'message': 'Student not found'})
    else:
        return render(request,'sentry.html')
def viewstudent(request):
    courses = Course.objects.all().values() 
    if courses:
        return render(request,'view.html', {'courses':courses})
    else:
        return 'Student not found'
def displaystudents(request):
    cid = request.POST.get('course')
    students=Students.objects.all()
    l=list()
    for s in students:
        ss=s.sce.filter(id=cid).values()
        if ss:
            l.append(s.name)
    if len(l)>=1:
        return render(request,'displaystudents.html', {'l':l})
    else:
        return HttpResponse("NO Students found for the course")
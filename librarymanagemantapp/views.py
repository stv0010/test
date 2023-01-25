from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from librarymanagemantapp.models import Student, Course, Book, Issuedbook


# Create your views here.
def log_fun(request):
    return render(request,'login.html',{'data':''})

def adminsign_fun(request):
    return render(request,'adminsignup.html',{'data':''})

def studentsign_fun(request):
    c1 = Course.objects.all()
    return render(request,'studentsignup.html',{'data':'','lis':c1})

def checklog_fun(request):
    usern=request.POST['tname']
    userp=request.POST['tpass']
    user1=authenticate(username=usern,password=userp)
    if user1 is not None:
        if user1.is_superuser:
            return render(request,'adminhome.html')
        else:
            return render(request, 'login.html', {'data': 'user is not super user'})
    elif Student.objects.filter(Q(sname=usern) & Q(spassw=userp)).exists():
        return render(request,'studenthome.html',{'nam':usern})
    else:
        return render(request, 'login.html', {'data': 'inavlid username or password'})


def adminreg_fun(request):
    usern=request.POST['tname']
    usere=request.POST['temail']
    userp=request.POST['tpass']
    if User.objects.filter(Q(username=usern)|Q(email=usere)).exists():
        return render(request, 'adminsignup.html', {'data': 'username or email already exists'})
    else:
        u1=User.objects.create_superuser(username=usern, email=usere, password=userp)
        u1.save()
        return render(request, 'login.html', {'data': 'Account created successfully'})


def studentreg_fun(request):
    usern = request.POST['tname']
    users = request.POST['tsem']
    userm = request.POST['tmob']
    userc = request.POST['ddlcourse']
    userp = request.POST['tpass']
    if Student.objects.filter(Q(sname=usern)):
        return render(request, 'studentsignup.html', {'data': 'user name already exists try another'})
    else:
        s1=Student()
        s1.sname=usern
        s1.spassw=userp
        s1.sem=users
        s1.sphno=userm
        s1.scourse=Course.objects.get(cname=userc)
        s1.save()
        return render(request, 'login.html', {'data': 'Registered successfully'})

def admminhome_fun(request):
    return render(request,'adminhome.html')

def addbook_fun(request):
    c1 = Course.objects.all()
    return render(request,'addbook.html',{'data':'','lis':c1})


def readbookdata_fun(request):
    b1=Book()
    b1.bname=request.POST['tbname']
    b1.authname=request.POST['taname']
    b1.courseid=Course.objects.get(cname=request.POST['ddlcourse'])
    b1.save()
    return render(request,'addbook.html',{'data':'details added','lis':''})


def displaybook_fun(request):
    b1=Book.objects.all()
    return render(request,'displaybook.html',{'data':'','lis':b1})


def deletebook_fun(request,id):
    b1=Book.objects.get(id=id)
    b1.delete()
    b2 = Book.objects.all()
    return render(request,'displaybook.html',{'data':'data deleted successfully','lis':b2})


def updatebook_fun(request,id):
    b1=Book.objects.get(id=id)
    c1 = Course.objects.all()
    if request.method=='POST':
        b2 =Book.objects.get(id=id)
        b2.bname = request.POST['tbname']
        b2.authname = request.POST['taname']
        b2.courseid = Course.objects.get(cname=request.POST['ddlcourse'])
        b2.save()
        return redirect('displaybook')
    return render(request,'updatebook.html',{'lis':b1,'lis2':c1})

def assignbook_fun(request):
    c1=Course.objects.all()
    if request.method=='POST':
        b1=Book.objects.filter(courseid=Course.objects.get(cname=request.POST['ddlcourse']))
        s1=Student.objects.get(Q(sem=request.POST['tsem']) & Q(scourse=Course.objects.get(cname=request.POST['ddlcourse'])))
        return render(request, 'assignbook.html', {'lis2': b1,'lis3':s1})
    return render(request,'assignbook.html',{'lis':c1})

def readissuedbook_fun(request):
    i1=Issuedbook()
    i1.studname=Student.objects.get(sname=request.POST['ddlstud'])
    i1.studbook=Book.objects.get(bname=request.POST['ddlbook'])
    i1.startdate=request.POST['tstart']
    i1.enddate=request.POST['tend']
    i1.save()
    return redirect('assignbook')

def issuedbookdis_fun(request):
    i1=Issuedbook.objects.all()
    return render(request,'issuedbookdisplay.html',{'lis':i1})

def issdbkupdate_fun(request,id):
    i2=Issuedbook.objects.get(id=id)
    b1=Book.objects.all()
    if request.method=='POST':
        i1 = Issuedbook.objects.get(id=id)
        i1.studname = Student.objects.get(sname=request.POST['ddlstud'])
        i1.studbook = Book.objects.get(bname=request.POST['ddlbook'])
        i1.startdate = request.POST['tstart']
        i1.enddate = request.POST['tend']
        i1.save()
    return render(request,'issuedbookupdate.html',{'lis':i2,'lis2':b1})


def issdbkdelete_fun(request,id):
    i1=Issuedbook.objects.get(id=id)
    i1.delete()
    return redirect('issuedbookdis')

def logoutad_fun(request):
    return redirect('log')


def studenthome_fun(request):
    return render(request,'studenthome.html',{'name':''})

def stissdbkdet_fun(request):

    i1=Issuedbook.objects.all()
    return render(request,'studentissuedbooks.html',{'lis':i1})

def logoutst_fun(request):
    return redirect('log')
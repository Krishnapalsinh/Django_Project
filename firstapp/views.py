from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Student
from .student_form import StudentForm


# Create your views here.
def index(req):
    return render(req, 'index.html')


def displayForm(req):
    context = {'form': StudentForm}
    return render(req, "displayForm.html", context)


def ins_data(req):
    Student.objects.create(name=req.POST['sname'], roll=req.POST['roll'])
    return HttpResponse("Inserted Successfully!")


def show_data(req):
    context = {'students': Student.objects.all()}
    return render(req, 'showDetails.html', context)


def perform_operations(req):
    id = req.POST.get("id")
    if req.POST.get("btnDelete"):
        s = Student.objects.get(id=id)
        s.delete()
        return HttpResponseRedirect("/home/Details")
    elif req.POST.get("bnUpdate"):
        pass


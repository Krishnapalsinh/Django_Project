from django.http import HttpResponseRedirect
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
    return HttpResponseRedirect("/home/details/")


def show_data(req):
    context = {'students': Student.objects.all()}
    return render(req, 'showDetails.html', context)


def perform_operations(req):
    id = req.POST.get("id")
    if req.POST.get("btnDelete"):
        s = Student.objects.get(id=id)
        s.delete()
        return HttpResponseRedirect("/home/details/")
    elif req.POST.get("btnEdit"):
        s = Student.objects.get(id=id)
        context = {'form': StudentForm(initial={'sname': s.name, 'roll': s.roll}), 'id': id}
        return render(req, 'update.html', context)


def update_record(req):
    name = req.POST.get('sname')
    roll = req.POST.get('roll')
    id = req.POST.get('id')
    s = Student.objects.get(id=id)
    s.name = name
    s.roll = roll
    s.save()
    return HttpResponseRedirect("/home/details/")

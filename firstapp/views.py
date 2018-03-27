from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from .models import Student
from .student_form import StudentForm


# Create your views here.
def index(req):
    return render(req, 'index.html')

def displayForm(req):
    context = {'form': StudentForm}
    return render(req, "displayForm.html", context)


def showDetails(req):
    context = {}
    try:
        Student.objects.create(name=req.POST['sname'], roll=req.POST['roll'])
    except :
        context["error"] = 'mulval'
        return HttpResponseRedirect("/home")
    context['students'] = Student.objects.all()
    return render(req, 'showDetails.html', context)

from django.shortcuts import render

from .student_form import StudentForm


# Create your views here.
def index(req):
    return render(req, 'index.html')


def displayForm(req):
    context = {'form': StudentForm}
    return render(req, "displayForm.html", context)


def showDetails(req):
    name = req.POST['name']
    roll = req.POST['roll']
    context = {'name': name, 'roll': roll}
    return render(req, 'showDetails.html', context)

from django.shortcuts import render, redirect
from .models import Korisnici, Predmeti, Upisi
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
# Create your views here.

@login_required
def home(request):
    context = {
        'title': "Home",
        'content': Korisnici.objects.all(),

    }
    return render(request, 'sustav/home.html', context)
@login_required
def predmet(request, predmet):
    context = {
        'predmet': Predmeti.objects.filter(ime=predmet).first()
    }
    return render(request, 'sustav/predmet.html', context)
@login_required
def predmetEdit(request, predmet):

    predmet = Predmeti.objects.filter(ime=predmet).first()
    data={"ime": predmet.ime, "kod": predmet.kod, "program": predmet.program, "bodovi": predmet.bodovi, "sem_redovni": predmet.sem_redovni, "sem_izvanredni": predmet.sem_izvanredni, "izborni": predmet.izborni}


    if request.method == 'POST':
        
        form = PredmetForm(request.POST, instance=predmet)
        if form.is_valid():    
            form.save()
            messages.success(request, f'Predmet uspješno promijenjen!')
            return redirect('Sustav-Courses')
    else:
        form = PredmetForm(initial=data)
    context = {
        'form': form,
        'predmet': predmet
    }
    return render(request, 'sustav/predmetEdit.html', context)
@login_required
def studentEdit(request, korisnik):
    content ={
        'upisi' : Upisi.objects.all(),
        'korisnik' : Korisnici.objects.filter(email=korisnik).first(),
        'content' : Predmeti.objects.all()
    }
    korisnik = Korisnici.objects.filter(email=korisnik).first()
    return render(request, 'sustav/studentEdit.html', content)

@login_required
def upisniList(request, korisnik):
    content ={
        'upisi' : Upisi.objects.all(),
        'korisnik' : Korisnici.objects.filter(email=korisnik).first(),
        'content' : Predmeti.objects.all()
    }
    korisnik = Korisnici.objects.filter(email=korisnik).first()
    return render(request, 'sustav/upisniList.html', content)

def add(request, pk, cpk):
    content ={
        'upisi' : Upisi.objects.all(),
        'korisnik' : Korisnici.objects.filter(id=pk).first(),
        'content' : Predmeti.objects.all()
    }
    student = Korisnici.objects.get(id=pk)
    predmet = Predmeti.objects.get(id=cpk)
    email=student.email
    upis = Upisi(student=student, predmet=predmet, status='enrolled')
    try:
        upis.save()
    except:
        return render(request, 'sustav/studentEdit.html', content)

    return render(request, 'sustav/studentEdit.html', content)

def remove(request, pk, cpk):
    content ={
        'upisi' : Upisi.objects.all(),
        'korisnik' : Korisnici.objects.filter(id=pk).first(),
        'content' : Predmeti.objects.all()
    }
    student = Korisnici.objects.get(id=pk)
    predmet = Predmeti.objects.get(id=cpk)
    email=student.email
    try:
        Upisi.objects.filter(student=student, predmet=predmet).delete()
    except:
        return render(request, 'sustav/studentEdit.html', content)

    return render(request, 'sustav/studentEdit.html', content)

def passed(request, pk, cpk):
    content ={
        'upisi' : Upisi.objects.all(),
        'korisnik' : Korisnici.objects.filter(id=pk).first(),
        'content' : Predmeti.objects.all()
    }
    student = Korisnici.objects.get(id=pk)
    predmet = Predmeti.objects.get(id=cpk)
    email=student.email
    upis = Upisi.objects.get(student=student, predmet=predmet)
    upis.status='passed'
    try:
        upis.save()
    except:
        return render(request, 'sustav/studentEdit.html', content)

    return render(request, 'sustav/studentEdit.html', content)



@login_required
def students(request):
    content = {
        'title': "Studenti",
        'content': Korisnici.objects.all()
    }
    return render(request, 'sustav/students.html', content)

@login_required
def courses(request):
    content = {
        'title': "Predmeti",
        'content': Predmeti.objects.all()
    }
    return render(request, 'sustav/courses.html', content)
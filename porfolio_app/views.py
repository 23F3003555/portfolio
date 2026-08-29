from django.shortcuts import render,redirect
from .forms import ContectForm
from .models import Project
from django.contrib import messages

def home(request):
    projects=Project.objects.all()

    return render(request, 'portfolio/home.html',
                  {'projects':projects})



def contect(request):
    if request.method == "POST":
        form=ContectForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"message sent successfully !")
            return redirect('home')
    else:
        form=ContectForm()


    return render(request, 'contect.html', {'form':form})
# Create your views here.

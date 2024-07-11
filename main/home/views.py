from django.shortcuts import render, redirect
from .form import person
from .models import personModel

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = person(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            Personalinfo = personModel(first_name=first_name,last_name=last_name)
            Personalinfo.save()
            return redirect('success')
    else:
        form = person
    return render(request, 'home.html',{'form':form})

def success(request):
    return render(request,'success.html')
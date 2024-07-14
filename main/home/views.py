from django.shortcuts import render, redirect
from .form import person

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = person(request.POST)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = person
    return render(request, 'home.html',{'form':form})

def success(request):
    return render(request,'success.html')
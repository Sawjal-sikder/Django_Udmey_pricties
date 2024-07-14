from django.shortcuts import render, redirect
from .form import person
from .models import personModel
# Create your views here.
def home(request):
    if request.method == 'POST':
        excute_data = personModel.objects.get(pk=1)
        form = person(request.POST, instance=excute_data)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = person
    return render(request, 'home.html',{'form':form})

def success(request):
    return render(request,'success.html')
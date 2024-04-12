from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView
from .forms import SubmitForm
from .models import Reading
from django.contrib import messages

# Create your views here.
# def success(request):
#     return HttpResponse('successfully submitted')


def success(request):
  return render(request,'base.html')

class ReadingListView(ListView):
    model = Reading
    template_name = 'reading.html'

# def reading(request):
#     return render(request,'reading.html')
    


def home(request):
    form = SubmitForm()
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,'Your submission has been successfully sent')
        return success(request)
        
            
        
    else:
        form = SubmitForm()
    

    return render(request, "home.html",context = {'form':form})



    


def home(request):
    form = SubmitForm()
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,'Your submission has been successfully sent')
        return success(request)
        
            
        
    else:
        form = SubmitForm()
    

    return render(request, "home.html",context = {'form':form})

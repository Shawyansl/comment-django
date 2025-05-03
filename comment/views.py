from django.shortcuts import render
from .models import User
from .forms import ContactUs
from django.http import HttpResponse
# Create your views here.

def home(request):
    result = User.objects.all()
    context = {'models': result}
    return render(request, 'comment/comments.html' , context)

def contactUs(request):
    msg = ""
    if request.method == 'POST':
        form = ContactUs(request.POST)
        msg = "Saved successfully!"
    else:
        form = ContactUs()
    return render(request, 'comment/contactUs.html', {'form': form, 'msg': msg})

def saveContact(request):
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for your comment, " + form.data["username"] + ".")
    return HttpResponse("Only POST requests are allowed.")

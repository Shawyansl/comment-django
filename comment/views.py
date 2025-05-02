from django.shortcuts import render
# Create your views here.

def home(request):
    context = {
        'name': 'Ali',
        'username': 'Ali123',
    }

    return render(request, 'comment/comments.html' , context)

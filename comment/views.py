from django.shortcuts import render , redirect
from .models import User
from .forms import CommentForm
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    result = User.objects.all()
    context = {'models': result}
    return render(request, 'comment/comments.html' , context)

def contactUs(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # گرفتن نام کاربری از فرم
            try:
                user = User.objects.get(username=username)  # پیدا کردن کاربر با نام کاربری
                comment = form.save(commit=False)
                comment.user = user  # استفاده از کاربر پیدا شده
                comment.text = form.cleaned_data['text']  # ذخیره کردن متن کامنت
                comment.save()
                return redirect('/')  # Redirect to a success page or home page
            except User.DoesNotExist:
                return HttpResponse("User with this username does not exist.")
    else:
        form = CommentForm()
    
    return render(request, 'comment/contactUs.html', {'form': form})

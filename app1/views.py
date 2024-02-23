from django.shortcuts import render
#from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'homepage.html')
def about(request):
    return render(request, 'myapp/about.html')
#@login_required
def mainpage_view(request):
    return render(request, 'mainpage.html')

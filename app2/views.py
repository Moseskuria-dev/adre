from django.shortcuts import render
#from django.contrib.auth.decorators import login_required

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def gallery(request):
    return render(request, 'gallery.html')
#@login_required
def index(request):
    return render(request, 'index.html')
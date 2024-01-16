from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def foodmenu(request):
    return render(request,'foodmenu.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')




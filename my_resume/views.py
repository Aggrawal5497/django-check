from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "my_resume/index.html", {"content" : "Hello world"})
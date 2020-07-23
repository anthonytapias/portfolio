from django.shortcuts import render

# Create your views here.
def home_view(request):
    template_name = "base.html"
    return render(request, template_name)

def about_view(request):
    template_name = "about.html"
    return render(request, template_name)

def projects_view(request):
    template_name = "projects.html"
    return render(request, template_name)

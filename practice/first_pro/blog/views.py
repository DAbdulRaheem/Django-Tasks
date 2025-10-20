from django.http import HttpResponse

def blog_home(request):
    return HttpResponse("This is the blog home page")

def blog_about(request):
    return HttpResponse("This is the blog about page")

from django.shortcuts import render

# Create your views here.
def index(request):
    html = "<H1>Priyanka website</H1>"
    return HttpResponse(html)

def index(request):
    return render(request, 'personalweb/index.html')
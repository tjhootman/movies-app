from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies': ['mission impossible', 'back to the future', 'lord of the rings']
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html', {})
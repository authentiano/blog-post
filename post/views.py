from django.shortcuts import render

# Create your views here.
def home(request):
    title = "My app"
    context = { "title": title}
    return render(request, 'post/home.html', context)


def blog(request):
    # title = "My app"
    context = {}
    return render(request, 'post/blogpost.html', context)

from django.shortcuts import render

# Create your views here.
def v_boke(request):
    return render(request, 'blog.html')
from django.shortcuts import render

# Create your views here.
def v_about(request):
    return render(request, 'about.html')
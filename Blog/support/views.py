from django.shortcuts import render

# Create your views here.

def v_support(request):
    return render(request, 'support.html')

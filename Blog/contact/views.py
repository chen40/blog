from django.shortcuts import render

# Create your views here.
def v_contact(request):
    return render(request, 'contact.html')
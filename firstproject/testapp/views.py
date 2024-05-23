from django.shortcuts import render

# Create your views here.
def mywish(request):
    return render(request,'testapp/index.html')

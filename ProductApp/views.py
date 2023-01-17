from django.shortcuts import render, HttpResponse

def productapp_home(request):
    return HttpResponse("<H1>Hello</H1>")

def testbt(request):
    return render(request, 'productapp/testbt.html')



from django.shortcuts import render, redirect

def index(request):
    if request.method == 'GET':
        return render(request, 'upload_test.html')

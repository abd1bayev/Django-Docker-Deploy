from django.shortcuts import render


def index(request):
    return render(request, 'expenses/index.html')

def add_expence(request):
    return render(request, 'expenses/add_expence.html')
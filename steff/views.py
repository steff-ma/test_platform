from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def test_data(request):
    return render(request, 'test_data.html', {})
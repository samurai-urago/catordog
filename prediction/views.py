from django.shortcuts import render
from .forms import ImageUploadForm
import random

def predict(request):
    if request.method == 'GET':
        form = ImageUploadForm()
        return render(request, 'home.html', {'form': form})

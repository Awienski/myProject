from django.shortcuts import render
from .models import Sekolah
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user = request.user
    sekolah = Sekolah.objects.filter(user_id=user).order_by('name_school')
    return render(request, 'sekolah/index.html', {
        'sekolah' : sekolah,
    })

def add(request):
    return render(request, 'sekolah/add.html')

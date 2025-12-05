from django.shortcuts import render
from django.http import HttpResponse

def user(request):
    user = {
        'name': 'Nayan',
        'image': 'user.jpeg',
        'designation': 'Software Developer',
        'email': 'john.doe@email.com',
        'phone': '+1 (555) 123-4567',
        'location': 'New York, USA',
        # 'since': 'January 2024',
        'is_male': True,
        'skills': ['python', 'javascript', 'c']
    }
    return render(request, 'user.html', user)

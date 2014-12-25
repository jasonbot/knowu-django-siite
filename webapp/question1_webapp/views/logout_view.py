#! python

import django.contrib.auth
from django.shortcuts import redirect

__all__ = ['logout']

def logout(request):
    django.contrib.auth.logout(request)    
    return redirect('/')

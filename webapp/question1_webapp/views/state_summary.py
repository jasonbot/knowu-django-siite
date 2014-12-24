#! python

__all__ = ['home']

import os
import json

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

STATE_DATA = None

def check_state_data():
    """Load JSON into memory if it isn't cached"""
    global STATE_DATA
    if STATE_DATA is None:
        script_dir = os.path.abspath(os.path.dirname(__file__))
        summary_file = os.path.join(script_dir, 'state_summary.json')
        with open(summary_file, 'rb') as summary_file:
            STATE_DATA = []
            for item in json.load(summary_file).itervalues():
                STATE_DATA.extend(item)

@login_required
def home(request):
    check_state_data()
    return render(request, "state_summary.html", {'states': STATE_DATA})

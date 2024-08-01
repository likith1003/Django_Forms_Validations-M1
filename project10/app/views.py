from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from .models import *
# Create your views here.

def insert_skool(request):
    ESFO = SchoolForm()
    d = {'ESFO': ESFO}
    if request.method == 'POST':
        SFO = SchoolForm(request.POST)
        if SFO.is_valid():
            sname = SFO.cleaned_data['sname']
            princy = SFO.cleaned_data['princy']
            contact = SFO.cleaned_data['contact']
            loc = SFO.cleaned_data['loc']
            school = School(sname=sname, princy=princy, contact=contact, loc=loc)
            school.save()
            return HttpResponse('School Created')
        return HttpResponse('Invalid Data')
    return render(request, 'insert_skool.html', d)
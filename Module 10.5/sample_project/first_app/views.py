from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def home(request):
    example = {'list': ['what','am','I','doing'], 'val': 4, 'quote':"we'll be well",
               
        'line' : 'W K  l' , 'cur_time' : datetime.datetime.now(), 'ans': "",
        'data' : [
            {'name':'Tyler','age':20},
            {'name':'Jimmy','age':25},
            {'name':'Sky','age':32},
            {'name':'Roni','age':19},
            
        ], 'file': 47384734393, 'manga': 'Jujutsu Kaisen','test':" Hel Lo _ I am",
        'time': '10:30:00.000123+02:00', 'state': 'Happy Birthday to','num_message': 3,
        'num_tomato': 5, 'num_cherr': 1
    }
    
    
    return render (request,'first_app/index.html',context=example)
    
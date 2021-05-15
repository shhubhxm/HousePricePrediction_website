from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request, "home.html")

def result(request):

    model = joblib.load('final_model.sav')

    lis = []

    lis.append(request.GET['CRIM'])
    lis.append(request.GET['ZN'])
    lis.append(request.GET['INDUS'])
    lis.append(request.GET['CHAS'])
    lis.append(request.GET['NOX'])
    lis.append(request.GET['RM'])
    lis.append(request.GET['AGE'])
    lis.append(request.GET['DIS'])
    lis.append(request.GET['RAD'])
    lis.append(request.GET['TAX'])
    lis.append(request.GET['PTRATIO'])
    lis.append(request.GET['B'])
    lis.append(request.GET['LSTAT'])

    prediction = model.predict([lis])

    return render(request, "result.html", {'prediction': prediction})
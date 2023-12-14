from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import TextComplaint
from django.http import Http404
import time
from datetime import datetime
from .predictor import make_prediction 

def index(request):
    complaints=TextComplaint.objects.all()
    context={
        'complaints':complaints
    }
    return render(request,'index.html',context=context)



def complain(request):
    if request.method=='POST':
        complaint=request.POST['complaint']
        complaint_time=datetime.now()
        predicted_class = make_prediction(complaint)

        # text_complaint=TextComplaint(complaint=complaint,complaint_time=complaint_time)
        text_complaint=TextComplaint(complaint=complaint,complaint_time=complaint_time,predicted_class=predicted_class)
        text_complaint.save()       
        return redirect('/') 
    return render(request,'complain.html')
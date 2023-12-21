from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import TextComplaint
from django.http import Http404
import time
from datetime import datetime
from .predictor import make_prediction 
from .predict import predict_from_speech
from .models import AudioRecording
from .forms import AudioRecordingForm
from django.http import JsonResponse
from tzlocal import get_localzone


local_timezone = get_localzone()

def index(request):
    complaints=TextComplaint.objects.all()
    context={
        'complaints':complaints
    }
    return render(request,'index.html',context=context)



def complain(request):
    if request.method=='POST':
        complaint=request.POST['complaint']
        complaint_time=datetime.now(local_timezone)
        predicted_class = make_prediction(complaint)

        # text_complaint=TextComplaint(complaint=complaint,complaint_time=complaint_time)
        text_complaint=TextComplaint(complaint=complaint,complaint_time=complaint_time,predicted_class=predicted_class)
        text_complaint.save()       
        return redirect('/') 
    return render(request,'complain.html')

def record_audio(request):   
        if request.method=="POST":
            audio = request.FILES["audio"]
            text=predict_from_speech(audio)
            predicted_class = make_prediction(text) 
            complaint_time=datetime.now(local_timezone)
            text_complaint = TextComplaint.objects.create(
                complaint=text,
                complaint_time=complaint_time,
                predicted_class=predicted_class
            )  
            text_complaint.save() 
            audio_file = AudioRecording.objects.create(
                                        title=predicted_class,
                                        audio_file=audio,
                                        converted_text=text
                                                                                )
            audio_path= audio_file.audio_file.path
            return redirect('/') 
        else:            
            return render(request, "record.html")



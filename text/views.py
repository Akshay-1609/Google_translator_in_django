from django.shortcuts import render
from googletrans import Translator
import googletrans
# Create your views here.

def home(request):
    if request.method=='POST':
        len=googletrans.LANGUAGES
        txt=request.POST.get('text')
        lang=request.POST.get('lang')
        translator = Translator()
        translated = translator.translate(txt, dest=lang)
        return render(request,'index.html',{"trans":translated.text,'l':len,'txt':txt,'lang':lang})

    else:
        len=googletrans.LANGUAGES
        return render(request,'index.html',{'l':len})
from django.shortcuts import render

# Create your views here.
def hai(request):
    #d={'name':0}
    d={'a':08,'b':21,'c':20}
    return render(request,'hai.html',context=d)

def looping(request):
    d={'name':'Ghost'}
    return render(request,'looping.html',context=d)
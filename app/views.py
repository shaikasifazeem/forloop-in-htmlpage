from django.shortcuts import render
def forloop(request):
    d={'name':'shaik asif'}
    return render(request,'forloop.html',context=d)
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request,'input.html')
def add(request):
    x=request.GET["t1"]
    y=request.GET["t2"]
    i=int(x)
    j=int(y)
    z=i+j
    con_dict={"sum":z}
    return render(request,'result.html',context=con_dict)
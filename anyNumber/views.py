from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tax_rate = 15
def index(request):
  
  return render(request,"anyNumber/index.html")

def test(request,num):
  return HttpResponse(f"the ammount after tax is :{(num*tax_rate/100)+ num }")

def theTax(request):
  return HttpResponse(f"<h1>tax rate is: {tax_rate}%</h1>")


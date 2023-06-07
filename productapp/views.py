from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product
from django.views import View

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class InsertInput(View):
    def get(self,request):
        return render(request,'insertinput.html')
class Insert(View):
    def get(self,request):
        pid=int(request.GET["t1"])
        pname=request.GET["t2"]
        pcost=float(request.GET["t3"])
        pmfdt=request.GET["t4"]
        pexpdt=request.GET["t5"]
        p=product(productid=pid,productname=pname,productcost=pcost,productmfdt=pmfdt,productexpdt=pexpdt)
        p.save()
        return HttpResponse("""<html><body bgcolor=blue><h1><center>DATA UPDATED SUCCESSFULLY</center></h1></body></html>""")
class Display(View):
    def get(self,request):
        qs=product.objects.all()
        condic={"records":qs}
        return render(request,'display.html',context=condic)
class DeleteInput(View):
    def get(self,request):
        qs=product.objects.all()
        condic={"records":qs}
        return render(request, 'deleteinput.html', context=condic)
class Delete(View):
    def get(self,request):
        pid=int(request.GET["t1"])
        p=product.objects.get(productid=pid)
        p.delete()
        return redirect('/productapp/display')
class UpdateInput(View):
    def get(self,request):
        qs = product.objects.all()
        condic = {"records": qs}
        return render(request, 'updateinput.html', context=condic)
class UpdateDetails(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        prod=product.objects.get(productid=p_id)
        condic={'rec':prod}
        return render(request,'update.html',context=condic)
class Update(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        prod=product.objects.get(productid=p_id)
        prod.productname=request.GET["t2"]
        prod.productcost=float(request.GET["t3"])
        prod.productmfdt=request.GET["t4"]
        prod.productexpdt=request.GET["t5"]
        prod.save()
        return redirect('/productapp/display')

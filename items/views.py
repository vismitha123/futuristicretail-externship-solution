from django.shortcuts import render
from . import forms
from . models import Item
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse


def input_orders(request):
    form=forms.AddItem()
    return render(request,'items/inputorders.html',{'form':form})

def view_sales(request):
    return render(request,'items/viewsales.html')




def io(req):
    id=req.POST.get('item_id')
    name=req.POST.get('item_name')
    pricei=req.POST.get('price')
    quantityi=req.POST.get('quantity')
    totali=req.POST.get('total')
    instance=Item(item_id=id,item_name=name,price=pricei,quantity=quantityi,total=totali)
    instance.save()
    return render(req,'items/inputorders.html',{'message':"Success"})



def idate(req):
    datei=req.POST.get('dt')
    ins=Item.objects.filter(date=datei)
    return render(req,'items/viewsales.html',{'instances':ins})

def getpdf(req):
    all=Item.objects.all()
    data={'itemss':all}
    template=get_template("items/pdftemplate.html")
    datap=template.render(data)
    response=BytesIO()

    pdfpage=pisa.pisaDocument(BytesIO(datap.encode("UTF-8")),response)
    if not pdfpage.err:
        return HttpResponse(response.getvalue(),content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")

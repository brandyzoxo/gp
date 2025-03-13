from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from gp.forms import CommerceForm
from gp.models import Commerce


# Create your views here.
def index(request):

    if request.method == "POST":
        form=CommerceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=CommerceForm()
        return render(request,'index.html',{'form':form})


    return render(request, 'index.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def service(request):
    return render(request, 'service.html')
def starter_page(request):
    return render(request, 'starter_page.html')

def commercelist(request):
    commerce=Commerce.objects.all()
    return render(request, 'commercelist.html',{'commerce':commerce})

def updatecommerce(request,id):
    commerce=get_object_or_404(Commerce,id=id)
    if request.method == "POST":
        form=CommerceForm(request.POST,instance=commerce)
        if form.is_valid():
            form.save()
            return redirect('commercelist')
    else:
        form=CommerceForm(instance=commerce)
    return render(request, 'updatecommerce.html',{'form':form,'commerce':commerce})

def deletecommerce(request,id):
    commerce=get_object_or_404(Commerce,id=id)
    try:
        commerce.delete()
    except Exception as e:
        messages.error(request,'Error deleting commerce')
    return redirect('commercelist')


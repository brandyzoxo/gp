from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

from gp.forms import CommerceForm
from gp.models import Commerce
from gp.serializers import CommerceSerializer



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
@api_view(['GET','POST'])
def commerceapi(request):
    if request.method == "GET":
        commerce=Commerce.objects.all()
        serializer=CommerceSerializer(commerce,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        serializer=CommerceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


def signup(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
           user=form.save()
           login(request,user)
           return redirect('index')
    else:
        form=UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':form})



def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to index page after login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})












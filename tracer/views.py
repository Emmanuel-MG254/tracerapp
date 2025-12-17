

from django.shortcuts import render, redirect

from tracer.models import Contact, Sea
from tracer.models import Index
from tracer.models import Price


# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        note = request.POST.get('note')
        query = Index(name=name,email=email,mobile=mobile,note=note)
        query.save()
        return redirect("/")

    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        query =Contact(name=name,email=email,subject=subject,message=message)
        query.save()
        return redirect("/")

    return render(request,'contact.html')
def feature(request):
    return render(request,'feature.html')
def price(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        note = request.POST.get('note')
        query = Price(name=name,email=email,mobile=mobile,note=note)
        query.save()
        return redirect("/")
    return render(request,'price.html')
def services(request):
    return render(request,'service.html')
def quote(request):
    return render(request,'quote.html')
def team(request):
    return render(request,'team.html')
def testimonial(request):
    return render(request,'testimonial.html')
def four(request):
    return render(request,'404.html')
def sea(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        message = request.POST.get('message')
        query = Sea (name=name,email=email,company=company,message=message)
        query.save()
        return redirect("/")
    return render(request,'sea-freight.html')
def air(request):
    return render(request,'air freight.html')
def road(request):
    return render(request,'road-freight.html')
def terms(request):
    return render(request,'Terms-and-conditon.html')
def logistics(request):
    return render(request,'logistics.html')
def support(request):
    return render(request,'support.html')


from django.shortcuts import render
from django.contrib import messages
from .models import GetinTouch,OnlineTraining,ApplyForProject

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def content(request):
    return render(request,'content.html')

def services(request):
    return render(request,'services.html')

def logout(request):
    return render(request,'index.html')

def register(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email=request.POST.get('email')
        phone = request.POST.get('phone')
        collage = request.POST.get('collage')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        if not name or not email or not phone or not collage or not branch or not year:
            messages.error(request, 'All fields are required.')
            return render(request, 'content.html', {'name': name,'email': email,'phone': phone,'collage': collage,'branch': branch,'year':year})        
        user_registration = ApplyForProject(name=name,email=email,phone=phone,collage=collage,branch=branch,year=year)
        user_registration.save()
        messages.success(request, 'You have been successfully registered wait Our Team Will Call You.')  
     
     return render(request,'onlinetraining.html')

def register1(request):    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')  
        collage = request.POST.get('collage')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        if not name or not email or not phone or not collage or not branch or not year:
            messages.error(request, 'All fields are required.')
            return render(request, 'content.html', {'name': name,'email': email,'phone': phone,'collage': collage,'branch': branch,'year':year})        
        user_registration = ApplyForProject(name=name,email=email,phone=phone,collage=collage,branch=branch,year=year)
        user_registration.save()
        messages.success(request, 'You have been successfully registered wait Our Team Will Call You.')  
        
    return render(request,'project.html')

def getintouch(request):     
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if not name or not email or not phone or not subject or not message:
            messages.error(request, 'All fields are required.')
            return render(request, 'content.html', {'name': name,'email': email,'phone': phone,'subject': subject,'message': message,})        
        user_registration = GetinTouch(name=name,email=email,phone=phone,subject=subject,message=message,)
        user_registration.save()
        messages.success(request, 'You have been successfully registered wait Our Team Will Call You.')       
    return render(request, 'content.html')

# def onlinetraining(request):   
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         print(name)
#     #     print("*"*30)
#     #     print(name)
#     #     print("*"*30)

#     #     email = request.POST.get('email')
#     #     phone = request.POST.get('phone')
#     #     collage = request.POST.get('collage')
#     #     branch = request.POST.get('branch')
#     #     year = request.POST.get('year')
#     #     print(year)
#     #     print(name,email,phone,collage,branch,year)
#     #     if not name or not email or not phone or not collage or not branch or not year:
#     #         messages.error(request, 'All fields are required.')
#     #         return render(request, 'onlinetraining.html', {'name': name,'email': email,'phone': phone,'collage': collage,'branch': branch,'year':year})        
#     #     user_registration1 = OnlineTraining(name=name,email=email,phone=phone,collage=collage,branch=branch,year=year)
#     #     user_registration1.save()
#     #     messages.success(request, 'You have been successfully registered wait Our Team Will Call You.')       
#     return render(request, 'onlinetraining.html')

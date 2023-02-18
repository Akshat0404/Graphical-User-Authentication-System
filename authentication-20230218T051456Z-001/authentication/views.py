from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate, login as auth_login, logout 
from .connection import *
import random as rand
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import time
from django.contrib.auth.decorators import login_required

class mainfunc():

    def signup(request):
        params = {
            'i1':"d_images/"+str(rand.randint(1,100))+".jpg",'i2':"d_images/"+str(rand.randint(1,100))+".jpg",
            'i3':"d_images/"+str(rand.randint(1,100))+".jpg",'i4':"d_images/"+str(rand.randint(1,100))+".jpg",
            'i5':"d_images/"+str(rand.randint(1,100))+".jpg",'i6':"d_images/"+str(rand.randint(1,100))+".jpg",
            'i7':"d_images/"+str(rand.randint(1,100))+".jpg",'i8':"d_images/"+str(rand.randint(1,100))+".jpg",
            'i9':"d_images/"+str(rand.randint(1,100))+".jpg"
        }

        if request.method=="POST":
            d_img = request.POST.get('avatar')
            d_img1 = request.POST.get('avatar1')
            d_img2 = request.POST.get('avatar2')
            mail = request.POST.get('email')
            passwd = " ".join([d_img, d_img1, d_img2])
            print(passwd)
            print(mail)
            c_user = User.objects.create_user(mail,passwd)
            c_user.save()
            return redirect('correct')
        return render(request,"sign_up.html",params)
    
    def login(request):
        try:
            if request.method == "POST":
                mail = request.POST.get('email')
                return HttpResponseRedirect('/password/?email={}'.format(mail))
        except:
            return redirect("wrong")
        return render(request, "login.html")

    def password(request):
        try:
            mail = request.GET.get('email')
            cursor = connection.cursor()
            cursor.execute('SELECT u_img FROM authentication_user WHERE email=%s', [mail])
            result = cursor.fetchone()
            a = result[0].split(" ")
            l =[]
            for i in range(0,3):
                b = a[i].split("/static/")
                l.append(b[1])
            params = {
                'i1':l[0],'i2':"d_images/"+str(rand.randint(1,100))+".jpg",
                'i3':"d_images/"+str(rand.randint(1,100))+".jpg",'i4':"d_images/"+str(rand.randint(1,100))+".jpg",
                'i5':l[1],'i6':"d_images/"+str(rand.randint(1,100))+".jpg",
                'i7':"d_images/"+str(rand.randint(1,100))+".jpg",'i8':"d_images/"+str(rand.randint(1,100))+".jpg",
                'i9':l[2]
            }
            if request.method=="POST":
                d_img = request.POST.get('avatar')
                d_img1 = request.POST.get('avatar1')
                d_img2 = request.POST.get('avatar2')
                try:
                    passwd = " ".join([d_img, d_img1, d_img2])
                    user = authenticate(request, email=mail, password=passwd)
                    if user is not None:
                        auth_login(request, user)
                        time.sleep(3)
                        return redirect('dashboard') 
                    else:
                        return redirect('wrong')
                except Exception as e:
                    return redirect('wrong')
        except:
            return redirect('wrong')
        return render(request, "password.html", params)
    
    @login_required
    def dashboard(request):
        return render(request, "dashboard.html")
    
    def wrong(request):
        return render(request, "wrong.html")

    def correct(request):
        return render(request, "correct.html")
    
    @login_required
    def logout(request):
        time.sleep(3)
        logout(request)
        return redirect('login')


# @csrf_exempt
# def img(request):
#     params = {
#         'i1':"d_images/"+str(rand.randint(1,100))+".jpg",'i2':"d_images/"+str(rand.randint(1,100))+".jpg",
#         'i3':"d_images/"+str(rand.randint(1,100))+".jpg",'i4':"d_images/"+str(rand.randint(1,100))+".jpg",
#         'i5':"d_images/"+str(rand.randint(1,100))+".jpg",'i6':"d_images/"+str(rand.randint(1,100))+".jpg",
#         'i7':"d_images/"+str(rand.randint(1,100))+".jpg",'i8':"d_images/"+str(rand.randint(1,100))+".jpg",
#         'i9':"d_images/"+str(rand.randint(1,100))+".jpg"
#     }
#     if request.method == "POST":
#         d_img = request.POST.get("data")
#         if d_img is not None:
#             # a = loda.split()
#             print(d_img)
#             # print(params[("i"+a[0])])
#         else:
#             print("maa chuda")
#     return render(request, "image.html",params)
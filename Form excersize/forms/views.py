from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .models import User1s
from .forms import NewUserForm, UserForm
from datetime import datetime, date
from .forms import UserProfileInfoForm
#*user models and froms excersize
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the forms INDEX function from VIEWS.PY. </br> Following ip adress type /index, /users or /form insde the browser to go to accual template page. <br> Another pages are under /templateurl, /other and /relatives. <br> For User Models& Forms type /user_page.")

#*  View for forms REGISTER and LOGIN
def form_view(request):
    return render(request, 'forms/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #do some code
            print('VALIDATION SUCCESS!')
            #grab the data
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])


    return render(request, 'forms/form_page.html', {'form':form})

#*View for User file and faker excersize
def users(request):
    #*create user = and grab all those objects and order by first name
    user_list = User1s.objects.order_by('first_name')
    #*create user list [key:value]
    user_dictionary = {'users':user_list}
    return render(request, 'forms/users.html', context=user_dictionary)

def users2(request):
    #*create new variable and asign newuserform to it
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return form_view(request)
        else:
            print('ERROR')

    return render(request, 'forms/users2.html', {'form':form})


#*URLS TEMPLATES EXCERSISE & TEMPLATE FILTERS
def template_url(request):
    context_dictionary = {'text':'Hello world, i am some dictionary','number':[100, 200, 300, 400, 500, 600], 'tekst':'I am a filter.', 'data':datetime.now()}
    return render(request,'forms/templateurls.html', context_dictionary)

def other(request):
    context_dictionary = {'text':'Hello world, i am some dictionary','number':[100, 200, 300, 400, 500, 600], 'tekst':'I am a filter.','data':datetime.now()}
    return render(request,'forms/other.html', context_dictionary)

def relatives(request):
    context_dictionary = {'data':datetime.now()}
    return render(request, 'forms/relative_url_templates.html',context_dictionary)

#*User Model and Forms
def user_page_index(request):
    return render(request, 'forms/user_page_index.html')

@login_required
def special(request):
    return HttpResponse("You are logged-in !!!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_index'))

def user_register(request):
    registered = False
    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():


            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'forms/user_page_registration.html',{'user_form':user_form, 'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('user_index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("SOMEONE TRIED AND FAILED!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("INVALID LOGIN DETAILS SUPLIED!")
    else:
        return render(request, 'forms/user_page_login.html',{})
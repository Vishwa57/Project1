from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Employee, Sal_details
from . import forms

# Create your views here.

def func(request):
    #return HttpResponse("<em>Hello Vishwa! Welcome to the new venture.</em>")
    my_dict = {'insert_here' : 'Now we are from views.py '}
    my_dict['sal_info']= Sal_details.objects.all()
    return render(request, 'app1/index.html', context=my_dict)

def users(request):
    mydict = {'user_info': Employee.objects.all()}
    return render(request, 'app1/users.html', context = mydict)

def Form_view(request):
    form_list = forms.Form_name()
    if request.method == 'POST':
        form = forms.Form_name(request.POST)

        if form.is_valid():
            
            # DO SOMETHING CODE
            # this will directly print the input in the console
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    form_dict = {'insert_form': form_list}
    return render(request, 'app1/forms.html', context=form_dict)

def ModelForm(request):
    form = forms.Model_form()
    if request.method == 'POST':
        form = forms.Model_form(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return sucess_page(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'app1/Signup.html',{'form_info':form})

def sucess_page(request):
    return render(request, 'app1/Success.html')

def base(request):
    return render(request, 'app1/base.html')

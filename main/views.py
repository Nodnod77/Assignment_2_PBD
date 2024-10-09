from django.shortcuts import render, redirect , reverse
from main.forms import FormEntryForm
from main.models import FormEntry
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages 
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    user = request.user
   
    print("shoow")
    context = {
        'npm' : '2406394906 ',
        'name': 'Donia Sakji',
        'login name' : request.user.username,
        'class': 'PBP KKI',
        'appName': 'nodnodShop',
        'last_login': request.COOKIES.get('last_login', 'Never') ,
    }

    return render(request, "main.html", context)



def create_form_entry(request):
    print("aaaaaaaaaaaa")
    form = FormEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form_entry = form.save(commit=False)
        form_entry.user = request.user  
        form_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_form_entry.html", context)
    
def show_xml(request):
    data = FormEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")    

def show_json(request):
    print("show_json")
    data = FormEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = FormEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = FormEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

##login lgout
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else :
        messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def edit_product(request, id):
    # Get form entry based on id
    product = FormEntry.objects.get(pk = id)

    # Set form entry as an instance of the form
    form = FormEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get form based on id
    product = FormEntry.objects.get(pk = id)
    # Delete form
    product.delete()
    # Return to home page
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_form(request, id):
    # Get form entry based on id
    form = FormEntry.objects.get(pk = id)

    # Set form entry as an instance of the form
    form = FormEntryForm(request.POST or None, instance=form)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_form.html", context)

def delete_form(request, id):
    # Get form based on id
    form = FormEntry.objects.get(pk = id)
    # Delete form
    form.delete()
    # Return to home page
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_form_entry_ajax(request):
    data1 = strip_tags (request.POST.get("data1") )
    print(data1,"je suis iciii 1")
    data2 = strip_tags (request.POST.get("data2"))
    print(data2,"je suis iciii 2")
    data3 = request.POST.get("data3")
    print(data3,"je suis iciii 3")
    user = request.user
    print(user,"je suis iciii 4")
    new_form = FormEntry(
        data1=data1, data2=data2,
        data3=data3,
        user=user
    )
    new_form.save()

    return HttpResponse(b"CREATED", status=201)

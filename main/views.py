from django.shortcuts import render, redirect
from main.forms import FormEntryForm
from main.models import FormEntry
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    form_entries = FormEntry.objects.all()

    context = {
        'npm' : '2406394906 ',
        'name': 'Donia Sakji',
        'class': 'PBP KKI',
        'appName': 'nodnodShop',
        'form_entries': form_entries,
    }

    return render(request, "main.html", context)



def create_form_entry(request):
    form = FormEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_form_entry.html", context)
    
def show_xml(request):
    data = FormEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")    

def show_json(request):
    data = FormEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = FormEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = FormEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
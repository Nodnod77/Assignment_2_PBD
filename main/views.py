from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406394906 ',
        'name': 'Donia Sakji',
        'class': 'PBP KKI',
        'appName': 'nodnodShop',
    }

    return render(request, "main.html", context)
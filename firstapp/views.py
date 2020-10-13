from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def index(request):
    header = "Personal Data"  # обычная переменная
    langs = ["English", "German", "Spanish"]  # массив
    user = {"name": "Tom", "age": 23}  # словарь
    addr = ("Botanicheskaya", 23, 45)  # кортеж

    data = {"header": header, "langs": langs, "user": user, "address": addr}
    # return render(request, "index.html", context=data)
    # return TemplateResponse(request,  "index.html", data) # analog
    return render(request, "index2.html", context={"langs": langs})

def about(request):
    return HttpResponse("<h2>About Web-Site </h2>")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def products(request, productid=1):
    category = request.GET.get("cat", "")
    output = "<h2>Product № {0}  Category: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request, id=0, name="Sabina"):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tom")
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)


def forms(request):
    '''if request.method == "POST":
        name = request.POST.get("name")
        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    else:
        userform = UserForm()
        return render(request, "firstapp/form.html", {"form": userform})
'''
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse("<h2>Hello, {0}</h2>".format(name))
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm()
        return render(request, "firstapp/form.html" , {"form": userform})
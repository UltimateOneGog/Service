from django.contrib import admin
from django.urls import path
from django.urls import re_path
from firstapp import views
from django.views.generic import TemplateView

urlpatterns = [
    #re_path(r'^about/contact', views.contact),
    #re_path(r'^about', views.about),
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('contact', views.contact),
    path('details', views.details),

    re_path(r'^products/(?P<productid>\d+)/', views.products),
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),

    path('products/', views.products),
    path('products/<int:productid>/', views.products),

    path('users/', views.users),
    path('users/<int:id>/<str:name>/', views.users),
    path('form', views.forms),

    path('about/', TemplateView.as_view(template_name="firstapp/about.html",extra_context={"header": "About from template view"})),
    path('contact/', TemplateView.as_view(template_name="firstapp/contact.html")),
]

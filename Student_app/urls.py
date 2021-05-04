from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('add1', views.add1, name ='add1'),
    path('add', views.add, name ='add'),
    # path('view', views.view, name ='view'),

]
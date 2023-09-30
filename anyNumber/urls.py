from django.urls import path
from . import views
urlpatterns = [path("", views.index,name="index"),
               path("<int:num>", views.test,name="number1"),
               path("taxrate/", views.theTax,name="tax")]
               
              


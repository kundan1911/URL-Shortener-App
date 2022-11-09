from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path(endpointname,renderthisfunctionforresponse)
    path('hello',views.hw),
    path('',views.home_page)
]                                                                                                                                                                                      
                                                       
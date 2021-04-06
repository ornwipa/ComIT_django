"""cool_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_app.views import get_current_time, hello_world
# from people.views import display_person_info
from people.views import AllEmails, PersonInfo, PersonListView

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('current_time/', get_current_time, name='current_time'),
    path('hello_world/<name>/<int:number>', hello_world), # take variables from the URL
    # path('display_person/<slug:pk>', display_person_info) # pk = primary key (as ascii)
    path('display_person/<slug:pk>', PersonInfo.as_view(), name='display-person'),
    path('people/', PersonListView.as_view(), name='people-list'),
    path('people/emails/', AllEmails.as_view(), name='people-emails-list')
]

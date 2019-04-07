"""March5Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from testapp import views
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', views.first_page),
    url(r'^first_page/', views.first_page),
    url(r'^login/', views.loginview),
    url(r'^register/', views.register),
    url(r'^docs_detail/', views.docs_detail_view),
    url(r'^section_detail/', views.section_detail_view),
    url(r'^log_out/', views.log_out),

]


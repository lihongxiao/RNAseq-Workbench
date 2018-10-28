"""transWorkbench URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from application.views import *
urlpatterns = [
    url(r'^transworkbench_main$',main),
    url(r'^transworkbench_main$',main, name='mainpage'),
    url(r'^help/$',helppage, name='help'),
    url(r'^login/$',log, name='login'),
    url(r'^signup/$',signUp, name='sign up'),
    url(r'^username/$',userpage, name='userpage'),
    url(r'^home/$',userpage, name='home'),
    url(r'^platform/$',platPage, name='RNASeqForm'),
    url(r'^RNASequencing_mRNASeq/$',mRNASeq, name='mRNASeq'),
    url(r'^RNASequencing_mRNASeq_Analysis/$',anaysisPage, name='analysis'),
]

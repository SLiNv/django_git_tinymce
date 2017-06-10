"""django_git URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from . import views

app_name = "repos"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create/$', views.createRepo, name='create'),
    url(r'^(?P<pk>.*)/change/$', views.deleteRepo, name='change'),
    url(r'^(?P<pk>.*)/delete/$', views.deleteRepo, name='delete'),
    url(r'^(?P<pk>.*)/setting/$', views.repoSetting, name='setting'),
    url(r'^(?P<pk>.*)/$', views.RepositoryDetailView.as_view(), name='detail'),
]

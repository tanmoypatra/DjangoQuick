"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from tutorial.quickstart import views as views1
from snippets import views as views


router = routers.DefaultRouter()
router.register(r'users', views1.UserViewSet)
router.register(r'groups', views1.GroupViewSet)
admin.autodiscover()



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest-framework')),
    url(r'^admin/', include(admin.site.urls))
]

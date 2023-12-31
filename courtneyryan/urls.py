"""courtneyryan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from ninja import NinjaAPI
from ninja import Schema

from django.conf import settings
from django.conf.urls.static import static
from courtneyOracle import views as blog_views

from courtneyOracle.api.v1.routers.dataconnectors import router as dataconnectors_router
from courtneyOracle.api.v1.routers.scrape import router as scrape_router

#We add all the routers in urls.py
api = NinjaAPI()
api.add_router("/dataconnectors/",dataconnectors_router)
api.add_router("/scrape/",scrape_router)

urlpatterns = \
[
    path("admin/", admin.site.urls),
    path("api/",api.urls),
    path("",blog_views.home,name="home")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
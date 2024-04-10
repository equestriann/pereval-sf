"""
URL configuration for pereval_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path, include
from rest_framework import routers
from pereval.views import *


# # Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UsersViewset)
# router.register(r'coords', CoordsViewset)
# router.register(r'levels', LevelViewset)
# router.register(r'images', ImageViewset)
# router.register(r'Pereval', PassViewset)

urlpatterns = [
    path('', include(router.urls)),
    # path('Pereval', include('rest_framework.urls', namespace='rest_framework')),
    path('Pereval/', PassViewset.as_view())
]

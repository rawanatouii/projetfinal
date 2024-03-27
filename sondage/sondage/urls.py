"""
URL configuration for sondage project.

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
from data.api import SondageViewSet, QuestionViewSet, ReponseViewSet

router = routers.DefaultRouter()
router.register(r'sondages', SondageViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'reponses', ReponseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/users/', include('data.users.urls')),
]
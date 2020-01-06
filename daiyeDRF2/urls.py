"""daiyeDRF2 URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

# 导入DRF的路由
from rest_framework import routers

# 导入视图
from MySer import views

router = routers.SimpleRouter()

#router.register(r'Student',views.StudentVS, base_name='stu')
router.register(r'apiview',views.StudentAPIView.as_view(), base_name='stuapi')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/', include(router.urls)),
    url(r'^apiview/', views.StudentAPIView.as_view()),
    url(r'^genapiview/', views.StudentGenAPIView.as_view()),
    url(r'^stuviewset/', views.StudentViewSet),
]

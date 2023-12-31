"""
URL configuration for study_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include


# 스프링의 컨트롤러같은 느낌
urlpatterns = [
    path('admin/', admin.site.urls),

    # include를 통해서 main 앱에 있는 url들을 모두 연결시켜준다.
    path('', include('main.urls')),
    path('board/', include('board.urls')),
    path('api/', include('restPractice.urls')),
]

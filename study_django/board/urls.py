from django.urls import path
from . import views


# board/write
urlpatterns = [
    path('write', views.gowrite, name='write'),
    path('save', views.writeBoard, name="writeBoard"),
    path('list', views.goList)
]

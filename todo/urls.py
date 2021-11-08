from django.urls import path
from .views import *;
urlpatterns = [
    path('', home, name='index'),
    path('<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('clearall/', clearAll, name='clearall'),
]

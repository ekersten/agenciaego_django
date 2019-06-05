from django.urls import path

from . import views

urlpatterns = [
    path('like/<int:page_id>/', views.like, name='like'),
    path('unlike/<int:page_id>/', views.unlike, name='unlike')
]

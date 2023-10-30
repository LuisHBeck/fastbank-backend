from django.urls import path, include

urlpatterns = [
  #DJOSER
  path('', include('djoser.urls.jwt')),
]

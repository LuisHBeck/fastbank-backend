from django.contrib import admin
from django.urls import path, include

from core.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('core.urls')),

    path('api/v1/auth/', include('users.urls')) 
]

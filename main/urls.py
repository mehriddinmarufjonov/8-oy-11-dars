from django.urls import path, include
from .views import KundalikView
from rest_framework import routers


router = routers.SimpleRouter()
router.register('kundalik', KundalikView)


urlpatterns = [
    
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
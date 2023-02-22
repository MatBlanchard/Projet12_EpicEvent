from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.views import SignupViewSet, ClientViewSet, ContractViewSet, EventViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register('', SignupViewSet, basename='signup')
router.register('clients', ClientViewSet, basename='client')
router.register('contracts', ContractViewSet, basename='contract')
router.register('events', EventViewSet, basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]

from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import viewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='v1',
      description="Student Information",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
	# path('api-token-auth/', obtain_auth_token,name='token'),
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
	path('studentapi', views.Student1.as_view()),
	path('studentapi/post', views.Student2.as_view()),
	path('studentapi/put', views.Student3.as_view()),
	path('studentapi/delete', views.Student4.as_view()),
	path('studentapi/<int:pk>/', views.getStudent.as_view()),
	path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	path('gettoken/', TokenObtainPairView.as_view(), name = 'gettoken'),
	path('refreshtoken/', TokenRefreshView.as_view(), name = 'refreshtoken'),
	path('verifytoken/', TokenVerifyView.as_view(), name = 'verifytoken'),






]
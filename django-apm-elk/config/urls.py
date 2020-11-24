from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [

    path("", include(("ness_elastic.base.urls", "base"), namespace='v1')),

    # User management
    path("api/users/", include("ness_elastic.users.urls", namespace="users")),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]


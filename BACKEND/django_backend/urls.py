from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include, re_path
from accounts.models import CustomAuthToken

from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth import views as auth_views

from rest_framework import permissions 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi

schema_url_v1_patterns = [
    url(r'^api/surveys/', include('surveys.urls')),
]
schema_view_v1 = get_schema_view(
    openapi.Info( 
        title="Django API", 
        default_version='v1', 
        description="안녕하세요. B108의 Open API 문서 페이지 입니다.",
        terms_of_service="https://www.google.com/policies/terms/", 
        ), 
        public=True, 
        permission_classes=(permissions.AllowAny,), 
        patterns=schema_url_v1_patterns,
    )


urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('api/surveys/',include('surveys.urls')),
    path('api/accounts/',include('accounts.urls')),
    path('api/ai/',include('ai.urls')),

    #rest-auth
    path('api/api-token-auth/',CustomAuthToken.as_view()), #이걸로 로그인!
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/signup/', include('rest_auth.registration.urls')),

    #password
    path('api/reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('api/reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('api/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('api/reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

    url(r'^swagger(?P<format>\.json|\.yaml)/v1$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/v1/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/v1/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
]
#urlpatterns  += doc_urls
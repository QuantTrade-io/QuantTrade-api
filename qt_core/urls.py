from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

auth_patterns = [
    # path('', include(auth_auth_patterns)),
    # path('followings/', include(auth_followings_patterns)),
    # path('followers/', include(auth_followers_patterns)),
    # path('linked-users/', include(auth_linked_users_patterns)),
    # path('blocked-users/', include(auth_blocked_users_patterns)),
    # path('users/', include(auth_users_patterns)),
    # path('user/', include(auth_user_patterns)),
    # path('proxy/', ProxyAuth.as_view(), name='proxy-auth'),
]


api_patterns = [
    path("auth/", include(auth_patterns)),
]


urlpatterns = [
    path("api/", include(api_patterns)),
    url("admin/", admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path # new
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')), # new
    path('api-auth/', include('rest_framework.urls')), # new
]
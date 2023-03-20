from django.urls import include, path
from rest_framework import routers
from hello_world.core import views

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('testendpoint/', views.basic_endpoint)
] # okay, so 


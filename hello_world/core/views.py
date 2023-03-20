from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from hello_world.core.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse

# Going to want to create a new viewset? Also has to handle post information too

from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



def basic_endpoint(request):
    # Okay, so something here taking in the request information, and returning what needs to be returned. Cool
    return HttpResponse('Test Complete') # So this is where I'm going to call whatever functions are necessary to parse the HTML... I should set this up differently as a endpoint, that quickstart was kinda trash

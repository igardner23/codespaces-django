
from django.http import HttpResponse

# Going to want to create a new viewset? Also has to handle post information too

from django.http import HttpResponse


def basic_endpoint(request):
    # Okay, so something here taking in the request information, and returning what needs to be returned. Cool
    return HttpResponse('Test Complete') # So this is where I'm going to call whatever functions are necessary to parse the HTML... I should set this up differently as a endpoint, that quickstart was kinda trash

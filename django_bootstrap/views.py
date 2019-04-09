from dramatiq.broker import get_broker

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.urls import reverse


@staff_member_required
def hello_world_actor(request):
    broker = get_broker()
    actor = broker.get_actor("hello_world")
    actor.send()

    messages.add_message(request, messages.INFO, "Hello world actor called")
    return HttpResponseRedirect(reverse("admin:index"))

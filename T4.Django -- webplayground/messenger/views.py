from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.http import Http404, JsonResponse
from .models import Thread, Message
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ThreadListView(TemplateView):
    template_name = 'messenger/thread_list.html'

class ThreadDetailView(DetailView):
    model = Thread

    def get_object(self):
        obj = super(ThreadDetailView, self).get_object()
        if not self.request.user in obj.user.all():
            raise Http404()
        return obj
    
def add_message(request, pk):
    json_response = {'created': False}
    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
            if len(thread.messages.all()) > 0:
                json_response['first'] = True
    else:
        raise Http404("User not authenticated")
    
    return JsonResponse(json_response)

@login_required
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))
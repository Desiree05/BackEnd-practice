from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class ThreadManager(models.Manager):
    def find(self, user1, user2):
        queryset = self.filter(user=user1).filter(user=user2)
        if len(queryset) > 0:
            return queryset[0]
        return None
    
    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.user.add(user1, user2)
        return thread

class Thread(models.Model):
    user = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
    updated = models.DateTimeField(auto_now=True)

    objects = ThreadManager()

    class Meta:
        ordering = ['-updated']

def message_changed(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    action = kwargs.pop('action', None)
    pk_set = kwargs.pop('pk_set', None)
    print(instance, action, pk_set)

    false_pk_set = set()

    if action == "pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.user.all():
                print("{} no pertenece a los usuarios del hilo".format(msg.user))
                false_pk_set.add(msg_pk)

    # Buscar los mensajes que no pertenecen a los usuarios del hilo
    # y eliminarlos de la relación, si estan en pk_set
    pk_set.difference_update(false_pk_set)

    # Forzar la actualizacion del campo updated
    instance.save()


m2m_changed.connect(message_changed, sender=Thread.messages.through)
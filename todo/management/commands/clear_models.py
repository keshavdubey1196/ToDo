from django.core.management.base import BaseCommand
from todo.models import Task


class TodoBaseCommand(BaseCommand):
    def handle(self, *args, **kwargs):
        Task.objects.all().delete()

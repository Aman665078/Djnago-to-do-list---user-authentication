from .models import Task
from django.contrib.auth.models import User
from datetime import datetime

# Create a task manually in Django shell with created datetime set
user = User.objects.first()
task = Task(user=user, title="Test Task", description="Description", complete=False, created=datetime.now())
task.save()

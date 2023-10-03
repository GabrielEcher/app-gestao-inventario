from django.views.generic.list import ListView
from .models import InvItem
from django.utils import timezone

class Inventory(ListView):
    model = InvItem
    template_name = 'inv_manager/index.html'
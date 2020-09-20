from django.views import generic
from .models import Page


# Create your views here.
class PageDetail(generic.DetailView):
    model = Page
    template_name = 'sections/page.html'

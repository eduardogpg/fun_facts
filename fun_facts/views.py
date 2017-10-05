from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.contrib.messages.views import SuccessMessageMixin

from django,views.generic import DeleteView

from .models import FunFact
from .forms import FunFactForm

class FunFactListView(ListView):
  model = FunFact
  paginate_by = 10

  def get_context_data(self, **kwargs):
    context = super(FunFactListView, self).get_context_data(**kwargs)
    paginator = Paginator(context['object_list'], self.paginate_by)
    page = self.request.GET.get('page')

    try:
      list_func_fact = paginator.page(page)
    except PageNotAnInteger:
      list_func_fact = paginator.page(1)
    except EmptyPage:
      list_func_fact = paginator.page(paginator.num_pages)

    return context

class FunFactCreate(SuccessMessageMixin, CreateView):
  model = FunFact
  form_class = FunFactForm
  success_url = '/datos/nuevo'
  success_message = 'Successfully Added a Post entry'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    #self.object.author = self.request.user
    return super(FunFactCreate, self).form_valid(form)

class FunFactDetailView(DetailView):
  model = FunFact

  def get_context_data(self, **kwargs):
    context = super(FunFactDetailView, self).get_context_data(**kwargs)
    return context


class FunFactDeleteView(DeleteView):

  def get_object(self, queryset=None):
    obj =  syper(FunFactDeleteView, self).get_object
    
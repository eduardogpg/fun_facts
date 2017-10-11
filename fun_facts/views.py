from django.core.urlresolvers import reverse
from django.urls import reverse_lazy


from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.contrib.messages.views import SuccessMessageMixin

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
  success_message = 'Dato creado exitosamente'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    return super(FunFactCreate, self).form_valid(form)

class FunFactDetailView(DetailView):
  model = FunFact   

  def get_context_data(self, **kwargs):
    context = super(FunFactDetailView, self).get_context_data(**kwargs)
    return context

class FunFactEditView(SuccessMessageMixin, UpdateView):
  model = FunFact
  form_class = FunFactForm
  success_message = 'Dato editado exitosamente'
  template_name_suffix = '_update_form'

  def get_success_url(self):
    return reverse("fun_fact_edit", kwargs={'pk': self.object.pk})

class FunFactDeleteView(SuccessMessageMixin, DeleteView):
  model = FunFact
  success_url = reverse_lazy('fun_fact_list')
  success_message = 'Dato eliminado correctamente'


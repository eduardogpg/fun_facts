from django.conf.urls import url
from .views import FunFactListView, FunFactCreate, FunFactDetailView, FunFactEditView, FunFactDeleteView

#r'^(?P<slug>[-\w]+)/$

urlpatterns = [
  url(r'^$', FunFactListView.as_view(), name='fun_fact_list'),
  url(r'^nuevo$', FunFactCreate.as_view(), name='fun_fact_new'),
  url(r'^(?P<pk>[0-9]+)/$',FunFactDetailView.as_view(), name='fun_fact_detail'),
  url(r'^(?P<pk>[0-9]+)/editar$',FunFactEditView.as_view(), name='fun_fact_edit'),
  url(r'^(?P<pk>[0-9]+)/eliminar$',FunFactDeleteView.as_view(), name='fun_fact_delete'),
]
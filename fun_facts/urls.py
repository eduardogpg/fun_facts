from django.conf.urls import url
from .views import FunFactListView, FunFactCreate, FunFactDetailView

urlpatterns = [
  url(r'^$', FunFactListView.as_view(), name='fun_fact_list'),
  url(r'^nuevo$', FunFactCreate.as_view(), name='fun_fact_new'),
  url(r'^(?P<pk>[0-9]+)/$',FunFactDetailView.as_view(), name='fun_fact_detail'),
  url(r'^(?P<pk>[0-9]+)/eliminar$',FunFactDetailView.as_view(), name='fun_fact_delete'),
  url(r'^(?P<pk>[0-9]+)/actualizar$',FunFactDetailView.as_view(), name='fun_fact_update'),
]
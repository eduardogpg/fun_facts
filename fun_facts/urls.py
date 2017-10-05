from django.conf.urls import url
from .views import FunFactListView, FunFactCreate

urlpatterns = [
  url(r'^$', FunFactListView.as_view(), name='fun_fact_list'),
  url(r'^nuevo$', FunFactCreate.as_view(), name='fun_fact_new'),
]

from django.shortcuts import render
from django.shortcuts import redirect


from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.views.generic import View

from .forms import LoginForm

def index(request):
  template = loader.get_template('index.html')
  context = {}
  return HttpResponse(template.render(context, request))

class SignIn(View):
  form = LoginForm()
  message = None
  template = 'sign_in.html'

  def get(self, request, *args, **kwargs):
    return render(request, self.template, self.get_context() )

  def post(self, request, *args, **kwargs):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
      login(request, user)
      return redirect('fun_fact_list')
    else:
      print("Entro aqui")
      self.message = "username o password incorrectos."
    return render(request, self.template, self.get_context() )

  def get_context(self):
    return {'form': self.form, 'message' : self.message}

@login_required( login_url = 'client:login' )
def logout(request):
  logout_django(request)
  return redirect('sign_in')
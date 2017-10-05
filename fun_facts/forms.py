#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import FunFact

bootstrap_class = {'class': 'form-control'}

ERROR_MESSAGE_TITLE = {'required' : 'El titulo es requerido'}
ERROR_MESSAGE_DESCRIPTION = {'required' : 'La descripción es requerida'} 


def validate_title(title):
  if len(title) < 2:
    raise forms.ValidationError('Debe contener por lo menos 2 caracteres.')
  
  if len(title) > 20:
    raise forms.ValidationError('Debe contener un máximo de 20 caracteres.')

def validate_description(description):
  if len(description) < 5:
    raise forms.ValidationError('Debe contener por lo menos 5 caracteres.')
  
  if len(description) > 250:
    raise forms.ValidationError('Debe contener un máximo de 250 caracteres.')

class FunFactForm(forms.ModelForm):
  title = forms.CharField(label='Título', required=True, error_messages=ERROR_MESSAGE_TITLE,
                          validators=[validate_title],
                          widget=forms.TextInput(attrs=bootstrap_class))
  
  description = forms.CharField(label='Descripción', required=True, error_messages=ERROR_MESSAGE_DESCRIPTION,
                          validators=[validate_description],
                          widget=forms.Textarea(attrs=bootstrap_class))
  
  is_true = forms.BooleanField(label='Verdadero',
                          widget=forms.CheckboxInput())

  def __init__(self, *args, **kwargs):
    super(FunFactForm, self).__init__(*args, **kwargs)

  class Meta:
    model = FunFact
    fields = ('title', 'description', 'is_true')

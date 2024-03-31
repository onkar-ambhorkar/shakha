from django.contrib import admin
from django import forms

from .models import Model


class Form(forms.ModelForm):
    class Meta:
        model = Model
        exclude = ("",)


class Admin(admin.ModelAdmin):
    form = Form


admin.site.register(Model, Admin)

from django.shortcuts import render
from django.views import View

from .forms import UserForm

class RegistrationView(View):
    template = 'ui/signup.html'
    form = UserForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {'form': self.form})

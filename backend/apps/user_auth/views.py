from django.urls import reverse_lazy
from django.views import generic
from .forms import CreationUserForm
from django.contrib import messages


class SignUpView(generic.CreateView):
    form_class = CreationUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

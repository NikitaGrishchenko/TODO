from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from .forms import CreationUserForm

# from django.shortcuts import redirect
# from django.contrib import auth


class SignUpView(generic.CreateView):
    form_class = CreationUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    redirect_field_name = "home"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = user.email
        user.save()
        messages.success(self.request, "Вы успешно зарегистрированы")
        return super().form_valid(form)

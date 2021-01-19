from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django_email_verification import sendConfirm

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
        sendConfirm(user)
        messages.success(
            self.request,
            f"Для завершения регистрации, перейдите по ссылке, указанной в письме, отправленное на {user.email}",
        )
        return super().form_valid(form)


class ConfirmationOutputView(TemplateView):
    """
    Страница подтверждения выхода
    """

    template_name = "pages/confirmation-output.html"

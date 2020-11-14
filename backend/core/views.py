from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    """Home page view"""

    template_name = "index.html"
    login_url = "/auth/login/"
    redirect_field_name = "home"

from django.urls import path

from .views import ConfirmationOutputView, SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "confirmation-output/",
        ConfirmationOutputView.as_view(),
        name="confirmation-output",
    ),
]

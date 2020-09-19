from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TodoConfig(AppConfig):
    """Default app config"""

    name = "apps.api.TODO"
    verbose_name = _("Todo")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import

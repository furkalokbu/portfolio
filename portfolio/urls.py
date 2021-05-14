from django import contrib
from django import urls
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from projects.views import home
from core.views import IndexTemplateView
from users.forms import CustomUserForm
from django_registration.backends.one_step.views import RegistrationView


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "accounts/register/",
        RegistrationView.as_view(
            form_class=CustomUserForm,
            success_url="/",
        ),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.one_step.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    # path("api/", include("users.api.urls")),
    path("api/", include("projects.api.urls", namespace="api")),
    re_path(r"^.*$", home, name="entry-point"),
    # re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

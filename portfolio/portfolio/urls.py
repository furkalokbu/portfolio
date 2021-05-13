from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from core.views import IndexTemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.api.urls')),
    # path('api/', include('projects.api.urls', namespace='api')),
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

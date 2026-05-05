from django.urls import include, path

urlpatterns = [
    path("", include("projects.urls")),
    path("", include("tecnologies.urls")),
]

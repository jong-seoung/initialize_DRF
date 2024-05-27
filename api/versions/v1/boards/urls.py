from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.versions.v1.boards.views import boardsViewsets

router = DefaultRouter()
router.register(r"boards", boardsViewsets)

urlpatterns = [
    path("", include(router.urls)),
]

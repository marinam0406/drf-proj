from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
    SubscriptionAPIView,
)

app_name = MaterialsConfig.name
router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lessons_list"),
    path(
        "lessons/retrieve/<int:pk>/",
        LessonRetrieveAPIView.as_view(),
        name="lessons_retrieve",
    ),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lessons_create"),
    path(
        "lessons/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lessons_update"
    ),
    path(
        "lessons/destroy/<int:pk>/",
        LessonDestroyAPIView.as_view(),
        name="lessons_destroy",
    ),
    path("subscription/create/", SubscriptionAPIView.as_view(), name="subscription_create", ),
] + router.urls

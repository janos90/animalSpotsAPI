from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest.views import Index, AnimalViewSet, UserViewSet, ProfileViewSet, SightingViewSet, getUser, attendEvent, \
    disAttendEvent

# from rest.views import DogList, DogDetails

router = DefaultRouter()
router.register('animals', AnimalViewSet, basename='dogs')
router.register('users', UserViewSet)
router.register('profiles', ProfileViewSet, basename='profiles')
router.register('sightings', SightingViewSet, basename='activities')

urlpatterns = [
    path('', Index),
    path('api/', include(router.urls)),
    path('api/getuser/', getUser.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
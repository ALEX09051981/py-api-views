from django.urls import path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    movie_list,
    movie_detail,
    GenreListCreateAPIView,
    GenreRetrieveUpdateDestroyAPIView,
    ActorListCreateAPIView,
    ActorRetrieveUpdateDestroyAPIView,
    CinemaHallViewSet,
    MovieViewSet,
)

app_name = "cinema"

urlpatterns = [
    path(
        "movies/",
        movie_list,
        name="movie-list"
    ),
    path(
        "movies/<int:pk>/",
        movie_detail,
        name="movie-detail"
    ),
    path(
        "genres/",
        GenreListCreateAPIView.as_view(),
        name="genre-list-create"
    ),
    path(
        "genres/<int:pk>/",
        GenreRetrieveUpdateDestroyAPIView.as_view(),
        name="genre-detail"
    ),
    path(
        "actors/",
        ActorListCreateAPIView.as_view(),
        name="actor-list-create"
    ),
    path(
        "actors/<int:pk>/",
        ActorRetrieveUpdateDestroyAPIView.as_view(),
        name="actor-detail"
    ),
]

router = DefaultRouter()
router.register(r"cinema-halls", CinemaHallViewSet, basename="cinema-hall")
router.register(r"movies", MovieViewSet, basename="movie")

urlpatterns += router.urls

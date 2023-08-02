from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserList.as_view(), name="user_list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user_detail"),
    path("cars/", views.CarList.as_view(), name="car_list"),
    path("cars/<int:pk>/", views.CarDetail.as_view(), name="car_detail"),
    path("trips/", views.TripList.as_view(), name="trip_list"),
    path("trips/<int:pk>/", views.TripDetail.as_view(), name="trip_detail"),
    path("user_routes/", views.UserRouteList.as_view(), name="user_route_list"),
    path(
        "user_routes/<int:pk>/",
        views.UserRouteDetail.as_view(),
        name="user_route_detail",
    ),
]

from django.urls import path

from perfomances.views import PosterList, PosterDetail, Place, Map, Ticket


urlpatterns = [
    path('', PosterList.as_view(), name="poster_list"),
    path('<int:pk>/', PosterDetail.as_view(), name="poster_detail"),
    path('<int:pk>/place/', Place.as_view()),
    path('<int:pk>/place/get-map/', Map.as_view()),
    path('<int:pk>/place/get-tickets/', Ticket.as_view())
]

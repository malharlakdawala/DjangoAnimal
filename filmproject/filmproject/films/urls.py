from django.urls import path
from . import views

urlpatterns = [
	path('films/homepage/',views.FilmListView.as_view(), name='homepage'),
	path('films/addFilm/',views.FilmAddView.as_view(),name='addFilm'),
	path('films/editFilm/<int:pk>/',views.FilmUpdateView.as_view(),name='updateFilm'),
	path('films/detailFilm/<int:pk>/',views.FilmDetailView.as_view(),name='detailFilm'),

]
#    path('new_post/', views.PostCreateView.as_view(), name='create_post'),

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='home'),
    path('movie/detail/<int:pk>', views.MovieDetailView.as_view(), name='movie_detail'),
    path('genre/movie/<int:pk>', views.GenreMovieView.as_view(), name='genre_movie'),
    path('comment', views.CommentListView.as_view(), name='comment_list'),
]

urlpatterns += [
    path('comment/<int:pk>/delete', views.CommentDelete.as_view(), name='comment_delete'),
    path('comment/<int:pk>/update', views.CommentUpdate.as_view(), name='comment_update'),
]
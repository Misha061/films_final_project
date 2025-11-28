from django.urls import path
from .views import FilmListView, FilmDetailView, FilmCreateView, FilmUpdateView, FilmCommentCreateView ,FilmDeleteView, FilmUpdateCommentView, FilmCommentDeleteView,FilmCreateScoreView, FilmUpdateScoreView, FilmDeleteScoreView ,  login_view, logout_view, register_view

urlpatterns = [

    path('', FilmListView.as_view(), name='film_catalog'),
    path('<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('create/', FilmCreateView.as_view(), name='film_create'),
    path('<int:pk>/update/', FilmUpdateView.as_view(), name='film_update'),
    path('<int:pk>/delete/', FilmDeleteView.as_view(), name='film_delete'),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path("logout/", logout_view, name='logout'),
    path("<int:pk>/add_comment", FilmCommentCreateView.as_view(), name="add_comment" ),
    path("<int:pk>/delete_comment", FilmCommentDeleteView.as_view(), name="delete_comment" ),
    path("<int:pk>/update_comment", FilmUpdateCommentView.as_view(), name="update_comment" ),
    path('<int:pk>/add_score/', FilmCreateScoreView.as_view(), name='add_score'),
    path('<int:pk>/score_update/', FilmUpdateScoreView.as_view(), name='update_score'),
    path('<int:pk>/score_delete/', FilmDeleteScoreView.as_view(), name='delete_score'),

]

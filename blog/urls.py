from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    add_comment,
    index,
    contact,
    directory,
    nueva_pregunta,
    foro,
    nosotros,

)


urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path('directory/' ,directory ,name='directory'),
    path('posts/', PostListView.as_view(), name='index'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
    path('nueva_pregunta', nueva_pregunta, name='nueva_pregunta'),
    path('foro/', foro, name='foro'),
    path('nosotros/', views.nosotros, name='nosotros'),

]

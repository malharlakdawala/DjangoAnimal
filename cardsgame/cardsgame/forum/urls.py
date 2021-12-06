from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='forum_page'),
    #path('add_comment', views.CommentsCreateView.as_view(), name='comment_section'),
    path('add_comment/<int:post_id>', views.CommentsCreateView.as_view(), name='add_comment'),
    path('new_post/new_post', views.PostCreateView.as_view(), name='create_post'),
]

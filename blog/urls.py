from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<slug:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('new_post/', views.CreatePostView.as_view(), name='new_post'),
    path('post/update_post/<slug:pk>/', views.UpdatePostView.as_view(), name='update_post'),
    path('post/delete_post/<slug:pk>/', views.DeletePostView.as_view(), name='delete_post'),
    path('drafts/', views.DraftListView.as_view(), name='drafts'),
    path('post/<slug:pk>/comment/', views.add_comments_to_post, name='add_comment_to_post'),
    path('comment/<slug:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<slug:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<slug:pk>/publish/', views.post_publish, name='post_publish'),
    path('logout/', views.user_logout, name='user_logout'),


]
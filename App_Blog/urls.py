from django.urls import path
from App_Blog import views

app_name = "App_Blog"

urlpatterns = [
    path("", views.BlogList.as_view(), name="blog_list"),
    path("write/", views.CreateBlog.as_view(), name="create_blog"),
    path("details/<slug:slug1>/", views.blog_details, name="blog_details"),
    path("liked_blog/<int:pk>/", views.liked_blog, name="liked_blog"),
    path("unliked_blog/<int:pk>/", views.unliked_blog, name="unliked_blog"),
    path("my_blogs/", views.MyBlogs.as_view(), name="my_blogs"),
    path("edit_blog/<int:pk>/", views.UpdateBlog.as_view(), name="edit_blog"),
]
from django.urls import path

from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    # path("<int:slug", views.post_list, name="post_list"),
    # path("search/",views.search_view, name = "post_search"),
    path("create/", views.create_view, name = "post_creation"),
    path("<int:pk>",views.post_detail,name = "post_detail"),    
    
]
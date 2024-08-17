from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view.as_view(), name="home"),
    path("search/", views.SearchResults.as_view(), name="search"),
    path("favorite/", views.favorite_list, name="favorite_list"),
    path("cart/", views.my_carts, name="cart_detail"),
    path(
        "categories/<int:category_id>/",
        views.category_articles,
        name="category_articles",
    ),
    path("articles/<int:article_id>/", views.article_detail, name="article_detail"),
    path("cart/<int:article_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/<int:pk>/delete/", views.remove_from_cart, name="remove_from_cart"),
    path("login", views.login_view, name="login"),
    path("registration/", views.register_view, name="registration"),
    path("logout/", views.user_logout, name="logout"),
    path("articles/create", views.create_article_view, name="create"),
    path("article/<int:pk>/update/", views.UpdateArticleView.as_view(), name="update"),
    path("article/<int:pk>/delete/", views.DeleteArticleView.as_view(), name="delete"),
]

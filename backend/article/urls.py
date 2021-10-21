from django.urls import path
from rest_framework import routers
from article.views import ArticleView, AuthorView ,ArticleViewset , AuthorViewset


app_name = "articles"

router = routers.DefaultRouter()
router.register(r"authorsvs", AuthorViewset)
router.register(r"articlevs", ArticleViewset)


# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>/', ArticleView.as_view()),
    path('authors/', AuthorView.as_view()),
    path('authors/<int:pk>/', AuthorView.as_view()),
]
print(router.urls)
urlpatterns = urlpatterns + router.urls
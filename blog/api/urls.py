from django.conf.urls import url, include
from django.urls import path

from rest_framework import routers
from blog.api import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'list', views.PostViewList.as_view()),
    path('get/<int:pk>', views.PostViewsDetail.as_view()),
    path('delete/<int:pk>', views.PostViewDestroy.as_view()),
]
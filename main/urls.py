from django.urls import path, include
from .views import VideoView, CommentsView

urlpatterns = [
    path('/video', VideoView.as_view({'post': 'create', 'get': 'list'}), name='video'),
    path('/comment', CommentsView.as_view({'post': 'create', 'get': 'list'}), name='comment')
]

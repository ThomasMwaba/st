from django.urls import path
from . import views
from .views import ReadingListView


urlpatterns = [
        path('reading/',ReadingListView.as_view(),name='reading'),
        path('success/',views.success,name='success'),
        path('',views.home,name='home'),
]
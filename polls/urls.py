from django.contrib import admin
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('<pk>/', views.DetailView.as_view(), name='detail'),
    path('<pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<question_id>/vote/', views.vote, name='vote')
]

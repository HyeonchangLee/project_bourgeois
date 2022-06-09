from . import views
from django.urls import path,include

app_name = 'analytics'
urlpatterns = [
    path('chart_data/', views.chart_data, name='chart_data'),
    path('inner/', views.inner, name='inner'),

]

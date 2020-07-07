from django.urls import path
from SDGTest import views

urlpatterns = [
    path('', views.API_Root.as_view(), name='API Root'),
    path('api/v1/on-covid-19', views.EstimateView.as_view(), name='Covid-19 Estimator'),
    path('api/v1/on-covid-19/json', views.EstimateViewJSON.as_view(), name='Covid-19 Estimator JSON'),
    path('api/v1/on-covid-19/xml', views.EstimateViewXML.as_view(), name='Covid-19 Estimator XML'),
    path('api/v1/on-covid-19/logs', views.APILogs.as_view(), name='API Logs'),
]




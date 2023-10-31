from django.urls import path
from . import views

urlpatterns = [
    path('ip.finder', views.index, name='index'),
    path('forex/slp-calc', views.forex_calc_stop_loss_price, name='fx_slpc')
]

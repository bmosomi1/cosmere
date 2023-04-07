from django.urls import path
from mpesa_api import views, home_land

urlpatterns = [
    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),

    path('c2b/142374/register', views.register_urls2, name="register_mpesa_validation"),
    path('c2b/142374/confirmation', views.confirmation2, name="confirmation"),
    path('c2b/142374/validation', views.validation2, name="validation"),

    # tobento
    path('c2b/tobento/196192/register', views.tobento_register_urls, name="register_mpesa_validation"),
    path('c2b/tobento/196192/confirmation', views.tobento_confirmation, name='tobento_confirmation'),
    path('c2b/tobento/196192/validation', views.tobento_validation, name='tobento_validation'),

    # mayanet
    path('c2b/mayanet/533382/register', views.mayanet_register_urls),
    path('c2b/mayanet/533382/validation', views.mayanet_validation),
    path('c2b/mayanet/533382/confirmation', views.mayanet_confirmation),

    # mayanet 2
    path('c2b/mayanet/4027033/register', views.mayanet2_register_urls),
    path('c2b/mayanet/4027033/validation', views.mayanet2_validation),
    path('c2b/mayanet/4027033/confirmation', views.mayanet2_confirmation),

    # t and t sky
    path('c2b/tntsky/4047479/register', views.tntsky_register_urls),
    path('c2b/tntsky/4047479/validation', views.tntsky_validation),
    path('c2b/tntsky/4047479/confirmation', views.tntsky_confirmation),

    # home land
    path('c2b/homeland/863893/register', home_land.register_urls),
    path('c2b/homeland/863893/validation', home_land.validation),
    path('c2b/homeland/863893/confirmation', home_land.confirmation),

    # gathu
    path('c2b/gathu/4070687/register', views.gathu_register_urls),
    path('c2b/gathu/4070687/validation', views.gathu_validation),
    path('c2b/gathu/4070687/confirmation', views.gathu_confirmation),

    # chrisbe
    path('c2b/chrisbe/4070685/register', views.chrisbe_register_urls),
    path('c2b/chrisbe/4070685/validation', views.chrisbe_validation),
    path('c2b/chrisbe/4070685/confirmation', views.chrisbe_confirmation),

    # experiential
    path('c2b/experiential/4048443/register', views.experiential_register_urls),
    path('c2b/experiential/4048443/validation', views.experiential_validation),
    path('c2b/experiential/4048443/confirmation', views.experiential_confirmation),

    #clemode
    path('c2b/clemode/4073307/register', views.clemode_register_urls),
    path('c2b/clemode/4073307/validation', views.clemode_validation),
    path('c2b/clemode/4073307/confirmation', views.clemode_confirmation),

    # dimples
    path('c2b/dimples/4075063/register', views.dimples_register_urls),
    path('c2b/dimples/4075063/validation', views.dimples_validation),
    path('c2b/dimples/4075063/confirmation', views.dimples_confirmation),

    path('archive', views.archive, name='archive')
]
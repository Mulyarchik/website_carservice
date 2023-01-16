from django.urls import path

from .views import *

app_name = 'vlads_app'

urlpatterns = [
    path('', home, name='home'),
    path('register/', user_signup, name='user_signup'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
    path('services/', service_selection, name='service_selection'),
    path('services/add/', add_service, name='add_service'),
    path('services/<int:service_id>/', day_selection, name='day_selection'),
    path('services/<int:service_id>/day/<int:day_id>/', time_selection, name='time_selection'),
    path('services/<int:service_id>/day/<int:day_id>/time/<int:time_id>/add_customer/', add_customer,
         name='add_customer'),
    path('profile/<int:user_id>/', profile, name='profile'),
    path('profile/<int:user_id>/service/<int:service_id>/check_customers', check_customers, name='check_customers'),

]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

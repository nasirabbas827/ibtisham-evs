from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.custom_register, name='register'), 
    path('login/', views.custom_login, name='login'),            
    path('logout/', views.custom_logout, name='logout'),         
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('view_candidates/<int:election_id>/', views.view_candidates, name='view_candidates'),
    path('cast_vote/<int:election_id>/<int:candidate_id>/', views.cast_vote, name='cast_vote'),
    path('view_results/', views.view_results, name='view_results'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

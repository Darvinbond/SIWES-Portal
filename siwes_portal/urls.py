from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Main),
    path('api/', include('api.urls')),
    path('signup/', Student_Signup),
    path('a_signup/', Admin_Signup),

    path('signin/', Student_Signin),
    path('a_signin/', Admin_Signin),

    path('st_home/', Student_home),
    path('ad_home/', Admin_home),

    path('st_change/', Student_change),
    path('ad_change/', Admin_change),

    path('st_report/', Student_report),
    path('ad_register/', Admin_register_student),
    path('ad_students/', Admin_student),

    path('st_work/', Student_work),
    path('st_404/', Student_404),
    path('ad_404/', Admin_404),
    path('ad_msg/', Admin_msg),
    path('st_msg/', Student_msg),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

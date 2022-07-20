from django.urls import path
from .views import *

urlpatterns = [
    path('l_student', s_signin),
    path('l_admin', a_signin),
    path('su_student', s_signup),
    path('su_admin', a_signup),
    path('c_student', s_update),
    path('del_mssg', delete_m),
    path('c_admin', a_update),
    path('s_report', s_report),
    path('s_w_details', s_work),
    path('s_w_details', s_work),
    path('find_st', find_st),
    path('reg_st', register_st),
    path('mssg_st', message_st),
    path('s_logout', s_logout),
    path('a_logout', a_logout),
]

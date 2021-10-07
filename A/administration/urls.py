from django.urls import path
from . import views
from django.urls import re_path
from . import consumers

app_name = 'administration'

urlpatterns = [
    path('',views.Index.as_view(),name="index"),    
    # ====================================
    path('user-management/',views.UserManagement.as_view(),name="user-management"),    
    path('edit-user/<str:user_id>',views.EditUser.as_view(),name="edit-user"),    
    path('block-user/<str:user_id>',views.BlockUser.as_view(),name="block-user"),    
    path('user-actions/<str:user_id>',views.UserActions.as_view(),name="user-actions"),
    path('user-appointments/<str:user_id>',views.UserAppointments.as_view(),name="user-appointments"),
    path('doctor-appointments/<str:user_id>',views.DoctorAppointments.as_view(),name="doctor-appointments"),
    path('add-user-appointment/<str:user_id>',views.AddUserAppointment.as_view(),name="add-user-appointment"),
    path('edit-user-appointment/<str:appointment_id>',views.EditUserAppointment.as_view(),name="edit-user-appointment"),
    path('edit-doctor-appointment/<str:appointment_id>',views.EditDoctorAppointment.as_view(),name="edit-doctor-appointment"),
    # ====================================
    path('role-management/',views.RoleManagement.as_view(),name="role-management"),    
    path('add-role/',views.AddRole.as_view(),name="add-role"),    
    path('edit-role/<str:role_id>',views.EditRole.as_view(),name="edit-role"),    
    path('remove-role/<str:role_id>',views.RemoveRole.as_view(),name="remove-role"),    
    # ====================================
    path('category-management/',views.CategoryManagement.as_view(),name="category-management"),    
    path('add-category/',views.AddCategory.as_view(),name="add-category"),    
    path('edit-category/<str:category_id>',views.EditCategory.as_view(),name="edit-category"),    
    path('remove-category/<str:category_id>',views.RemoveCategory.as_view(),name="remove-category"),    
    path('add-sub-category/<str:category_id>',views.AddSubCategory.as_view(),name="add-sub-category"),    
    path('edit-sub-category/<str:sub_category_id>',views.EditSubCategory.as_view(),name="edit-sub-category"),    
    path('remove-sub-category/<str:sub_category_id>',views.RemoveSubCategory.as_view(),name="remove-sub-category"),    
    # ====================================
    path('picture-management/',views.PictureManagement.as_view(),name="picture-management"),    
    path('add-picture/',views.AddPicture.as_view(),name="add-picture"),    
    path('edit-picture/<str:picture_id>',views.EditPicture.as_view(),name="edit-picture"),    
    path('remove-picture/<str:picture_id>',views.RemovePicture.as_view(),name="remove-picture"),    
    # ====================================
    path('edit-site-settings/',views.EditSiteSettings.as_view(),name="edit-site-settings"),    
    # ====================================
    path('sms-logs/',views.SmsLogs.as_view(),name="sms-logs"),    
    # ====================================
    path('blocked-ips/',views.IpManagement.as_view(),name="ip-management"),    
    path('add-blocked-ip/',views.AddBlockedIp.as_view(),name="add-blocked-ip"),    
    path('remove-blocked-ip/<str:id>',views.RemoveBlockedIp.as_view(),name="remove-blocked-ip"),    
    # ====================================
]

# websocket_urlpatterns = [
#         path('ws/logs/sms-logs/', consumers.DataConsumer.as_asgi()),
# ]
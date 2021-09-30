from django.urls import path
from . import views

app_name = 'administration'

urlpatterns = [
    path('',views.Index.as_view(),name="index"),    
    path('user-management/',views.UserManagement.as_view(),name="user-management"),    
    path('role-management/',views.RoleManagement.as_view(),name="role-management"),    
    path('add-role/',views.AddRole.as_view(),name="add-role"),    
    path('category-management/',views.CategoryManagement.as_view(),name="category-management"),    
    path('add-category/',views.AddCategory.as_view(),name="add-category"),    
    path('picture-management/',views.PictureManagement.as_view(),name="picture-management"),    
    path('add-picture/',views.AddPicture.as_view(),name="add-picture"),    
    path('edit-site-settings/',views.EditSiteSettings.as_view(),name="edit-site-settings"),    
]
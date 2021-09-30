from django.shortcuts import render
from django.views import View
from .pages.index import Index
from .pages.UserManagement.userManagement import UserManagement
from .pages.UserManagement.blockUser import BlockUser
from .pages.RoleManagement.roleManagement import RoleManagement
from .pages.RoleManagement.add_role import AddRole
from .pages.CategoryManagement.categoryManagement import CategoryManagement
from .pages.CategoryManagement.add_category import AddCategory
from .pages.PictureManagement.pictureManagement import PictureManagement
from .pages.PictureManagement.add_picture import AddPicture
from .pages.SiteSettings.edit_site_settings import EditSiteSettings


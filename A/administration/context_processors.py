


def administration_context_processor(request):
    user = request.user
    can_see_users = False
    # --------------
    can_see_roles = False
    can_add_role = False
    # --------------
    can_see_categories = False
    can_add_category = False
    # --------------
    can_see_pictures = False
    can_add_picture = False
    # --------------
    can_edit_site_settings = False
    # --------------

    if user.is_authenticated:
        see_users_permission_code = 10
        can_see_users = user.has_permission(see_users_permission_code)
        # --------------
        see_roles_permission_code = 20
        add_role_permission_code = 21
        can_see_roles = user.has_permission(see_roles_permission_code)
        can_add_role = user.has_permission(add_role_permission_code)
        # --------------
        see_categories_permission_code = 40
        add_category_permission_code = 41
        can_see_categories = user.has_permission(see_categories_permission_code)
        can_add_category = user.has_permission(add_category_permission_code)
        # --------------
        see_pictures_permission_code = 30
        add_picture_permission_code = 31
        can_see_pictures = user.has_permission(see_pictures_permission_code)
        can_add_picture = user.has_permission(add_picture_permission_code)
        # --------------
        edit_settings_permission_code = 2
        can_edit_site_settings = user.has_permission(edit_settings_permission_code)
        # --------------

    return {
        "can_see_users":can_see_users,
        "can_see_roles":can_see_roles,
        "can_add_role":can_add_role,
        "can_see_categories":can_see_categories,
        "can_add_category":can_add_category,
        "can_see_pictures":can_see_pictures,
        "can_add_picture":can_add_picture,
        "can_edit_site_settings":can_edit_site_settings
    }
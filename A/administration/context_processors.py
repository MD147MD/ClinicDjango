


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
        see_admin_panel_permission_code = 1
        can_see_admin_panel = user.has_permission(see_admin_panel_permission_code)
        # -------------
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
        see_logs_permission_code = 70
        see_sms_logs_permission_code = 71   
        can_see_sms_logs = user.has_permission(see_sms_logs_permission_code)
        can_see_logs = user.has_permission(see_logs_permission_code)
        # --------------
        see_common_permission_code = 100
        see_blocked_ips_permission_code = 80
        add_blocked_ip_permission_code = 81
        can_see_common = user.has_permission(see_common_permission_code)
        can_see_blocked_ips = user.has_permission(see_blocked_ips_permission_code)
        can_add_blocked_ip = user.has_permission(add_blocked_ip_permission_code)
        # --------------
        

    return {
        "can_see_admin_panel":request.user.is_authenticated and can_see_admin_panel,
        "can_see_users":request.user.is_authenticated and can_see_users,
        "can_see_roles":request.user.is_authenticated and can_see_roles,
        "can_add_role":request.user.is_authenticated and can_add_role,
        "can_see_categories":request.user.is_authenticated and can_see_categories,
        "can_add_category":request.user.is_authenticated and can_add_category,
        "can_see_pictures":request.user.is_authenticated and can_see_pictures,
        "can_add_picture":request.user.is_authenticated and can_add_picture,
        "can_edit_site_settings":request.user.is_authenticated and can_edit_site_settings,
        "can_see_sms_logs":request.user.is_authenticated and can_see_sms_logs,
        "can_see_logs":request.user.is_authenticated and can_see_logs,
        "can_see_blocked_ips":request.user.is_authenticated and can_see_blocked_ips,
        "can_add_blocked_ip":request.user.is_authenticated and can_add_blocked_ip,
        "can_see_common":request.user.is_authenticated and can_see_common,
    }
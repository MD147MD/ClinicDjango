from django.shortcuts import redirect


edit_settings_permission_code = 2


secure_urls = [
    {'url':'edit-site-settings','permission_code':2},
    # ===========================================
    {'url':'user-management','permission_code':10},
    {'url':'edit-user','permission_code':12},
    {'url':'block-user','permission_code':13},
    {'url':'user-actions','permission_code':14},
    {'url':'user-appointments','permission_code':15},
    # ===========================================
    {'url':'role-management','permission_code':20},
    {'url':'add-role','permission_code':21},
    {'url':'edit-role','permission_code':22},
    {'url':'remove-role','permission_code':23},
    # ===========================================
    {'url':'picture-management','permission_code':30},
    {'url':'add-picture','permission_code':31},
    {'url':'edit-picture','permission_code':32},
    {'url':'remove-picture','permission_code':33},
    # ===========================================
    {'url':'category-management','permission_code':40},
    {'url':'add-category','permission_code':41},
    {'url':'edit-category','permission_code':42},
    {'url':'remove-category','permission_code':43},
    {'url':'add-sub-category','permission_code':41},
    {'url':'edit-sub-category','permission_code':42},
    {'url':'remove-sub-category','permission_code':43},
    # ===========================================
]



def administration_middleware(get_response):

    def middleware(request):
        response = get_response(request)
        user = request.user
        see_admin_panel_permission_code = 1
        path = request.path.split("/")
        if 'administration' in path[1]:
            if user.is_authenticated and user.has_permission(see_admin_panel_permission_code):
                if path[2]:
                    for secure_url in secure_urls:
                            if secure_url['url'] in path[2]:
                                if request.user.has_permission(secure_url['permission_code']):
                                    return response
                    return redirect("/404")
                return response
            return redirect("/404")
        return response

    return middleware

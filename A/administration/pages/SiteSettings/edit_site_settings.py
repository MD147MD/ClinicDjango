from django.shortcuts import render,redirect
from django.views import View
from administration.forms import SiteSettingsForm
from siteSettings.models import SiteSettings
from django.contrib import messages


class EditSiteSettings(View):

    def get(self,request,*args,**kwargs):
        edit_site_settings_permission_code = 1
        if not request.user.has_permission(edit_site_settings_permission_code):
            return redirect("/404")
        settings = SiteSettings.objects.first()
        data = {}
        if settings:
            data["about_us"] = settings.about_us_text
            data["contact_us"] = settings.contact_us_text
        form = SiteSettingsForm(initial=data)
        return render(request,"site-settings/site-settings.html",
        {
            "section":"تنظیمات سایت",
            "page":"ویرایش تنظیمات",
            "icon":"fa fa-cogs",
            "form":form
        })
    

    def post(self,request,*args,**kwargs):
        edit_site_settings_permission_code = 1
        if not request.user.has_permission(edit_site_settings_permission_code):
            return redirect("/404")
        form = SiteSettingsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            settings = SiteSettings.objects.first()
            if not settings:
                settings = SiteSettings()
            settings.about_us_text = cd["about_us"]
            settings.contact_us_text = cd["contact_us"]
            settings.save()
            messages.success(request,"تنظیمات سایت با موفقیت ویرایش شد","info")
        return render(request,"site-settings/site-settings.html",
        {
            "section":"تنظیمات سایت",
            "page":"ویرایش تنظیمات",
            "icon":"fa fa-cogs",
            "form":form
        })
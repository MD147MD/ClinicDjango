from django.shortcuts import render,redirect
from django.views import View
from accounts.models import UserLoginAttempt,User
from django.core.paginator import Paginator
from uuid import UUID


class UserActions(View):

    def get(self,request,user_id,*args,**kwargs):
        user = None
        try:
            UUID(user_id)
            user = User.objects.get(pk=user_id)
        except:
            return redirect("/404")

        page = request.GET.get("page") if request.GET.get("page") else 1

        try:
            page = int(page)
        except:
            page = 1

        attempts = UserLoginAttempt.objects.filter(user=user).order_by("-created_at")
        attempt_pages = Paginator(attempts, 10)
        page_count = attempt_pages.num_pages
        page = page if page <= page_count else 1
        paginated_attempts = attempt_pages.page(page)
        max_page = page + 3 if (page + 3) <= page_count else page_count
        min_page = page - 3 if (page - 3) >= 1 else 1
        return render(request,"user-actions/user-actions.html",{
            "section":"مدیریت کاربران",
            "page":"دیدن فعالیت ها",
            "icon":"fa fa-eye",
            "attempts":paginated_attempts.object_list,
            "page_count":page_count,
            "has_next":paginated_attempts.has_next(),
            "has_previous":paginated_attempts.has_previous(),
            "min_page":min_page,
            "max_page":max_page,
            "current_page":page,
            "page_range":range(min_page,max_page + 1),
        })
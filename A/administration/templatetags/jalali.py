from django import template
from persiantools.jdatetime import JalaliDateTime
from django.contrib.humanize.templatetags.humanize import intcomma


register = template.Library()

week = {
    1:'شنبه',
    2:'یکشنبه',
    3:'دو شنبه',
    4:'سه شنبه',
    5:'چهار شنبه',
    6:'پنج شنبه',
    7:'جمعه'
}

month = {
    1:'فروردین',
    2:'اردیبهشت',
    3:'خرداد',
    4:'تیر',
    5:'مرداد',
    6:'شهریور',
    7:'مهر',
    8:'آبان',
    9:'آذر',
    10:'دی',
    11:'بهمن',
    12:'اسفند',
}


@register.filter(name="tojalali")
def tojalali(value):
    date = JalaliDateTime(value)
    minute = date.minute if len(str(date.minute)) == 2 else f"۰{date.minute}"
    hour = date.hour if len(str(date.hour)) == 2 else f"۰{date.hour}"
    day = date.day if len(str(date.day)) == 2 else f"۰{date.day}"
    value = f"{week[date.weekday()]} {day} {month[date.month]} {date.year} ساعت {minute} : {hour}"
    return value



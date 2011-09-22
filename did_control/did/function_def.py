from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from prefix_country.models import Country
from did.models import *
from user_profile.models import UserProfile
from dateutil.relativedelta import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
import calendar
import string
import urllib
import time



def field_list(name, user=None):
    """Return List of phonebook, campaign, country"""
    if name == "phonebook" and user is None:
        list = Phonebook.objects.all()
    
    #else:
    #    list = []
    return ((l.id, l.name) for l in list)


def day_range():
    """List of days"""
    DAYS = range(1, 32)
    days = map(lambda x: (x, x), DAYS)
    return days


def validate_days(year, month, day):
    """Validate no of days in a month"""
    total_days = calendar.monthrange(year, month)
    if day > total_days[1]:
        return total_days[1]
    else:
        return day


def month_year_range():
    """List of months"""
    tday = datetime.today()
    year_actual = tday.year
    YEARS = range(year_actual - 1, year_actual + 1)
    YEARS.reverse()
    m_list = []
    for n in YEARS:
        if year_actual == n:
            month_no = tday.month + 1
        else:
            month_no = 13
        months_list = range(1, month_no)
        months_list.reverse()
        for m in months_list:
            name = datetime(n, m, 1).strftime("%B")
            str_year = datetime(n, m, 1).strftime("%Y")
            str_month = datetime(n, m, 1).strftime("%m")
            sample_str = str_year + "-" + str_month
            sample_name_str = name + "-" + str_year
            m_list.append((sample_str, sample_name_str))
    return m_list


def variable_value(request, field_name):
    """Variables are checked with request &
    return field value"""
    if request.method == 'GET':
        if field_name in request.GET:
            field_name = request.GET[field_name]
        else:
            field_name = ''

    if request.method == 'POST':
        if field_name in request.POST:
            field_name = request.POST[field_name]
        else:
            field_name = ''

    return field_name


def type_field_chk(base_field, base_field_type, field_name):
    """Type fileds (e.g. equal to, begins with, ends with, contains)
    are checked."""
    kwargs = {}
    if base_field != '':
        if base_field_type == '1':
            kwargs[field_name + '__contains'] = base_field
        if base_field_type == '2':
            kwargs[field_name + '__exact'] = base_field
        if base_field_type == '3':
            kwargs[field_name + '__startswith'] = base_field
        if base_field_type == '4':
            kwargs[field_name + '__endswith'] = base_field
    return kwargs


def striplist(l):
    """Take a list of string objects and return the same list
    stripped of extra whitespace.
    """
    return([x.strip() for x in l])


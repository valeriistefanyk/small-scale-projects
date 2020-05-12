from django.template import Library, Node, TemplateSyntaxError
from datetime import date
from datetime import datetime
register = Library()

#custom template filter - place this in your custom template tags file
@register.filter
def only_hours(value):
    """
    Filter - removes the minutes, seconds, and milliseconds from a datetime

    Example usage in template:

    {{ my_datetime|only_hours|timesince }}

    This would show the hours in my_datetime without showing the minutes or seconds.
    """
    #replace returns a new object instead of modifying in place
    return value.replace(hour=0, minute=0, second=0, microsecond=0)


@register.filter(expects_localtime=True)
def days_since(value, arg=None):
    try:
        tzinfo = getattr(value, 'tzinfo', None)
        value = date(value.year, value.month, value.day)
    except AttributeError:
        # Passed value wasn't a date object
        return value
    except ValueError:
        # Date arguments out of range
        return value
    today = datetime.now(tzinfo).date()
    delta = value - today
    if abs(delta.days) == 1:
        day_str = ("day")
    else:
        day_str = ("days")

    if delta.days < 1:
        fa_str = ("ago")
    else:
        fa_str = ("from now")

    return "%s %s %s" % (abs(delta.days), day_str, fa_str)
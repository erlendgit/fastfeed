import functools
from datetime import datetime

from starlette.templating import Jinja2Templates

__all__ = ('render',)

templates = Jinja2Templates(directory="templates")


def register_filter(func):
    templates.env.filters[func.__name__] = func

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper


def render(*args, **kwargs):
    return templates.TemplateResponse(*args, **kwargs)


"""
Filters follow:
"""


@register_filter
def format_datetime(value: datetime):
    return value.strftime('%d %B %H:%M')


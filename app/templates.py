from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


def render(*args, **kwargs):
    return templates.TemplateResponse(*args, **kwargs)

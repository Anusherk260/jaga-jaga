from django.template import Library
from core.models import Category

register = Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def is_category_current(request, category_id):
    return str(category_id) in request.path

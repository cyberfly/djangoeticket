from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    query = context["request"].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    return query.urlencode()

@register.filter(name='format_ticket_status')
def format_ticket_status(status):
    if status == 'open':
        return mark_safe('<span class="badge bg-warning">'+status+'</span>')
    
    if status == 'in_progress':
        return mark_safe('<span class="badge bg-info">'+status+'</span>')
    
    if status == 'closed':
        return mark_safe('<span class="badge bg-success">'+status+'</span>')

    return status
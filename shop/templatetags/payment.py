from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def payment_mean(value):
    payment_means = {
        'cash': 'Liquide',
        'card': 'Carte de crédit',
        'check': 'Chèque',
    }
    return mark_safe(payment_means[value])


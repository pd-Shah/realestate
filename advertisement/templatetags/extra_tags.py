from django.template import Library

register = Library()

@register.filter(name='persianize_digits')
def persian_int(string):
    persianize = dict(zip("0123456789",'۰۱۲۳۴۵۶۷۸۹'))
    return " "+''.join(persianize[digit] if digit in persianize else digit for digit in str(string)) + " تومان"

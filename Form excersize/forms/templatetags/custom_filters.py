from django import template

register = template.Library()

#*CUSTOM FUNCTION
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts all values of "arg" fom the string!
    """
    return value.replace(arg, '')

#*Register function created above. ..('give it a neme', actual name of the function) or use decorator above the function
#//register.filter('cut',cut)
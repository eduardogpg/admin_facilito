from django import template

def set_title_model(value):
	return value.__class__.__name__

def list_fields(model):
	if model == "":
		return []
	return [field.name for field in model._meta.get_fields() if not field.is_relation and field.name != 'id' ]

def value_attr(model, value):
	return getattr(model, value)

register = template.Library()
register.filter('list_fields', list_fields)
register.filter('value_attr', value_attr)

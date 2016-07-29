from django import template

def set_title_model(value):
	return value.__class__.__name__

def list_fields(model):
	return [field.name for field in model._meta.get_fields() if not field.is_relation and field.name != 'id' ]

def value_attr(model, value):
	return getattr(model, value)

def attrs(value):
	return { field.name : getattr(value, field.name) for field in value._meta.get_fields() if not field.is_relation  }


register = template.Library()
register.filter('list_fields', list_fields)
register.filter('value_attr', value_attr)

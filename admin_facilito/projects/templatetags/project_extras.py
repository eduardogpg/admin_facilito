#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template

def date_format(value):
	meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
	mes = meses[value.month]
	return "El día {} de {} del {}".format(value.day, mes, value.year )

register = template.Library()
register.filter('date_format', date_format)
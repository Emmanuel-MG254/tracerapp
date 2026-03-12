from django.contrib import admin
from tracer.models import Contact
from tracer.models import Index
from tracer.models import Price
from tracer.models import Sea
from tracer.models import Road
from tracer.models import Air


# Register your models here.
admin.site.register(Contact)
admin.site.register(Index)
admin.site.register(Price)
admin.site.register(Sea)
admin.site.register(Road)
admin.site.register(Air)

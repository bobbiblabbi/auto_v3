from django.contrib import admin

from .models import FIO, Template
from .models import Files, Page1

admin.site.register(FIO)
admin.site.register(Files)
admin.site.register(Template)
admin.site.register(Page1)

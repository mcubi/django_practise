from django.contrib import admin

from .models import Person, Belongings
from .models import User

admin.site.register(Person)
admin.site.register(Belongings)
admin.site.register(User)

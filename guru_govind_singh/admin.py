from django.contrib import admin

from guru_govind_singh.admins.society_admin import SocietyAdmin
from guru_govind_singh.admins.swayamsevak_admin import SwayamsevakAdmin
from guru_govind_singh.models.society import Society
from guru_govind_singh.models.swayamsevak import Swayamsevak

admin.site.register(Swayamsevak, SwayamsevakAdmin)
admin.site.register(Society, SocietyAdmin)

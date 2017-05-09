from django.contrib import admin

# Register your models here.
from user_mgr.models import FriendList, UserAccount, Address

admin.site.register(FriendList)
admin.site.register(UserAccount)
admin.site.register(Address)
from django.contrib import admin

from .models import ConversationModel, ConversationMessageModel

admin.site.register(ConversationModel)
admin.site.register(ConversationMessageModel)
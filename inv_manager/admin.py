from django.contrib import admin
from inv_manager.models import (InvItem, ItemBrand, ItemModel, ItemDisk, ItemIP, ItemLocalization,
                                ItemMemory, ItemOS, ItemProcessor, ItemSector, ItemType)


@admin.register(InvItem, ItemBrand, ItemModel, ItemDisk, ItemIP, ItemLocalization, ItemMemory, ItemOS, ItemProcessor, ItemSector, ItemType)
class InvItemAdmin(admin.ModelAdmin):
    ...

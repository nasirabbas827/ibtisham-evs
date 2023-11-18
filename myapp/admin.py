from django.contrib import admin
from .models import Election, Candidate, BlockchainRecord

class BlockchainRecordAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'election', 'candidate', 'block_data', 'block_hash', 'prev_hash', 'created_at')

admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(BlockchainRecord, BlockchainRecordAdmin)

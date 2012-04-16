from feelgood.apps.tools.models import TripleColumnEntry, TripleColumn, CognitiveDistortion, BDC
from django.contrib import admin


class TripleColumnAdmin(admin.ModelAdmin):

    def queryset(self, request):
        return TripleColumn.objects.filter(user=request.user)

admin.site.register(TripleColumn, TripleColumnAdmin)


class TripleColumnEntryAdmin(admin.ModelAdmin):

    def queryset(self, request):
        return TripleColumnEntry.objects.filter(triplecolumn__user=request.user)

admin.site.register(TripleColumnEntry, TripleColumnEntryAdmin)


class CognitiveDistortionAdmin(admin.ModelAdmin):
    pass

admin.site.register(CognitiveDistortion, CognitiveDistortionAdmin)


class BDCAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Meta information', {'fields': ['timestamp','user'], 'classes': ['collapse']}),
        ('Questions',        {'fields': BDC.QUESTION_FIELDS}),
    ]

    def queryset(self, request):
        return BDC.objects.filter(user=request.user)

admin.site.register(BDC,BDCAdmin)

from django.contrib import admin


class SingletonModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        """ Singleton pattern: prevent addition of new objects """
        return False

    def has_delete_permission(self, request, obj=None):
        """ Singleton pattern: prevent deletion of The One object."""
        return False

    def change_view(self, request, object_id, extra_context=None):
        if object_id == '1':
            self.model.objects.get_or_create(pk=1)
        return super(SingletonModelAdmin, self).change_view(
            request,
            object_id,
            extra_context=extra_context,
        )

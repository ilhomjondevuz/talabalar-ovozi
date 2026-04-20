from django.contrib import admin

from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'opinion', 'rating')
    search_fields = ('student_name', 'opinion', 'rating')

admin.site.register(Feedback, FeedbackAdmin)
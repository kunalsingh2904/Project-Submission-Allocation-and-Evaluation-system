from django.contrib import admin

from .models import Assignment, Comments, Submission

# admin.site.register(Assignment)
# admin.site.register(Comments)
# admin.site.register(Submission)


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'submit_by', 'file', 'marks', 'status')
    list_filter = ('assignment', 'submit_by', 'status')


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'types', 'teach_by', 'course', 'semester', 'year')
    list_filter = ('year', 'types', 'semester', 'teach_by', 'course')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'user', 'comment')


admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Comments, CommentsAdmin)

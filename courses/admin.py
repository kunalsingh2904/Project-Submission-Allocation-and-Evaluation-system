from django.contrib import admin

from .models import Takes, Teaches, Courses

# admin.site.register(Teaches)
# admin.site.register(Courses)
# admin.site.register(Takes)


class TakesAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'student_id', 'section', 'semester', 'year')
    list_filter = ('course_id', 'year', 'semester')


class TeachesAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'teacher_id', 'section', 'semester', 'year')
    list_filter = ('course_id', 'year', 'semester')


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'title', 'credits', 'department')
    list_filter = ('credits', 'department')


admin.site.register(Courses, CoursesAdmin)
admin.site.register(Takes, TakesAdmin)
admin.site.register(Teaches, TeachesAdmin)

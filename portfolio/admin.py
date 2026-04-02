from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Resume, Profile, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'created_at', 'image_preview')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('title', 'tech_stack')
    readonly_fields = ('image_preview',)
    inlines = [ProjectImageInline]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 5px;" />', obj.image.url)
        return "No Image"

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('uploaded_at', 'is_active', 'file')
    list_filter = ('is_active',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')


from django.contrib import admin
from octofit_tracker.models import Team, CustomUser, Activity, Workout, Leaderboard
from django.contrib.auth.admin import UserAdmin

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'team', 'is_active', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('team',)}),
    )

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'duration', 'calories')

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'points')

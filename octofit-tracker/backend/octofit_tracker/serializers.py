from rest_framework import serializers
from octofit_tracker.models import Team, Activity, Leaderboard, Workout, CustomUser

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['_id', 'username', 'email', 'team', 'is_active']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user', 'type', 'duration', 'calories']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description']

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['_id', 'user', 'points']

from django.test import TestCase
from octofit_tracker.models import Team, CustomUser, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc')
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=10, calories=100)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=123)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_user_team(self):
        self.assertEqual(self.user.team, self.team)

    def test_activity_str(self):
        self.assertIn('testuser', str(self.activity))

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')

    def test_leaderboard_str(self):
        self.assertIn('testuser', str(self.leaderboard))

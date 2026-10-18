from django.test import TestCase
from django.urls import reverse
from .models import madlibs


class MadLibFlowTests(TestCase):
	def test_create_displays_generated_story(self):
		response = self.client.post(reverse('madlibs:create'), {
			'name': 'Test Story',
			'place': 'Test Place',
			'adjective': 'bright',
			'color': 'green',
			'animal': 'otter',
			'feeling': 'happy',
			'verb': 'dance',
		})

		self.assertEqual(response.status_code, 302)
		story = madlibs.objects.get(name='Test Story')
		story_response = self.client.get(response.url)
		self.assertContains(story_response, story.story_text)

	def test_missing_story_returns_not_found(self):
		url = reverse('madlibs:story_detail', kwargs={'madlibs_id': 999999})

		self.assertEqual(self.client.get(url).status_code, 404)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from .models import Question
import datetime
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
def create_question(text, offset):
	time = timezone.now() + datetime.timedelta(days = offset)
	return Question.objects.create(question_text=text, pub_date = time)

class QuestionModelTest(TestCase):
	def test_question_was_not_published_today(self):
		time = timezone.now() - datetime.timedelta(days=1,seconds=1)
		old_question = Question(question_text="This is past", pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)
	def test_question_was_published_today(self):
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59,seconds=59)
		new_question = Question(question_text="This is new",pub_date=time)
		self.assertIs(new_question.was_published_recently(), True)


class IndexViewTest(TestCase):
	def test_no_question(self):
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available")
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def testPastQuestion(self):
 		create_question("Past Question", -30)
 		response = self.client.get(reverse('polls:index'))
 		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question>'])

	def testFutureQuestion(self):
 		create_question("Future Question", 30)
 		response = self.client.get(reverse('polls:index'))
 		self.assertQuerysetEqual(response.context['latest_question_list'], [])
 		self.assertEqual(response.status_code, 200)
 		self.assertContains(response, "No polls are available")

	def past_and_future_question(self):
 		create_question("Past Question", -30)
 		create_question("Future Question", 30)
 		response = self.client.get(reverse('polls:index'))
 		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past Question>'])

	def two_past_question(self):
 		create_question("Past Question 1", -30)
 		create_question("Past Question 2", -15)
 		response = self.client.get(reverse('polls:index'))
 		self.assertQuerysetEqual(['<Question: Past Question 2>', '<Question: Past Question 1>'])



class DetailsViewTest(TestCase):
	def future_test(self):
		future_question = create_question("This is Future", 30)
		url = reverse('polls:details', arg=future_test.id)
		response = self.client.get(url)
		#self.assertQuerysetEqual(response.context['latest_question_list'],[])
		self.assertEqual(reponse.status_code, 404)
		#self.assertContains(repsonse,"No polls available")

	def past_test(self):
		past_question = create_question("This is past", -30)
		url = reverse('polls:details', arg=past_question.id)
		response = self.client.get(url)
		self.assertContains(response, past_question.question_text)
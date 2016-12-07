import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    @classmethod
    def init_questions(cls):
        # Remove all choices and questions
        for question in Question.objects.all():
            for choice in question.choice_set.all():
                choice.delete()
            question.delete()
        question2 = Question.objects.create(question_text="Who is your favorite Star Wars character?",
                                            pub_date=timezone.now())
        for choice_text in ['BB-8', 'C3PO', 'Finn', 'Han Solo', 'Kylo Ren', 'Leia Organa', 'Luke Skywalker', 'R2D2', 'Rey']:
            question2.choice_set.create(choice_text=choice_text, votes=0)
        question1 = Question.objects.create(question_text="What is your favorite cuisine?",
                                            pub_date=timezone.now())
        for choice_text in ['American', 'Chinese', 'Indian', 'Italian', 'Japanese', 'Thai']:
            question1.choice_set.create(choice_text=choice_text, votes=0)
        return True

    def votes(self):
        sum = 0
        for choice in self.choice_set.all():
            sum += choice.votes
        return sum

    def choices_by_vote_count(self):
        return self.choice_set.order_by('-votes')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    def vote_for(self):
        self.votes += 1
        self.save()

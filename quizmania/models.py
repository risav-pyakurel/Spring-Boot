from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length = 255, unique = True)
    password = models. CharField(max_length = 120)

    def __str__(self):
        return self.username

class Questions(models.Model):

    question_text= models.TextField()
    Option_A = models.CharField(max_length = 255)
    Option_B = models.CharField(max_length = 255)
    Option_C = models.CharField(max_length = 255)
    Option_D = models.CharField(max_length = 255)
    Correct_Answer = models.CharField(max_length = 1)

    def __str__(self):
        return self.question_text
from django.db import models

class Question(models.Model):
    OPEN = 'ouverte'
    QCM = 'qcm'
    QUESTION_TYPES = [
        (OPEN, 'Ouverte'),
        (QCM, 'QCM'),
    ]

    intitule = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    reponses = models.JSONField(blank=True, null=True)

class Sondage(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    createur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)

class Reponse(models.Model):
    sondage = models.ForeignKey(Sondage, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reponse = models.JSONField()
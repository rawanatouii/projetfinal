import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '../sondage.settings')

# Configure Django
django.setup()


from django.contrib.auth.models import User
from data.models import Sondage, Question, Reponse

# Obtenez ou créez un utilisateur
user, created = User.objects.get_or_create(username='nom_utilisateur', defaults={'password': 'mot_de_passe'})

# Créez un sondage
sondage = Sondage.objects.create(nom="Sondage Préférences Alimentaires", createur=user)

# Créez une question ouverte
question1 = Question.objects.create(sondage=sondage, intitule="Quel est votre plat préféré ?", type="ouverte")

# Créez une question à choix multiple
question2 = Question.objects.create(sondage=sondage, intitule="Quels types de cuisine préférez-vous ?", type="qcm")

# Ajoutez des réponses
reponse1 = Reponse.objects.create(sondage=sondage, utilisateur=user, question=question1, reponse="Pizza")
reponse2 = Reponse.objects.create(sondage=sondage, utilisateur=user, question=question2, reponse=["Italienne", "Indienne"])

import random
import string

from django.db import models


CATEGORIE_CHOICES = [
    ("Concours académique", "Concours académique"),
    ("Compétition sportive", "Compétition sportive"),
    ("Atelier / Formation", "Atelier / Formation"),
    ("Conférence", "Conférence"),
]


def generer_ticket_id():
    return "BJ-" + "".join(random.choices(string.digits, k=6))


def generer_place():
    lettre = random.choice("ABCDEF")
    numero = random.randint(10, 99)
    return f"{lettre}-{numero}"


class Registration(models.Model):
    nom = models.CharField("Nom complet", max_length=150)
    email = models.EmailField("Email")
    telephone = models.CharField("Téléphone", max_length=30)
    categorie = models.CharField("Catégorie", max_length=50, choices=CATEGORIE_CHOICES)
    ville = models.CharField("Ville", max_length=100)
    reference_paiement = models.CharField(
        "Référence de paiement Mobile Money", max_length=100, blank=True
    )
    motivation = models.TextField("Motivation / message", blank=True)

    ticket_id = models.CharField(max_length=20, unique=True, editable=False)
    place = models.CharField(max_length=10, editable=False)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.ticket_id:
            self.ticket_id = generer_ticket_id()
        if not self.place:
            self.place = generer_place()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom} ({self.ticket_id})"

    class Meta:
        verbose_name = "Inscription"
        verbose_name_plural = "Inscriptions"
        ordering = ["-date_inscription"]

# Inscription à l'événement — Backend Django

Formulaire d'inscription (thème « billet d'entrée ») avec base de données et interface d'administration.

## Installation

```bash
python -m venv venv
source venv/bin/activate      # sur Windows : venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # pour accéder à /admin/
python manage.py runserver
```

Puis ouvrir : http://127.0.0.1:8000/

## Fonctionnement

- `/` — formulaire d'inscription (nom, email, téléphone, catégorie, ville, référence Mobile Money, motivation)
- À la validation, un numéro de billet (`BJ-xxxxxx`) et une place (ex : `D-13`) sont générés automatiquement
- `/billet/<ticket_id>/` — page de confirmation avec le billet
- `/admin/` — tableau de bord administrateur (liste, recherche, filtres par catégorie/ville)

## Structure

```
core/                   # projet Django (settings, urls)
inscriptions/           # application
  models.py             # modèle Registration
  forms.py              # formulaire
  views.py               # logique d'inscription + confirmation
  admin.py               # configuration de l'admin
  templates/inscriptions/
    register.html        # formulaire (thème billet)
    confirmation.html     # billet confirmé
```

## Personnalisation

- Catégories : modifier `CATEGORIE_CHOICES` dans `inscriptions/models.py`
- Design/couleurs : variables CSS en haut de chaque template
- En production : passer `DEBUG = False`, définir `ALLOWED_HOSTS`, et utiliser PostgreSQL (remplacer la section `DATABASES` dans `core/settings.py`)

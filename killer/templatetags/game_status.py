from django import template


register = template.Library()


@register.filter
def game_status(value):
    if value.is_registration_open():
        status = "Inscriptions ouvertes"
    elif value.is_creation_in_progress():
        status = "Attribution des missions"
    elif value.is_game_open():
        status = "Jeu en cours"
    elif value.is_game_ended():
        status = "Jeu fini"

    return status


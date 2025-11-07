from rest_framework.throttling import AnonRateThrottle

class MatriculaAnonRateThrottle(AnonRateThrottle):
    # Sempre observar se o limite de requisição esta menor que o  global no settings.py, para não ocorre erros!
    rate = '5/day' 
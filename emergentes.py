import openai

openai.api_key = "TU_API_KEY_AQUÍ"

try:
    # Solicitud básica para comprobar el acceso a la API
    response = openai.Model.list()
    print("API funcionando correctamente. Modelos disponibles:")
    print(response)
except openai.AuthenticationError:
    print("Error de autenticación. Verifica tu API key.")
except openai.RateLimitError:
    print("Límite de cuota excedido. Verifica tus límites en OpenAI.")

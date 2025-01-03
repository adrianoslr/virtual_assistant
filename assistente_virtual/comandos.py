import webbrowser
import wikipedia
import googlemaps
from .tts import text_to_speech

def abrir_youtube():
    webbrowser.open("https://www.youtube.com")
    text_to_speech("Abrindo o YouTube.")

def pesquisar_wikipedia(query):
    wikipedia.set_lang("pt")
    try:
        resultado = wikipedia.summary(query, sentences=2)
        text_to_speech("Aqui está o que encontrei:")
        print(resultado)
        text_to_speech(resultado)
    except wikipedia.exceptions.DisambiguationError:
        text_to_speech("Desculpe, encontrei várias opções. Seja mais específico.")
    except Exception:
        text_to_speech("Não consegui encontrar informações sobre isso.")

def localizar_farmacia():
    gmaps = googlemaps.Client(key='SUA_CHAVE_API')
    geocode_result = gmaps.places("farmácia", location=(LATITUDE, LONGITUDE), radius=2000)
    if geocode_result['results']:
        local = geocode_result['results'][0]
        text_to_speech(f"A farmácia mais próxima é {local['name']} em {local['vicinity']}.")
    else:
        text_to_speech("Não encontrei farmácias próximas.")

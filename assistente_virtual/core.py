from .tts import text_to_speech
from .stt import speech_to_text
from .comandos import abrir_youtube, pesquisar_wikipedia, localizar_farmacia

def executar_assistente():
    text_to_speech("Assistente virtual iniciada. Como posso ajudar?")
    while True:
        comando = speech_to_text()
        if "youtube" in comando:
            abrir_youtube()
        elif "pesquisar" in comando:
            text_to_speech("O que você quer pesquisar?")
            query = speech_to_text()
            pesquisar_wikipedia(query)
        elif "farmácia" in comando:
            localizar_farmacia()
        elif "sair" in comando:
            text_to_speech("Encerrando o sistema. Até logo!")
            break
        else:
            text_to_speech("Comando não reconhecido. Tente novamente.")

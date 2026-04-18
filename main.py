from gtts import gTTS

texto = "Olá! Este é um teste do meu projeto de voz com IA."

tts = gTTS(text=texto, lang='pt')
tts.save("resposta.mp3")

print("Áudio gerado com sucesso!")

import pyttsx3

# https://pyttsx3.readthedocs.io/en/latest/index.html

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print(voice.languages[0], voice.id, voice.name)
    engine.setProperty('voice', voice.id)
    engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()


"""
com.apple.speech.synthesis.voice.Alex
Alex
['en_US']

com.apple.speech.synthesis.voice.alice
Alice
['it_IT']

com.apple.speech.synthesis.voice.alva
Alva
['sv_SE']

com.apple.speech.synthesis.voice.amelie
Amelie
['fr_CA']

com.apple.speech.synthesis.voice.anna
Anna
['de_DE']

com.apple.speech.synthesis.voice.carmit
Carmit
['he_IL']

com.apple.speech.synthesis.voice.damayanti
Damayanti
['id_ID']

com.apple.speech.synthesis.voice.daniel
Daniel
['en_GB']

com.apple.speech.synthesis.voice.diego
Diego
['es_AR']

com.apple.speech.synthesis.voice.ellen
Ellen
['nl_BE']

com.apple.speech.synthesis.voice.fiona
Fiona
['en-scotland']

com.apple.speech.synthesis.voice.Fred
Fred
['en_US']

com.apple.speech.synthesis.voice.ioana
Ioana
['ro_RO']

com.apple.speech.synthesis.voice.joana
Joana
['pt_PT']

com.apple.speech.synthesis.voice.jorge
Jorge
['es_ES']

com.apple.speech.synthesis.voice.juan
Juan
['es_MX']

com.apple.speech.synthesis.voice.kanya
Kanya
['th_TH']

com.apple.speech.synthesis.voice.karen
Karen
['en_AU']

com.apple.speech.synthesis.voice.kyoko
Kyoko
['ja_JP']

com.apple.speech.synthesis.voice.laura
Laura
['sk_SK']

com.apple.speech.synthesis.voice.lekha
Lekha
['hi_IN']

com.apple.speech.synthesis.voice.luca
Luca
['it_IT']

com.apple.speech.synthesis.voice.luciana
Luciana
['pt_BR']

com.apple.speech.synthesis.voice.maged
Maged
['ar_SA']

com.apple.speech.synthesis.voice.mariska
Mariska
['hu_HU']

com.apple.speech.synthesis.voice.mei-jia
Mei-Jia
['zh_TW']

com.apple.speech.synthesis.voice.melina
Melina
['el_GR']

com.apple.speech.synthesis.voice.milena
Milena
['ru_RU']

com.apple.speech.synthesis.voice.moira
Moira
['en_IE']

com.apple.speech.synthesis.voice.monica
Monica
['es_ES']

com.apple.speech.synthesis.voice.nora
Nora
['nb_NO']

com.apple.speech.synthesis.voice.paulina
Paulina
['es_MX']

com.apple.speech.synthesis.voice.rishi
Rishi
['en_IN']

com.apple.speech.synthesis.voice.samantha
Samantha
['en_US']

com.apple.speech.synthesis.voice.sara
Sara
['da_DK']

com.apple.speech.synthesis.voice.satu
Satu
['fi_FI']

com.apple.speech.synthesis.voice.sin-ji
Sin-ji
['zh_HK']

com.apple.speech.synthesis.voice.tessa
Tessa
['en_ZA']

com.apple.speech.synthesis.voice.thomas
Thomas
['fr_FR']

com.apple.speech.synthesis.voice.ting-ting
Ting-Ting
['zh_CN']

com.apple.speech.synthesis.voice.veena
Veena
['en_IN']

com.apple.speech.synthesis.voice.Victoria
Victoria
['en_US']

com.apple.speech.synthesis.voice.xander
Xander
['nl_NL']

com.apple.speech.synthesis.voice.yelda
Yelda
['tr_TR']

com.apple.speech.synthesis.voice.yuna
Yuna
['ko_KR']

com.apple.speech.synthesis.voice.yuri
Yuri
['ru_RU']

com.apple.speech.synthesis.voice.zosia
Zosia
['pl_PL']

com.apple.speech.synthesis.voice.zuzana
Zuzana
['cs_CZ']
"""

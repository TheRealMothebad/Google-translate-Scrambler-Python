import random, googletrans, time
from googletrans import Translator

translator = Translator()

langs = googletrans.LANGUAGES

crazyness = 7

def randomTranslate(sentence):
    last_l = translator.detect(sentence).lang
    next_l = random.choice(list(langs.keys()))
    print("last " + langs.get(last_l) + " next " + langs.get(next_l))
    time.sleep(1)
    return translator.translate(sentence,  src=last_l, dest=next_l)

for x in range(1, crazyness):
    if x == 1:
        input_text = "random data nobody asked: something nobody payed attention at all, is that SUDO clan logo is perfect for the clan, when you look at it you can watch the 4 letters of the clan name, the S is around the U and D and all the letters are inside a circle, similar to an O, and it uses grey scale colors, it's a very nice clan logo and congratulations to who maded it"
    input_text = randomTranslate(input_text).text
    #print(result)
    print(input_text)
    if x == crazyness - 1:
        print(translator.translate(input_text,  src=translator.detect(input_text).lang, dest="en").text)


#print(googletrans.LANGUAGES)

#randomTranslate(input_text)
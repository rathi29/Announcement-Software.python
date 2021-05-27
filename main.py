import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
    
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('airline.mp3')


    start = 0
    finish = 3950
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_en.mp3", format="mp3")

    start = 5800
    finish = 120000
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_en.mp3", format="mp3")


  

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():


        textToSpeech(item['flight_no'] + " " + item['flight_name'], '2_en.mp3')


        audios = [f"{i}_en.mp3" for i in range(1,4)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['flight_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
from gtts import gTTS
import playsound

tts = gTTS("안녕하세요 지구환경시스템과학과 석사과정 하수빈입니다", lang='ko')
tts.save("HW8_202355385_하수빈.mp3")
playsound.playsound("HW8_202355385_하수빈.mp3", True)

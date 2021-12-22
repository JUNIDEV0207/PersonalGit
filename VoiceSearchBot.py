import speech_recognition as sr
import pyttsx3 

r = sr.Recognizer()
m = sr.Microphone()

print("A moment of silence, please...")
with m as source: r.adjust_for_ambient_noise(source)
print("Set minimum energy threshold to {}".format(r.energy_threshold))

print("Say something!")
with m as source: audio = r.listen(source)
print("Got it! Now to recognize it...")
try:
    # recognize speech using Google Speech Recognition
    words = r.recognize_google(audio)

    # we need some special handling here to correctly print unicode characters to standard output
    if str is bytes:  # this version of Python uses bytes for strings (Python 2)
        print(u"You said {}".format(words).encode("utf-8"))
    else:  # this version of Python uses unicode for strings (Python 3+)
        print("You said {}".format(words))
except sr.UnknownValueError:
    print("Oops! Didn't catch that")
except sr.RequestError as e:
    print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

#region selenium description test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\\Users\\Administrator\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
driver.get("https://www.google.com")

search = driver.find_element_by_name("q")

search.send_keys(words)
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='kno-rdesc']"))
    )
    results = driver.find_elements_by_xpath("//div[@class='kno-rdesc']")
    for value in results:
        value2 = value.text
        print(value.text)
finally:
    pass

# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init()
  
# say method on the engine that passing input text to be spoken
engine.say(value2)
  
# run and wait method, it processes the voice commands. 
engine.runAndWait()

import speech_recognition as sr
import sqlite3


def recog(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    return audio

if __name__ == '__main__':
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    staffName = r.recognize_google(audio, language='en-US')

    # using google speech recognition
    try:
        print("You said " + staffName)
    except sr.UnknownValueError:
        print("Error")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Connect to database (creates if not exists)
    conn = sqlite3.connect("sogeti.db")

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the CREATE TABLE statement

    cursor.execute('SELECT * FROM employees WHERE name LIKE ?', (staffName,))
    if len(list(cursor)) == 1:
        print('Yes we do have this staff in our company')
    else:
        print('Sorry we don`t know him or her.')

    conn.commit()
    conn.close()

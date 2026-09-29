import speech_recognition as sr
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import webbrowser
import os
import time
from datetime import datetime

# === TRAINING DATA ===

commands = [
    "open browser", "close browser", "play music", "pause music", "stop music",
    "what time is it", "shutdown computer", "restart computer",
    "increase volume", "decrease volume"
]
labels = [
    "open_browser", "close_browser", "play_music", "pause_music", "stop_music",
    "tell_time", "shutdown", "restart", "volume_up", "volume_down"
]

# Vectorize the commands
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(commands)

# Train the model
clf = MultinomialNB()
clf.fit(X, labels)

# === SYSTEM COMMANDS ===

def open_browser():
    print("🌐 Opening Microsoft Edge...")
    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

    if os.path.exists(edge_path):
        os.startfile(edge_path)
    else:
        print("❌ Microsoft Edge not found at the expected path.")

def close_browser():
    print("❌ Closing Microsoft Edge...")
    os.system("taskkill /f /im msedge.exe >nul 2>&1")


def play_music():
    print("🎵 Playing music...")
    music_folder = "C:/Users/Public/Music"  # Change to your music folder
    songs = os.listdir(music_folder)
    if songs:
        song_path = os.path.join(music_folder, songs[0])
        os.startfile(song_path)
    else:
        print("⚠️ No music files found.")

def pause_music():
    print("⏸️ Music paused. (Functionality not implemented)")

def stop_music():
    print("⏹️ Music stopped. (Functionality not implemented)")

def volume_up():
    print("🔊 Volume increased. (Functionality not implemented)")

def volume_down():
    print("🔉 Volume decreased. (Functionality not implemented)")

def tell_time():
    now = datetime.now().strftime("%I:%M %p")
    print(f"🕒 Current time is {now}")

def shutdown():
    print("⚠️ Shutting down computer... (not actually doing it)")
    # os.system("shutdown /s /t 1")  # Uncomment to activate

def restart():
    print("⚠️ Restarting computer... (not actually doing it)")
    # os.system("shutdown /r /t 1")  # Uncomment to activate

# === COMMAND EXECUTION ===

def execute_command(prediction):
    actions = {
        "open_browser": open_browser,
        "close_browser": close_browser,
        "play_music": play_music,
        "pause_music": pause_music,
        "stop_music": stop_music,
        "tell_time": tell_time,
        "shutdown": shutdown,
        "restart": restart,
        "volume_up": volume_up,
        "volume_down": volume_down
    }
    if prediction in actions:
        actions[prediction]()
    else:
        print("🤖 Command recognized but no action is mapped.")

# === VOICE INPUT ===

recognizer = sr.Recognizer()
mic = sr.Microphone()

def recognize_command():
    print("\n🎤 Say something...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command_text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command_text}")
        command_vec = vectorizer.transform([command_text])
        prediction = clf.predict(command_vec)[0]
        print(f"🤖 Recognized Command: {prediction}")
        execute_command(prediction)

    except sr.UnknownValueError:
        print("❌ Sorry, I couldn't understand the audio.")
    except sr.RequestError as e:
        print(f"⚠️ Could not request results; {e}")

# === MAIN LOOP ===

if __name__ == "__main__":
    print("🔊 Voice Command Classifier with Action Execution")
    print("Press Ctrl+C to quit.\n")

    try:
        while True:
            recognize_command()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Exiting. Goodbye!")

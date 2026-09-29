Voice Command Classifier with Action Execution

A Python desktop assistant that listens to spoken commands, classifies the intent with a machine learning model, and runs the matching action on your computer. Built during my internship at Edupheonix.

How it works
Speech to text: Captures microphone input and transcribes it using Google's Speech Recognition API (SpeechRecognition).
Intent classification: Converts the text into features with CountVectorizer (bag-of-words) and predicts the intent with a Multinomial Naive Bayes classifier trained on a small command dataset.
Action execution: Maps the predicted intent to a Python function that performs the task.
Supported commands
Intent	Example phrase	Behavior
Open / close browser	"open browser"	Launches / kills Microsoft Edge
Play music	"play music"	Plays a song from a local music folder
Tell time	"what time is it"	Prints the current time
Shutdown / restart	"shutdown computer"	Safe demo mode (real command commented out)
Pause / stop music, volume up / down	"increase volume"	Placeholder, not yet implemented
Tech stack

Python · SpeechRecognition · scikit-learn · PyAudio · Windows OS commands

Setup
bash
pip install SpeechRecognition scikit-learn pyaudio
python voice_assistant.py

Speak a command when you see the 🎤 prompt. Press Ctrl+C to quit.

Future improvements
Implement volume, pause, and stop controls
Expand the training data so phrasing variations are recognized more reliably
Add wake-word detection and offline speech recognition
Cross-platform support (currently Windows-only paths and commands)

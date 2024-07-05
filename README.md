# Desktop Voice Assistant

A desktop voice assistant that recognizes human voice commands and performs tasks accordingly using the speech recognition module. This assistant can perform various tasks such as opening websites, playing music, checking the time, and sending emails.

## Installation

To run this project, you need to install the following Python packages. Please make sure you have an active internet connection.

```bash
pip install pyttsx3
pip install speech_recognition
pip install wikipedia
```

## How to Run

To run this voice assistant, an internet connection is required. 

## Modules

- **pyttsx3**: Enables the computer to speak.
- **speech_recognition**: Recognizes human voice.
- **datetime**: Provides the current time.
- **wikipedia**: Searches in Wikipedia.
- **webbrowser**: Opens websites in a browser.
- **os**: Opens files.
- **smtplib**: Sends emails.

## Main Engine for pyttsx3

```python
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
```

## Usage

The assistant can perform the following tasks:

- **Search Wikipedia**: "wikipedia [search term]"
- **Open YouTube**: "open YouTube"
- **Open Google**: "open Google"
- **Play Music**: "play music"
- **Check the Time**: "the time"
- **Open PyCharm**: "open PyCharm"
- **Send Email**: "email to Dhanush"
- **Close the Assistant**: "close"
- **General Interaction**: "hello", "thank you"

Ensure you replace placeholders such as `youremail@gmail.com` and `your-password` with actual email credentials for the email functionality to work.

Enjoy your voice assistant!

"""
Flask server for Emotion Detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detect():
    """
    Detect the emotion of the text input and return a formatted response string
    """
    text_to_analyse = request.args.get("textToAnalyze") #from java script
    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Render the main index page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
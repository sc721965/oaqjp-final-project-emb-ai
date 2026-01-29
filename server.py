"""
Flask server for Emotion Detection Application.

This module provides a web interface for emotion detection using the Watson NLP API.
It includes routes for rendering the main page and processing emotion detection requests.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle emotion detection requests.
    
    Retrieves text from request arguments, processes it through the emotion detector,
    and returns formatted results or an error message for invalid input.
    
    Returns:
        str: Formatted emotion analysis results or error message.
    """
    # Get the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Extract dominant emotion
    dominant_emotion = response['dominant_emotion']

    # Check if dominant_emotion is None (error case)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Extract emotion scores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    # Format the response string
    formatted_response = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

    return formatted_response

@app.route("/")
def render_index_page():
    """
    Render the main index page.
    
    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

"""
Flask server for Emotion Detection Application
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route to handle emotion detection requests
    """
    # Get the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Call the emotion_detector function
    response = emotion_detector(text_to_analyze)
    
    # Extract emotion scores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
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
    Route to render the main index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

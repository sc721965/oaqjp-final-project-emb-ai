import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyze emotions in the given text using Watson NLP Emotion Predict function.
    
    Args:
        text_to_analyze: The text string to analyze for emotions
        
    Returns:
        A dictionary containing emotion scores and the dominant emotion
    """
    # Define the URL for the Emotion Predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define the headers with the model ID
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the input JSON with the text to analyze
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Make the POST request to the API
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check for status code 400 (blank or invalid input)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Convert response text to dictionary
    response_dict = json.loads(response.text)
    
    # Extract emotion scores from the response
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Extract the required emotions
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Find the dominant emotion (emotion with highest score)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

from flask import Flask, render_template, request
from emotion_detection import emotion_detector

# Instantiate the primary Flask micro web service application framework engine
app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    # Extract the dynamic text message string passed from browser client networks
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Send the raw string data into the Watson core script to fetch scores metric map
    response = emotion_detector(text_to_analyze)
    
    # Isolate individual emotion score metric values from the structural response payload mapping
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']
    
    # Construct formatting sentence template target strings for client output view
    output_message = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )
    return output_message

@app.route("/")
def render_index_page():
    # Serve the static UI HTML layout elements out to client browsers
    return render_template('index.html')

if __name__ == "__main__":
    # Launch microserver instance listening on universal host interface boundaries
    app.run(host="0.0.0.0", port=5000)
# Locate the last line and change it precisely to port 5500:
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)

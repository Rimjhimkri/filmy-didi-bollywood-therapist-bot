from flask import Flask, request, jsonify, render_template
from bot import get_therapist_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    
    if not data or "message" not in data:
        return jsonify({"error": "Please send a 'message' field with your problem"}), 400
    
    user_message = data["message"].strip()
    
    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400
    
    if len(user_message) > 500:
        return jsonify({"error": "Message too long. Please keep it under 500 characters"}), 400
    
    reply = get_therapist_response(user_message)
    
    return jsonify({
        "your_problem": user_message,
        "filmy_didi_says": reply
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
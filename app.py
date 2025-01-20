from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Quiz questions and options
questions = [
    {"question": "Who was Shah Jahan's beloved queen?", "options": ["Mumtaz Mahal", "Jodha Bai", "Noor Jahan", "Rani Lakshmibai"], "answer": "Mumtaz Mahal"},
    {"question": "What material was the Taj Mahal primarily made of?", "options": ["Granite", "White Marble", "Limestone", "Sandstone"], "answer": "White Marble"},
    {"question": "How many years did it take to build the Taj Mahal?", "options": ["15 years", "22 years", "30 years", "10 years"], "answer": "22 years"},
    {"question": "Why are the minarets of the Taj Mahal slightly tilted outward?", "options": ["To allow sunlight", "To protect during earthquakes", "Architectural effect", "Persian designs"], "answer": "To protect during earthquakes"},
    {"question": "Which river flows beside the Taj Mahal?", "options": ["Ganges", "Yamuna", "Brahmaputra", "Saraswati"], "answer": "Yamuna"},
    {"question": "What was Shah Jahan's unrealized plan?", "options": ["Second Taj Mahal in black marble", "Palace near the Taj Mahal", "Temple near the river", "Monument for son"], "answer": "Second Taj Mahal in black marble"},
    {"question": "How many skilled workers were involved in building the Taj Mahal?", "options": ["5,000", "10,000", "20,000", "50,000"], "answer": "20,000"},
    {"question": "Which precious stone was NOT used in the decoration of the Taj Mahal?", "options": ["Jade", "Turquoise", "Ruby", "Lapis Lazuli"], "answer": "Ruby"},
    {"question": "Which emperor's reign saw the construction of the Taj Mahal?", "options": ["Akbar", "Aurangzeb", "Humayun", "Shah Jahan"], "answer": "Shah Jahan"},
    {"question": "Which architectural style influenced the Taj Mahal?", "options": ["Greek", "Gothic", "Mughal", "Baroque"], "answer": "Mughal"},
]

# Route for the main quiz page
@app.route('/')
def index():
    return render_template('quiz.html')

# Route to check answers and return feedback
@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answers = request.json['answers']
    correct_answers = 0
    feedback = []
    
    for idx, user_answer in enumerate(user_answers):
        correct = questions[idx]["answer"]
        if user_answer == correct:
            correct_answers += 1
            feedback.append({"correct": True, "correct_answer": correct})
        else:
            feedback.append({"correct": False, "correct_answer": correct})
    
    return jsonify({"score": correct_answers, "feedback": feedback})

if __name__ == '__main__':
    app.run(debug=True)

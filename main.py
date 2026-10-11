from fastapi import FastAPI

# Create our FastAPI application
app = FastAPI()


# Home page
@app.get("/")
def home():
    return {
        "message": "🇭🇹 Haiti Trivia Battle is running!"
    }


# Game information
@app.get("/game")
def game_info():
    return {
        "name": "Haiti Trivia Battle",
        "questions": 10,
        "points_per_correct_answer": 10,
        "players_needed": 2
    }


# Trivia questions
questions = [
    {
        "question": "What is the capital of Haiti?",
        "choices": [
            "Port-au-Prince",
            "Jacmel",
            "Cap-Haitien",
            "Les Cayes"
        ],
        "answer": "Port-au-Prince"
    },
    {
        "question": "What colors are on the Haitian flag?",
        "choices": [
            "Blue and Red",
            "Green and Yellow",
            "Black and White",
            "Orange and Blue"
        ],
        "answer": "Blue and Red"
    },
    {
        "question": "What is the national sport of Haiti?",
        "choices": [
            "Soccer",
            "Basketball",
            "Football",
            "Baseball"
        ],
        "answer": "Soccer"
    },
    {
        "question": "When is Haiti's Independence Day?",
        "choices": [
            "January 1",
            "May 18",
            "August 15",
            "December 25"
        ],
        "answer": "January 1"
    },
    {
        "question": "What is the largest city in Haiti?",
        "choices": [
            "Port-au-Prince",
            "Cap-Haitien",
            "Jacmel",
            "Les Cayes"
        ],
        "answer": "Port-au-Prince"
    }
]


# Get all trivia questions
@app.get("/questions")
def get_questions():
    return {
        "questions": questions
    } 
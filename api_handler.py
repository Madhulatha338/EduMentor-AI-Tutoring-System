# ==========================
# api_handler.py — Simulation Mode (Offline Demo + PDF Support)
# ==========================

import time
import random
import os
from PyPDF2 import PdfReader


# ==========================
# Function to read PDF text
# ==========================
def read_pdf(file_path):
    text = ""
    try:
        reader = PdfReader(file_path)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    except Exception as e:
        print("PDF Read Error:", e)

    return text


# ==========================
# Main AI Tutor Response
# ==========================
def send_query_get_response(client_placeholder, user_question, assistant_id=None, file_path=None):
    """
    Offline simulation version — no OpenAI calls.
    Returns realistic educational responses for demo use.
    """

    # Simulate AI thinking
    time.sleep(random.uniform(1.2, 2.5))

    q = user_question.lower().strip()

    # ===================================
    # IF USER UPLOADED A PDF
    # ===================================
    if file_path and os.path.exists(file_path):

        pdf_text = read_pdf(file_path)

        if pdf_text:
            return (
                "📚 Based on your uploaded study material:\n\n"
                + pdf_text[:1000] +
                "\n\n(This is a preview from your document.)"
            )

    # ===================================
    # SUBJECT-WISE PRESET RESPONSES
    # ===================================

    # --- SCIENCE ---
    if "photosynthesis" in q:
        return (
            "Photosynthesis is the process by which green plants use sunlight, carbon dioxide, "
            "and water to make food (glucose) and release oxygen. It mainly occurs in the chloroplasts of leaves."
        )

    if "force" in q:
        return (
            "Force is a push or pull acting upon an object as a result of its interaction with another object. "
            "It can change the object's motion, direction, or shape."
        )

    if "cell" in q:
        return (
            "A cell is the smallest structural and functional unit of life. "
            "All living organisms are made up of one or more cells — either unicellular or multicellular."
        )

    if "climate" in q or "weather" in q:
        return (
            "Climate refers to the average weather conditions in a particular area over a long period, "
            "while weather describes short-term atmospheric conditions."
        )

    # --- GEOGRAPHY ---
    if "plate tectonics" in q or "earthquake" in q:
        return (
            "Plate tectonics explains how Earth's lithosphere is divided into plates that move slowly over the mantle. "
            "Their movement causes earthquakes, volcanoes, and mountain formation."
        )

    if "river" in q or "erosion" in q:
        return (
            "Rivers shape the Earth's surface through erosion, transportation, and deposition. "
            "They carry sediments from higher to lower areas, carving valleys and forming fertile plains."
        )

    if "volcano" in q:
        return (
            "A volcano is an opening in the Earth's crust that allows molten rock, gases, and ash to escape from below the surface. "
            "Volcanic eruptions can form mountains and islands."
        )

    # --- MATHEMATICS ---
    if "pythagoras" in q:
        return (
            "The Pythagoras theorem states that in a right-angled triangle, "
            "the square of the hypotenuse equals the sum of the squares of the other two sides (a² + b² = c²)."
        )

    if "area of circle" in q or "circle area" in q:
        return (
            "The area of a circle is calculated using the formula A = πr², "
            "where r is the radius and π is approximately 3.1416."
        )

    if "prime number" in q:
        return (
            "A prime number is a natural number greater than 1 that has exactly two factors — 1 and itself. "
            "Examples: 2, 3, 5, 7, 11, ..."
        )

    if "mean" in q or "average" in q:
        return (
            "The mean or average of a set of numbers is the sum of all numbers divided by the total count of numbers."
        )

    # --- GENERAL CHAT ---
    if "who are you" in q or "your name" in q:
        return "I'm EduMentor — your friendly AI study companion here to make learning easy and fun!"

    if "hello" in q or "hi" in q:
        return random.choice([
            "Hello! How can I help you study today?",
            "Hi there! Ready to learn something new?",
            "Hey! What topic would you like to explore today?"
        ])

    if "thank" in q:
        return "You're very welcome! Keep up the great work 😊"

    if "how are you" in q:
        return "I'm just a bunch of code — but I'm great when you're learning something new! 😄"

    # ===================================
    # DEFAULT RESPONSE
    # ===================================
    return (
        "That's a great question! In the full online AI version, I would provide a detailed explanation "
        "using advanced AI models. For now, I'm running in offline demo mode."
    )
          🧠  AI-Powered Task Optimizer

The AI-Powered Task Optimizer is an intelligent system that analyzes an employee’s emotional state using text, facial expressions, and speech inputs and recommends suitable tasks to improve productivity and well-being.
The system also detects prolonged stress and triggers alerts for timely intervention.

This project is implemented in Python and aligns with modern AI, Machine Learning, and Data Science principles.






🎯Objectives

Detect employee emotions using multimodal inputs

Recommend tasks based on detected mood

Monitor stress levels over time

Promote a healthy and productive work environment

Ensure basic data privacy and anonymization







🛠️ Technology Stack

Programming Language: Python

Frontend / UI: Streamlit

NLP: TextBlob (Sentiment Analysis)

Audio Processing: Librosa

Machine Learning: Scikit-learn (logic-based)

Vision (Placeholder): OpenCV (simulated)






📁 Project Structure
task optimiser/

├── app.py                  # Main Streamlit application


├── requirements.txt        # Project dependencies


├── text_emotion.py         # Text emotion detection


├── face_emotion.py         # Facial emotion detection


├── speech_emotion.py       # Speech emotion detection


├── mood_engine.py          # Mood inference engine


├── task_recommender.py     # Task recommendation logic


├── stress_monitor.py       # Stress detection & alerts


├── privacy.py              # Data anonymization




⚙️ Installation & Setup


1️⃣ Clone or Download the Project


git clone <repository-url>
cd task-optimiser



2️⃣ Install Required Dependencies
pip install -r requirements.txt




If pip causes issues:



python -m pip install -r requirements.txt




3️⃣ Download TextBlob Corpora
python -m textblob.download_corpora




▶️ Running the Application
streamlit run app.py





🧪 How It Works

1.User enters text input

2.System analyzes:

3.Text emotion (NLP)

4.Facial emotion (simulated)

5.Speech emotion (simulated)

6.Final mood is inferred using ensemble logic

7.Task is recommended based on mood

8.Stress alerts are generated if stress persists



📊 Example Task Mapping


Mood              --------------------------                                              	Recommended Task


Happy             --------------------------                                	Creative / Brainstorming Tasks



Stressed	       ---------------------------                                               Light Admin & Mindfulness


Angry	            ---------------------------                                           Independent Technical Work



Sad	                -------------------------                                   Learning & Training



Neutral                                                           	Routine Tasks


📈 Future Enhancements

Real-time facial & speech emotion detection

BERT-based NLP emotion classification

Database integration (SQLite / MongoDB)

Team-level analytics dashboard

Mobile application support




👤 Author

Renuka Sharma
B.Tech / Data Science (Student Project)



📄 License

This project is for educational purposes only.












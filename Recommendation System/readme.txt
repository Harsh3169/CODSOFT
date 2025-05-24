# Task 4: Movie Recommendation System

This is a simple movie recommendation system that suggests similar movies based on genres and directors using content-based filtering. It also includes a collaborative filtering alternative and a graphical user interface (GUI).

## Features
- **Content-Based Filtering** using genres and directors
- **Collaborative Filtering** using user ratings
- GUI with search suggestions and recommendation display
- Built-in movie dataset (`movies.csv`)

## Technologies Used
- Python 3
- Pandas
- scikit-learn
- Tkinter (GUI)

## Files Included
- `recommendation_system.py` — backend logic for both content-based and collaborative filtering
- `gui.py` — GUI application for recommending movies interactively
- `movies.csv` — dataset of movie titles, genres, and directors

## How to Run (GUI)
1. Make sure all 3 files (`gui.py`, `movies.csv`, and dependencies) are in the same folder.
2. Run the GUI:
   ```bash
   python gui.py

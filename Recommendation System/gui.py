import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import messagebox, ttk

df = pd.read_csv('movies.csv')
df['features'] = df['genre'] + ' ' + df['director']

vectorizer = TfidfVectorizer()
feature_matrix = vectorizer.fit_transform(df['features'])
similarity = cosine_similarity(feature_matrix)

movie_titles = df['title'].tolist()

def recommend(movie_title):
    if movie_title not in movie_titles:
        return None
    idx = df[df['title'] == movie_title].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:4]
    return [df.iloc[i[0]]['title'] for i in sim_scores]

def on_click():
    movie = combo.get()
    result = recommend(movie)
    output_box.delete(0, tk.END)
    if result:
        for title in result:
            output_box.insert(tk.END, f"• {title}")
    else:
        messagebox.showwarning("Movie Not Found", "Movie not found in the database.")

def on_keyrelease(event):
    value = event.widget.get()
    if value == '':
        combo['values'] = movie_titles
    else:
        data = [item for item in movie_titles if value.lower() in item.lower()]
        combo['values'] = data

window = tk.Tk()
window.title("🎬 Movie Recommender System")
window.geometry("400x380")
window.resizable(False, False)

tk.Label(window, text="Movie Recommender", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Label(window, text="Select or Type a movie title:", font=("Helvetica", 12)).pack()

combo = ttk.Combobox(window, width=40)
combo['values'] = movie_titles
combo.pack(pady=5)
combo.bind('<KeyRelease>', on_keyrelease)

ttk.Button(window, text="Get Recommendations", command=on_click).pack(pady=10)

tk.Label(window, text="Top 3 Recommendations:", font=("Helvetica", 12)).pack(pady=5)

output_box = tk.Listbox(window, width=40, height=5, font=("Helvetica", 11))
output_box.pack(pady=5)

window.mainloop()
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "Movie": ["Inception", "Interstellar", "The Dark Knight", "Tenet", "Dunkirk"],
    "Genre": ["Sci-Fi Thriller", "Sci-Fi Space", "Action Crime", "Sci-Fi Time Travel", "War Drama"],
    "UserRatings": [4.8, 4.7, 4.9, 4.5, 4.2]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
genre_matrix = vectorizer.fit_transform(df["Genre"])
similarity_matrix = cosine_similarity(genre_matrix)

df["NormalizedRating"] = df["UserRatings"] / df["UserRatings"].max()

def recommend(movie_name, method="content"):
    if method == "content":
        idx = df[df["Movie"] == movie_name].index[0]
        scores = list(enumerate(similarity_matrix[idx]))
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        recommendations = [df.iloc[i[0]]["Movie"] for i in sorted_scores[1:]]
    elif method == "collaborative":
        top_rated = df.sort_values(by="NormalizedRating", ascending=False)
        recommendations = top_rated["Movie"].tolist()[1:]  # Skip highest-rated
    else:
        return "Invalid method! Choose 'content' or 'collaborative'."
    
    return recommendations

print("Content-Based Recommendations:", recommend("Interstellar", method="content"))
print("Collaborative Filtering Recommendations:", recommend("Interstellar", method="collaborative"))
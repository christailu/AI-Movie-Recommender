import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.cluster import KMeans


class MovieRecommenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommender")

        # Load movie data
        self.movies_df = pd.read_csv("IMDB-Movie-Data.csv")

        # Create GUI elements
        self.filter_label = ttk.Label(root, text="Enter Movie Name:")
        self.filter_label.grid(row=0, column=0, padx=10, pady=10)

        self.filter_entry = ttk.Entry(root, width=30)
        self.filter_entry.grid(row=0, column=1, padx=10, pady=10)

        self.cluster_button = ttk.Button(root, text="Cluster Movies", command=self.cluster_movies)
        self.cluster_button.grid(row=0, column=2, padx=10, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.movies_listbox = tk.Listbox(root, width=100, height=20)
        self.movies_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Add genre filter buttons
        genres = ["Action", "Adventure", "Sci-Fi", "Mystery", "Horror", "Thriller", "Animation", "Comedy", "Family",
                  "Fantasy", "Drama", "Music", "Biography", "History", "Crime", "Romance", "Western", "War", "Sport", "Musical"]

        self.genre_buttons = []
        self.selected_genres = []
        row_num = 3
        col_num = 0
        for genre in genres:
            button = ttk.Button(root, text=genre, command=lambda g=genre: self.toggle_genre_filter(g))
            button.grid(row=row_num, column=col_num, padx=5, pady=5)
            col_num += 1
            if col_num == 5:
                col_num = 0
                row_num += 1
            self.genre_buttons.append(button)

    def cluster_movies(self):
        movie_name = self.filter_entry.get()
        if movie_name:
            filtered_movies = self.movies_df[self.movies_df['Title'].str.contains(movie_name, case=False)]
            self.result_label.config(text=f"Filtered by Movie Name: {len(filtered_movies)} movies")
            self.display_movie_list(filtered_movies)
        else:
            self.result_label.config(text="Please enter a movie name")

    def toggle_genre_filter(self, genre):
        if genre in self.selected_genres:
            self.selected_genres.remove(genre)
        else:
            self.selected_genres.append(genre)
        self.update_filtered_count()

    def update_filtered_count(self):
        if self.selected_genres:
            filtered_movies = self.movies_df.copy()
            for genre in self.selected_genres:
                filtered_movies = filtered_movies[filtered_movies["Genre"].str.contains(genre)]
            self.result_label.config(text=f"Filtered by {', '.join(self.selected_genres)}: {len(filtered_movies)} movies")
            self.display_movie_list(filtered_movies)
        else:
            self.result_label.config(text="")
            self.movies_listbox.delete(0, tk.END)

    def display_movie_list(self, movies):
        self.movies_listbox.delete(0, tk.END)
        for idx, movie in movies.iterrows():
            self.movies_listbox.insert(tk.END, f"{movie['Title']} ({movie['Year']}) - {movie['Genre']}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MovieRecommenderApp(root)
    root.mainloop()

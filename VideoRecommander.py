from tkinter import *

class MovieRecommenderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Movie Recommender")
        self.master.geometry("700x350")
        
        self.create_widgets()

    def create_widgets(self):
        self.frame = Frame(self.mast+er, width=300, height=300)
        self.frame.grid(row=0, column=0, sticky="NW")

        self.mainLabel = Label(self.master, text="Welcome To the movie Recommender!")
        self.mainLabel.place(relx=0.5, rely=0.10, anchor=CENTER)

        self.Movies_screen = Frame(self.master)
        self.Anime_screen = Frame(self.master)

        self.Movies = Button(self.master, text="Movies", bg="grey", fg="black", command=self.show_movies_screen)
        self.Movies.place(relx=0.9, rely=0.5, anchor=CENTER)

        self.Anime = Button(self.master, text="Anime", bg="grey", fg="black", command=self.show_anime_screen)
        self.Anime.place(relx=0.11, rely=0.5, anchor=CENTER)

        self.Back = Button(self.master, text="Back", bg="grey", fg="black", command=self.show_main_frame)
        self.Back.place(relx=0.5, rely=0.9, anchor=CENTER)

    def show_movies_screen(self):
        self.hide_frames()
        self.Movies_screen.grid(row=0, column=0)
        self.mainLabel.config(text="Movies Here")

    def show_anime_screen(self):
        self.hide_frames()
        self.Anime_screen.grid(row=0, column=0)
        self.mainLabel.config(text="Anime Here")

    def show_main_frame(self):
        self.hide_frames()
        self.frame.grid(row=0, column=0)
        self.mainLabel.config(text="Welcome To the movie Recommender!")

    def hide_frames(self):
        self.frame.grid_forget()
        self.Movies_screen.grid_forget()
        self.Anime_screen.grid_forget()

def main():
    root = Tk()
    app = MovieRecommenderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import random


class Media:
    def __init__(self, title, publication_year, genre, views):
        self.title = title
        self.publication_year = publication_year
        self.genre = genre
        self.views = views

    def play(self):
        self.views += 1


class Movie(Media):
    def __init__(self, title, publication_year, genre, views):
        super().__init__(title, publication_year, genre, views)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


class TVSeries(Media):
    def __init__(self, title, publication_year, genre, episode_number, season_number, views):
        super().__init__(title, publication_year, genre, views)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02}E{self.episode_number:02}"


def get_movies(library):
    movies = [media for media in library if isinstance(media, Movie)]
    return sorted(movies, key=lambda x: x.title)


def get_series(library):
    series = [media for media in library if isinstance(media, TVSeries)]
    return sorted(series, key=lambda x: x.title)


def search(library, title):
    results = [media for media in library if title.lower() in media.title.lower()]
    return results


def generate_views(library):
    random_media = random.choice(library)
    random_views = random.randint(1, 100)
    random_media.views += random_views


def generate_views_x10(library):
    for i in range(10):
        generate_views(library)


def top_titles(library, count, content_type=None):
    if content_type == 'movies':
        sorted_library = sorted(get_movies(library), key=lambda x: x.views, reverse=True)
    elif content_type == 'series':
        sorted_library = sorted(get_series(library), key=lambda x: x.views, reverse=True)
    else:
        sorted_library = sorted(library, key=lambda x: x.views, reverse=True)

    return sorted_library[:count]


movie1 = Movie("Pulp Fiction", 1994, "Crime", 207456)
movie2 = Movie("The Shawshank Redemption", 1994, "Drama", 198273)
series1 = TVSeries("Breaking Bad", 2008, "Drama", 5, 7, 325476)
series2 = TVSeries("Game of Thrones", 2011, "Fantasy", 8, 3, 238765)
my_library = [movie1, movie2, series1, series2]

generate_views_x10(my_library)
top_titles_result = top_titles(my_library, 2)
print("Top titles:", [str(media) for media in top_titles_result])

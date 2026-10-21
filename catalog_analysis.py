import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    total_rating = sum(movie["rating"] for movie in movies)
    return round(total_rating / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    average_age = math.ceil(sum(ages) / len(ages))
    return max(ages), min(ages), average_age


def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


def print_non_comedy_movies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def print_first_masterpiece(movies):
    index = 0
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > 9.0:
            print(movie["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    words = title.split()
    normalized_words = []
    for word in words:
        normalized_words.append(word[0].upper() + word[1:])
    return " ".join(normalized_words)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


def count_by_genre(movies):
    genre_counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography[actor] = filmography.get(actor, [])
            filmography[actor].append(movie["title"])
    return filmography


def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def main():
    print("Этап 1")
    print("Средний рейтинг:", average_rating(movies))

    oldest_age, newest_age, average_age = catalog_age_stats(movies)
    print("Максимальный возраст, лет:", oldest_age)
    print("Минимальный возраст, лет:", newest_age)
    print("Средний возраст, лет:", average_age)

    duration = duration_in_hours(movies[0]["duration_min"])
    print("Длительность первого фильма", duration)

    print()
    print("Этап 2")
    movie = movies[0]
    print("Категория рейтинга первого фильма:", rating_tier(movie["rating"]))
    print("Категория года первого фильма:", decade_label(movie["year"]))

    print()
    print("Этап 3")
    print("Фильмы без жанра comedy:")
    print_non_comedy_movies(movies)

    print("Первый фильм с рейтингом выше 9.0:")
    print_first_masterpiece(movies)

    print("Поиск в каталоге без фильмов с рейтингом выше 9.0:")
    movies_without_masterpieces = [movie for movie in movies if movie["rating"] <= 9.0]
    print()
    print_first_masterpiece(movies_without_masterpieces)
    print("Фильмов длиннее 120 минут:", count_long_movies(movies))

    print()
    print("Этап 4")
    title = normalize_title(movie["title"])
    print("Нормализованное название:", title)
    print("Слаг:", make_slug(title))
    print(format_report_line(movie))

    print()
    print("Этап 5")
    print("Названия по убыванию рейтинга:", titles_sorted_by_rating(movies))
    print("Топ-3 по рейтингу:", top_n_by_rating(movies))

    print()
    print("Этап 6")
    print("Фильмов по жанрам:", count_by_genre(movies))
    print("Фильмография актёров:", actor_filmography(movies))

    mean_rating = average_rating(movies)
    above_average = {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > mean_rating
    }
    print("Фильмы с рейтингом выше среднего:", above_average)

    print()
    print("Этап 7")
    print("Все жанры:", all_genres(movies))
    print(
        "Общие актёры первого и четвёртого фильмов:",
        common_actors(movies[0], movies[3]),
    )
    print(
        "Жанры шестого фильма, которых нет в первых пяти:",
        genres_only_in_one(movies[5:6], movies[:5]),
    )

    print()
    print("Этап 8")
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))

    total_duration = sum(
        movie["duration_min"] for movie in movies if movie["rating"] > 7
    )
    print("Длительность фильмов с рейтингом выше 7, мин:", total_duration)


if __name__ == "__main__":
    main()

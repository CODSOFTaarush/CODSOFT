print("=" * 40)
print("🎬 MOVIE RECOMMENDATION SYSTEM")
print("=" * 40)

movies = {
    "action": ["Avengers", "John Wick", "Batman"],
    "comedy": ["Mr. Bean", "The Mask", "Home Alone"],
    "horror": ["Conjuring", "Insidious", "Nun"],
    "sci-fi": ["Interstellar", "Inception", "Matrix"]
}

while True:
    genre = input("\nEnter genre (action/comedy/horror/sci-fi) or 'exit': ").lower()

    if genre == "exit":
        print("Thank you for using the Recommendation System!")
        break

    elif genre in movies:
        print("\nRecommended Movies:")
        for movie in movies[genre]:
            print("⭐", movie)

    else:
        print("Invalid genre! Please try again.")
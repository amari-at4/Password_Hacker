def tallest_people(**kwargs):
    tallest = {}
    for name, height in sorted(kwargs.items()):
        tallest.setdefault(height, []).append(name)
    tallest_height = sorted(tallest, reverse=True)[0]
    for people in tallest.get(tallest_height):
        print(f"{people} : {tallest_height} ")

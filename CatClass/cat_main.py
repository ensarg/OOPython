from Cat import Cat


# Example usage
if __name__ == "__main__":
    my_cat = Cat("Whiskers", 3, "Gray")
    print(f"My cat's name is {my_cat.get_name()}")
    print(f"It is {my_cat.get_age()} years old.")
    print(f"Its color is {my_cat.get_color()}")

    my_cat.meow()

from Counter import Counter  # Import the Counter class from counter.py


if __name__ == "__main__":
    c1 = Counter()        # Default constructor, count = 0
    c2 = Counter(5)       # Constructor with initial value

    c1.increment()        # Increment by 1
    # c1.increment()      # (Commented out, as in Java)

    c2.increment()        # Increment by 1
    c2.increment()        # Increment by 1

    print("counter =", c1.get_count())
    print("counter2 =", c2.get_count())

    # print("counter2 =", c2.count)  # This would access the count directly

    # print("\n hello again")  # Commented out, as in Java

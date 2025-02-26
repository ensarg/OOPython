class Counter:
    def __init__(self, initial_value=0):
        """Constructor: Sets the count to the initial value (default is 0)."""
        self.count = initial_value

    def get_count(self):
        """Returns the current count value."""
        return self.count

    def increment(self, delta=1):
        """Increments the count by 1 (default) or a specified delta."""
        self.count += delta

    def reset(self):
        """Resets the count to zero."""
        self.count = 0

try:
        result = 10 / 0
        print(int(result))
except ZeroDivisionError as e:
        print(f"Error: {e}")
else:
        print("No exception occurred.")
finally:
        print("This will always execute.")


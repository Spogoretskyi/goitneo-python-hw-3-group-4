def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name please."
        except IndexError:
            return "Give me name and phone please."
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    return inner
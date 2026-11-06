def log_result(text):
    with open("input_errors.log", "a", encoding="utf-8") as f:
        f.write(text + "\n")
def print_and_log(text):
    print(text)
    log_result(text)
    
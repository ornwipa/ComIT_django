def hello_world():
    print("hello world")

if __name__ == "__main__":
    hello_world() # method doesn't get invoked during import

hello_world() # method gets invoked when module is imported
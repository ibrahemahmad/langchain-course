import os

from dotenv import load_dotenv


def main():
    # look for env file
    load_dotenv()
    print("Hello from langchain-course!")
    print(os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()

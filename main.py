import speech_recognition as speech_recog
import random
import time

# Функция распознавания речи
def speech():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="en-EN")

# Наборы слов для разных уровней сложности
levels = {
    "easy": ["dairy", "mouse", "computer"],
    "medium": ["programming", "algorithm", "developer"],
    "hard": ["neural network", "machine learning", "artificial intelligence"]
}

# Функция игры
def play_game(level):
    words_to_guess = levels[level]
    score = 0
    num_words = len(words_to_guess)

    print(f"Хай на  {level} уровне!")
    print("Произнеси эти слова:")

    # Перебираем слова для угадывания
    for word in words_to_guess:
        print(word)
        print("Говорите...")

        # Получаем ответ пользователя
        try:
            user_input = speech()
            if user_input.lower() == word.lower():
                print("Правильно")
                score += 1
            else:
                print("Не правильно")

            time.sleep(2)  
        except speech_recog.UnknownValueError:
            print("Извини, твоего голоса не было слышно")
        except speech_recog.RequestError as e:
            print(f"Error: {e}")

    print(f"Игра окончена, твои очки: {score}/{num_words}")

# Главная функция
def main():
    print("Добро пожаловать в игру по распознаванию речи!")
    print("Выбери сложность игры: easy, medium, hard")
    level = input("Введите уровень игры: ").lower()

    if level in levels:
        play_game(level)
    else:
        print("Неверный уровень. Выберите easy, medium, hard")

if __name__ == "__main__":
    main()

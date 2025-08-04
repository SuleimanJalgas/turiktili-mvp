import random

# Бастапқы қазақша-түрікше сөздік
translations = {
    "merhaba": "сәлем",
    "teşekkürler": "рахмет",
    "evet": "иә",
    "hayır": "жоқ",
    "gün": "күн",
}

def translate_to_kazakh(turkish_word: str) -> str | None:
    """Берілген түрік сөзінің қазақша аудармасын қайтарады.

    Args:
        turkish_word: Түрік тіліндегі сөз.
    Returns:
        Қазақ тіліндегі аудармасы немесе None егер сөз табылмаса.
    """
    return translations.get(turkish_word.lower())

def translate_to_turkish(kazakh_word: str) -> str | None:
    """Берілген қазақ сөзінің түрікше аудармасын қайтарады."""
    for turkish, kazakh in translations.items():
        if kazakh == kazakh_word.lower():
            return turkish
    return None

def quiz() -> None:
    """Кездейсоқ сөзді сұрап, пайдаланушыдан жауап алады."""
    turkish, kazakh = random.choice(list(translations.items()))
    print(f"'{kazakh}' деген сөздің түрікшесі қандай?")
    answer = input("Жауабыңыз: ").strip().lower()
    if answer == turkish:
        print("Дұрыс!")
    else:
        print(f"Қате. Дұрыс жауап: {turkish}")

if __name__ == "__main__":
    quiz()

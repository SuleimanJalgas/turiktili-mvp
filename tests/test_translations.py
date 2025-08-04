import os
import sys
from unittest.mock import patch

# Ensure root directory is on path for imports
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from turkish_kazakh_app import (
    translate_to_kazakh,
    translate_to_turkish,
    quiz,
)


def test_translate_to_kazakh():
    assert translate_to_kazakh("merhaba") == "сәлем"
    assert translate_to_kazakh("TEŞEKKÜRLER") == "рахмет"


def test_translate_to_turkish():
    assert translate_to_turkish("иә") == "evet"
    assert translate_to_turkish("жоқ") == "hayır"


def test_quiz_correct_answer(capsys):
    with patch("random.choice", return_value=("merhaba", "сәлем")), patch(
        "builtins.input", return_value="merhaba"
    ):
        quiz()
    captured = capsys.readouterr()
    assert "Дұрыс!" in captured.out


def test_quiz_incorrect_answer(capsys):
    with patch("random.choice", return_value=("merhaba", "сәлем")), patch(
        "builtins.input", return_value="yanlış"
    ):
        quiz()
    captured = capsys.readouterr()
    assert "Қате. Дұрыс жауап: merhaba" in captured.out

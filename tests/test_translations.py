import os
import sys

# Ensure root directory is on path for imports
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from turkish_kazakh_app import translate_to_kazakh, translate_to_turkish


def test_translate_to_kazakh():
    assert translate_to_kazakh("merhaba") == "сәлем"
    assert translate_to_kazakh("TEŞEKKÜRLER") == "рахмет"


def test_translate_to_turkish():
    assert translate_to_turkish("иә") == "evet"
    assert translate_to_turkish("жоқ") == "hayır"

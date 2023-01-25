from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    """Test arguments with wrong types"""
    with pytest.raises(TypeError):
        encrypt_message(1, 2)

    with pytest.raises(TypeError):
        encrypt_message("string", "1")

    """Test key is not a valid positive index of message"""
    assert encrypt_message("string", 6) == "".join(reversed("string"))

    """Test key is odd"""
    assert encrypt_message("string", 3) == "rts_gni"
    assert encrypt_message("string", 3) != "gni_rts"

    """Test key is even"""
    assert encrypt_message("string", 2) == "gnir_ts"

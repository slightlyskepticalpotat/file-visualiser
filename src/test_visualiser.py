import pytest
import visualiser

def test_get_file_raw(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: "fake.txt")
    with pytest.raises(ValueError):
        project.get_file_raw()

def test_build_image_bw():
    assert project.build_image_bw([0, 255, 0, 255], 2) != None

def test_next_byte():
    source = project.next_byte([i for i in range(100)])
    for i in range(100):
        next(source)

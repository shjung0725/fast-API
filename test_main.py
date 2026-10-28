from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Check that the health endpoint returns status ok
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# Check that predict returns correct counts for a short sentence
def test_predict_short():
    response = client.post("/predict", json={"text": "hello world"})
    assert response.status_code == 200
    body = response.json()
    assert body["word_count"] == 2
    assert body["char_count"] == 11
    assert body["label"] == "short"


# Check that predict labels a long sentence as long
def test_predict_long():
    text = "one two three four five six seven eight nine ten eleven"
    response = client.post("/predict", json={"text": text})
    assert response.json()["label"] == "long"

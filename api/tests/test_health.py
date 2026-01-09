import run


def test_health_check():
    with run.app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.data.decode("utf-8") == "ok"

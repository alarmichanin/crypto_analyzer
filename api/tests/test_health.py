import run


def test_health_check():
    with run.app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.get_data(as_text=True) == "ok"

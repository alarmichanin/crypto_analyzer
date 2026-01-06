from run import app

def test_health_check():
    with app.test_client() as client:
        responce = client.get('/health')
        
        assert responce.status_code == 200
        assert responce.data.decode('utf-8') == 'ok'
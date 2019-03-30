
from main import app

def test_for_invalid_main_page():
    with app.test_client() as test1:
        res1 = test1.get("http://127.0.0.1:5000/adjfhdkjfhs")
        assert res1.status_code == 404

def test_for_invalid_home_page():
    with app.test_client() as test2:
        res2 = test2.get("http://127.0.0.1:5000/home/alkdfjlakdfjklsa")
        assert res2.status_code == 404

def test_for_invalid_about_page():
    with app.test_client() as test3:
        res3 = test3.get("http://127.0.0.1:5000/about/alkdfjlakdfjklsa")
        assert res3.status_code == 404
def test_for_success_main_page():
    with app.test_client() as test1:
        res1 = test1.get("http://127.0.0.1:5000/")
        assert res1.status_code == 200


```python
"""
Posts API Testing with Python Requests
"""
import requests

class TestPostsAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def test_get_posts(self):
        response = requests.get(f"{self.BASE_URL}/posts")
        assert response.status_code == 200
        posts = response.json()
        assert len(posts) > 0
        print("✅ GET /posts test passed")
    
    def test_create_post(self):
        new_post = {
            "title": "Test Post Title",
            "body": "This is a test post body",
            "userId": 1
        }
        
        response = requests.post(f"{self.BASE_URL}/posts", json=new_post)
        assert response.status_code == 201
        print("✅ POST /posts test passed")

if __name__ == "__main__":
    posts_tester = TestPostsAPI()
    posts_tester.test_get_posts()
    posts_tester.test_create_post()
```
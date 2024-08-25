import unittest

from starlette.testclient import TestClient

from api.main import app


def get_testing_client():
    return TestClient(app, headers={"Host": "localhost"})


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = get_testing_client()

    def test_correct_info(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertEqual({"version": "dev"}, response.json())

    def test_echo(self):
        msg = {"msg": "hello"}
        response = self.client.post("/echo", json=msg)
        self.assertEqual(200, response.status_code)
        self.assertEqual(msg, response.json())


if __name__ == "__main__":
    unittest.main()

from rest_framework.test import APITestCase

class FibonacciAPITest(APITestCase):
    def setUp(self):
        self.url = '/fib' 

    def test_valid_input(self):
        params = {'n': 99}
        response = self.client.get(self.url, params, format='json')
        # ステータスコードの確認
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['result'], 218922995834555169026)

    # 負の値を入力した場合エラー
    def test_negative_input(self):
        params = {'n': -1}
        response = self.client.get(self.url, params, format='json')
        self.assertEqual(response.status_code, 400)
        error = response.data['error']
        self.assertEqual(error, '0以上の値を入力してください')

    # 文字列を入力した場合エラー
    def test_str_input(self):
        params = {'n': 'aaa'}
        response = self.client.get(self.url, params, format='json')
        self.assertEqual(response.status_code, 400)
        error = response.data['error']
        self.assertEqual(error, '数値を入力してください')
    
    # 小数点入力した場合もエラー
    def test_float_input(self):
        params = {'n': '1.0'}
        response = self.client.get(self.url, params, format='json')
        self.assertEqual(response.status_code, 400)
        error = response.data['error']
        self.assertEqual(error, '数値を入力してください')
        
    # パラメータがない時もエラー
    def test_no_input(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 400)
        error = response.data['error']
        self.assertEqual(error, '数値を入力してください')
    

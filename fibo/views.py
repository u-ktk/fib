from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# フィボナッチ数列の計算をメモ化して、再帰呼び出し部分の計算量を減らす
memo = {}

def calculate_fib(n):
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = calculate_fib(n-1) + calculate_fib(n-2)
        
    # 結果をメモに保存
    memo[n] = result
    return result    

class FibView(APIView):
    def get(self, request):
        # クエリからnを取得、もしnが指定されていない場合はNoneを返す
        n = request.query_params.get('n', None)
        try:
            n = int(n)
        # 例外処理（不適切な型、値）
        # 何も入力していない場合([NoneType])TypeError,数値以外を入力した場合はValueError
        except (TypeError, ValueError):
            return Response({'error': '数値を入力してください'}, status=status.HTTP_400_BAD_REQUEST)
        # 負の値を入力した場合エラー
        if n < 0:
            return Response({'error': '0以上の値を入力してください'},status=status.HTTP_400_BAD_REQUEST)

        result = calculate_fib(n)
        return Response({'result': result})

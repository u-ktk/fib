### URI
http://u-ktk-fib.com/fib

### リクエスト例
```
curl -X GET -H "Content-Type: application/json" "http://u-ktk-fib.com/fib?n=99"
```
-> {"result":218922995834555169026}
### エラー例
```
curl -X GET -H "Content-Type: application/json" "http://u-ktk-fib.com/fib?n=-1"
```
-> {"status":400,"message":"0以上の値を入力してください"}

```
curl -X GET -H "Content-Type: application/json" "http://u-ktk-fib.com/fib?n=xxx"
```
-> {"status":400,"message":"数値を入力してください"}


### ソースコードの構成など
+ Django　REST Frameworkを使ってREST APIを開発しました。
  Djangoのプロジェクト名は"Speee" アプリケーション名は"fibo"となっています。
+ fibo > views.py > FibViewクラスで、実際にクライアントに返すAPIビューを定義しています。
  def get(self, request)はGETリクエストを処理するメソッドです。
+ フィボナッチ数列を計算する関数は再帰呼び出しを行っていますが、無駄な計算を防ぐため、計算結果をメモするための辞書も定義しました。
+ test_views.pyに、正常なリクエストを送った場合と、不正なリクエストを送った場合のユニットテストを記述しています。
+ fibo > urls.py　でルーティングの設定を行っており、(サーバー名)/fibo/にアクセスした際FibViewクラスを呼び出しています。
+ Dockerfileは開発環境と本番環境の処理を分けて記述しています。本番環境ではGunicornを用いてDjangoアプリを実行しています。
+ 本番環境では、Amazon EC2インスタンス内でDockerを起動しています。

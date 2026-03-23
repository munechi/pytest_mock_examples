# mock の書き方メモ

`tests` には、`hogelib.main.greet` を差し替える 3 パターンのサンプルがあります。

- `unittest.mock.patch`
  標準ライブラリだけで完結する、いちばん基本の書き方です。
- `pytest-mock`
  pytest の fixture と相性がよく、テストが増えたときに整理しやすい書き方です。
- `monkeypatch + Mock`
  `monkeypatch` のシンプルな差し替えと、`Mock` の呼び出し検証を両立する書き方です。

今回のサンプルでは、どの書き方でも次の 2 点をそろえています。

- `hoge()` の戻り値が `"mocked"` になること
- 差し替えた `greet()` が 1 回だけ呼ばれること

実務では、用途ごとに次のように使い分けると分かりやすいです。

- 標準機能だけで書きたいときは `patch`
- pytest に寄せて統一したいときは `pytest-mock`
- 関数や環境変数を手軽に差し替えたいときは `monkeypatch`

`return_value` と `side_effect` の違いを見たいときは、`tests/test_mock_basics.py` を見ると最小例で追いやすいです。

同期の `httpx.Client` を差し替える例は `tests/test_api.py`、非同期の `httpx.AsyncClient` を `pytest-mock` と `AsyncMock` で差し替える例は `tests/test_api_async.py` にあります。

`httpx.Client` や `httpx.AsyncClient` を直接 mock したくないときは、`src/hogelib/http_client.py` のような薄いラッパーを作って、そのラッパー関数を patch するとテストがかなり簡単になります。

普段の方針としては、まず `pytest-mock` を第一候補にして、環境変数や属性の差し替えが自然な場面だけ `monkeypatch` を使う運用にすると迷いにくいです。

pytest のテスト関数に出てくる `tmp_path` や `monkeypatch` は、pytest が標準で提供している fixture です。`mocker` は `pytest-mock` をインストールすると使える fixture で、どれも import ではなく pytest が引数名を見て自動で渡しています。

型ヒントを付けたいときの import は次のとおりです。

- `monkeypatch` -> `from pytest import MonkeyPatch`
- `tmp_path` -> `from pathlib import Path`
- `mocker` -> `from pytest_mock import MockerFixture`

`patch` や `monkeypatch.setattr` でモジュールパスを書くときは、関数の定義場所ではなく、テスト対象コードが参照している場所を置き換えます。今回の `hoge()` は `src/hogelib/main.py` の中で `from .greet import greet` しているので、置き換えるのは `hogelib.greet.greet` ではなく `hogelib.main.greet` です。

import の形によって、置き換える場所は次のように変わります。

- `from x import y`
  使う側のモジュールにある `y` を置き換えます。
- `import x`
  使う側のモジュールにある `x.y` が参照されるので、`x` を import している側のモジュールを起点に考えます。
- `from x import y as z`
  使う側では `z` という名前で参照しているので、その `z` を置き換えます。

同じ関数が複数のモジュールで参照されている場合は、参照先ごとに置き換えが必要です。

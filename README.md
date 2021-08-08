# エラー出現中

basic認証を作ろうと写経したらサーバー起動時に以下のエラー

```
Traceback (most recent call last):
  File "run.py", line 1, in <module>
    from urls import app
  File "/home/ubuntu/fastAPI_Tutorial/urls.py", line 6, in <module>
    app.add_api_route('/admin',admin)
  File "/home/ubuntu/.local/lib/python3.6/site-packages/fastapi/applications.py", line 264, in add_api_route
    openapi_extra=openapi_extra,
  File "/home/ubuntu/.local/lib/python3.6/site-packages/fastapi/routing.py", line 543, in add_api_route
    openapi_extra=openapi_extra,
  File "/home/ubuntu/.local/lib/python3.6/site-packages/fastapi/routing.py", line 400, in __init__
    self.dependant = get_dependant(path=self.path_format, call=self.endpoint)
  File "/home/ubuntu/.local/lib/python3.6/site-packages/fastapi/dependencies/utils.py", line 298, in get_dependant
    param=param, path=path, security_scopes=security_scopes
  File "/home/ubuntu/.local/lib/python3.6/site-packages/fastapi/dependencies/utils.py", line 123, in get_param_sub_dependant
    security_scopes=security_scopes,
  File "/home/ubuntu/.local/lib/python3.6/site-packages/fastapi/dependencies/utils.py", line 159, in get_sub_dependant
    use_cache=depends.use_cache,
  File "/home/ubuntu/.local/lib/python3.6/site-packages/fastapi/dependencies/utils.py", line 290, in get_dependant
    endpoint_signature = get_typed_signature(call)
  File "/home/ubuntu/.local/lib/python3.6/site-packages/fastapi/dependencies/utils.py", line 246, in get_typed_signature
    signature = inspect.signature(call)
  File "/usr/lib/python3.6/inspect.py", line 3065, in signature
    return Signature.from_callable(obj, follow_wrapped=follow_wrapped)
  File "/usr/lib/python3.6/inspect.py", line 2815, in from_callable
    follow_wrapper_chains=follow_wrapped)
  File "/usr/lib/python3.6/inspect.py", line 2193, in _signature_from_callable
    raise TypeError('{!r} is not a callable object'.format(obj))
TypeError: <module 'fastapi.security' from '/home/ubuntu/.local/lib/python3.6/site-packages/fastapi/security/__init__.py'> is not a callable object
```
# 考察
クラスを呼び出せていない

# 参考
https://rightcode.co.jp/blog/information-technology/fastapi-tutorial-todo-apps-authentication-user-registration

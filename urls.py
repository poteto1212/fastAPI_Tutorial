from contorollers import *

#表紙ページ
app.add_api_route('/',index)
#管理者ページ
app.add_api_route('/admin',admin)

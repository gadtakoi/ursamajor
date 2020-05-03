DEBUG = True
STATIC_ROOT = '/tmp/static/'
ALLOWED_HOSTS = ['*']
YNDX_TRNS_API_KEY = "trnsl.1.1.20200428T777744Z.e8888888c2b4f6e6.b9999999bbe75fdbc1035a55555555555d742c2d"
YNDX_TRNS_URL = "https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&lang=ru".format(YNDX_TRNS_API_KEY)

"""
Bayan HTTP Library - مكتبة HTTP للبيان
http / شبكة

Provides HTTP operations with bilingual (Arabic/English) names.
Uses urllib for basic HTTP without external dependencies.
"""

import urllib.request as _request
import urllib.parse as _parse
import urllib.error as _error
import json as _json
import ssl as _ssl

# Create SSL context that doesn't verify certificates (for simplicity)
_ssl_context = _ssl.create_default_context()
_ssl_context.check_hostname = False
_ssl_context.verify_mode = _ssl.CERT_NONE

# ============ Basic HTTP Methods - طرق HTTP الأساسية ============

def get(url, headers=None, timeout=30):
    """HTTP GET request - طلب GET"""
    req = _request.Request(url, headers=headers or {})
    try:
        with _request.urlopen(req, timeout=timeout, context=_ssl_context) as response:
            return {
                'status': response.status,
                'headers': dict(response.headers),
                'body': response.read().decode('utf-8'),
                'url': response.url
            }
    except _error.HTTPError as e:
        return {'status': e.code, 'error': str(e), 'body': e.read().decode('utf-8', errors='ignore')}
    except _error.URLError as e:
        return {'status': 0, 'error': str(e.reason)}
احصل = طلب_احصل = get

def post(url, data=None, json_data=None, headers=None, timeout=30):
    """HTTP POST request - طلب POST"""
    headers = headers or {}
    if json_data is not None:
        data = _json.dumps(json_data).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    elif data is not None:
        if isinstance(data, dict):
            data = _parse.urlencode(data).encode('utf-8')
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
        elif isinstance(data, str):
            data = data.encode('utf-8')
    
    req = _request.Request(url, data=data, headers=headers, method='POST')
    try:
        with _request.urlopen(req, timeout=timeout, context=_ssl_context) as response:
            return {
                'status': response.status,
                'headers': dict(response.headers),
                'body': response.read().decode('utf-8'),
                'url': response.url
            }
    except _error.HTTPError as e:
        return {'status': e.code, 'error': str(e), 'body': e.read().decode('utf-8', errors='ignore')}
    except _error.URLError as e:
        return {'status': 0, 'error': str(e.reason)}
أرسل = طلب_أرسل = post

# ============ JSON API - واجهة JSON ============

def get_json(url, headers=None, timeout=30):
    """GET request returning JSON - طلب GET يرجع JSON"""
    headers = headers or {}
    headers['Accept'] = 'application/json'
    response = get(url, headers, timeout)
    if 'body' in response and response.get('status', 0) == 200:
        try:
            response['json'] = _json.loads(response['body'])
        except _json.JSONDecodeError:
            response['json'] = None
    return response
احصل_جيسون = طلب_جيسون = get_json

def post_json(url, data, headers=None, timeout=30):
    """POST JSON data - إرسال بيانات JSON"""
    return post(url, json_data=data, headers=headers, timeout=timeout)
أرسل_جيسون = إرسال_جيسون = post_json

# ============ URL Operations - عمليات الروابط ============

def encode_url(text):
    """URL encode text - ترميز النص للرابط"""
    return _parse.quote(text, safe='')
رمز_رابط = ترميز_رابط = encode_url

def decode_url(text):
    """URL decode text - فك ترميز الرابط"""
    return _parse.unquote(text)
فك_رابط = فك_ترميز_رابط = decode_url

def parse_url(url):
    """Parse URL into components - تحليل الرابط إلى مكونات"""
    parsed = _parse.urlparse(url)
    return {
        'scheme': parsed.scheme,
        'host': parsed.netloc,
        'path': parsed.path,
        'query': parsed.query,
        'fragment': parsed.fragment,
        'params': dict(_parse.parse_qsl(parsed.query))
    }
حلل_رابط = تحليل_رابط = parse_url

def build_url(base, path='', params=None):
    """Build URL from components - بناء رابط من مكونات"""
    url = base.rstrip('/') + '/' + path.lstrip('/') if path else base
    if params:
        query = _parse.urlencode(params)
        url = f"{url}?{query}"
    return url
ابن_رابط = بناء_رابط = build_url

def add_params(url, params):
    """Add query parameters to URL - إضافة معاملات للرابط"""
    parsed = _parse.urlparse(url)
    existing = dict(_parse.parse_qsl(parsed.query))
    existing.update(params)
    query = _parse.urlencode(existing)
    return _parse.urlunparse((
        parsed.scheme, parsed.netloc, parsed.path,
        parsed.params, query, parsed.fragment
    ))
أضف_معاملات = إضافة_معاملات = add_params

# ============ Download - التحميل ============

def download(url, path, timeout=60):
    """Download file from URL - تحميل ملف من رابط"""
    try:
        req = _request.Request(url)
        with _request.urlopen(req, timeout=timeout, context=_ssl_context) as response:
            with open(path, 'wb') as f:
                f.write(response.read())
        return True
    except Exception as e:
        return {'error': str(e)}
حمل = تحميل = download

def download_text(url, encoding='utf-8', timeout=30):
    """Download text content - تحميل محتوى نصي"""
    response = get(url, timeout=timeout)
    return response.get('body', '')
حمل_نص = تحميل_نص = download_text

# ============ Headers - الترويسات ============

def create_headers(content_type=None, auth=None, custom=None):
    """Create HTTP headers dict - إنشاء ترويسات HTTP"""
    headers = {}
    if content_type:
        headers['Content-Type'] = content_type
    if auth:
        headers['Authorization'] = auth
    if custom:
        headers.update(custom)
    return headers
أنشئ_ترويسات = إنشاء_ترويسات = create_headers

def bearer_auth(token):
    """Create Bearer auth header - إنشاء ترويسة Bearer"""
    return f"Bearer {token}"
ترويسة_حامل = bearer_auth

def basic_auth(username, password):
    """Create Basic auth header - إنشاء ترويسة Basic"""
    import base64
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
    return f"Basic {credentials}"
ترويسة_أساسية = basic_auth


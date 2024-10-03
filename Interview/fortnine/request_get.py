def get(
    url: str | bytes,
    params: _Params | None = None,
    *,
    data: _Data | None = ...,
    headers: _HeadersMapping | None = ...,
    cookies: RequestsCookieJar | _TextMapping | None = ...,
    files: _Files | None = ...,
    auth: _Auth | None = ...,
    timeout: _Timeout | None = ...,
    allow_redirects: bool = ...,
    proxies: _TextMapping | None = ...,
    hooks: _HooksInput | None = ...,
    stream: bool | None = ...,
    verify: _Verify | None = ...,
    cert: _Cert | None = ...,
    json: Any | None = ...
) -> Response

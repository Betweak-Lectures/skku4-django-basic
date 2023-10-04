from django.http import HttpResponse


def profile(request):
    profile = {
        "이름": "신윤수",
        "별명": "ys",
    }
    result = ""

    for k, v in profile.items():
        result += f"<li>{k}: {v}</li>"

    html = f"""
        <h1>나의 정보</h1>
        <ul>
            {result}
        </ul>
    """

    # print(dir(request))
    request_attrs = dir(request)

    for attr in request_attrs:
        if attr.startswith("_"):
            continue
        print(attr, getattr(request, attr))
        print('-'*10)

    return HttpResponse(html)

import requests

from django.conf import settings

from yesnowtf.conf import StatusCode


def get_answer_info():
    """return information of answer from yes_no_wtf service"""

    response = requests.get(url=settings.YES_NO_URL)

    data = {
        'status': StatusCode.ERROR,
    }

    if response.status_code == 200:
        data['status'] = StatusCode.OK
        data['answer_info'] = response.json()

    return data

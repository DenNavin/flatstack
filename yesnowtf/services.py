from yesnowtf.conf import StatusCode
from yesnowtf.models import Answer
from yesnowtf.utils import get_answer_info


class AnswerService:

    @classmethod
    def create_answer(cls, question):

        answer = None
        answer_yes_no = get_answer_info()

        if answer_yes_no['status'] == StatusCode.OK:
            answer_text = answer_yes_no.get('answer_info', {}).get('answer')

            if answer_text in (Answer.AnswerText.YES, Answer.AnswerText.NO) and question:
                answer = Answer.objects.create(question=question, text=answer_text).display_data()

        return answer


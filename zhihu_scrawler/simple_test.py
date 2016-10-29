from answer import Answer
from question import Question
import unittest

test_answer_url = "https://www.zhihu.com/question/21100397/answer/29424643"
test_question_url = "https://www.zhihu.com/question/50735289"

class TestAnswerClass(unittest.TestCase):
    def setUp(self):
        self.answer_parser = Answer(test_answer_url)
    def test_thumbsup_count(self):
        self.assertEqual(self.answer_parser.get_thumbs_up_count(), 47739)

# test_question_url = "https://www.zhihu.com/question/21100397"
# test_people_url = "https://www.zhihu.com/people/zhang-jia-wei"
# test for answer num

if __name__ == '__main__':
    # answer_parser = Answer(test_answer_url)
    # print answer_parser.get_related_question_title()
    # print answer_parser.get_related_question_url()

    # question_parser = Question(test_question_url)
    # question_parser.get_all_answer_url_list()
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestAnswerClass)
    unittest.main()
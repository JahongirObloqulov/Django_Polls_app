from django.urls import path
from .views import question_list, question_detail, question_vote, question_result

urlpatterns = [
    path("", question_list),
    path("<int:question_id>/detail/", question_detail, name='detail'),
    path("<int:question_id>/vote/", question_vote, name='vote'),
    path("<int:question_id>/result/", question_result, name="result")
]

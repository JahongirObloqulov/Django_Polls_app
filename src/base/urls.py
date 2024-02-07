from django.urls import path
from .views import question_list, question_detail, question_vote

urlpatterns = [
    path("", question_list),
    path("<int:question_id>/detail/", question_detail),
    path("<int:question_id>/vote/", question_vote, name='vote')

]

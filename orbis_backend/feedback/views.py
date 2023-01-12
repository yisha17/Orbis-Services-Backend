from django.shortcuts import render
from .serializer import FeedbackSerializer
from .models import Feedback
from rest_framework import generics

class FeedbackCreateAPIView(generics.CreateAPIView):

    query = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


feedback_create_view = FeedbackCreateAPIView.as_view()


class FeedbackDetailAPIView(generics.RetrieveAPIView):

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    lookup_field = 'pk'


Feedback_detail_view = FeedbackDetailAPIView().as_view()


class FeedbackUpdateAPIView(generics.UpdateAPIView):

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    lookup_field = 'pk'


Feedback_update_view = FeedbackUpdateAPIView.as_view()


class FeedbackDeleteAPIView(generics.DestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    lookup_field = 'pk'

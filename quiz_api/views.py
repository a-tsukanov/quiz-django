from rest_framework.decorators import api_view
from rest_framework.response import Response
from .fields import QuizSerializer
from .models import Quiz


@api_view(['GET'])
def quizes(request):
    quizes = Quiz.objects.all()
    serializer = QuizSerializer(quizes, many=True)
    return Response(serializer.data)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from .fields import QuizSerializer
from .models import Quiz


@api_view(['GET'])
def quizes(request):
    all_quizes = Quiz.objects.all()
    serializer = QuizSerializer(all_quizes, many=True)
    return Response(serializer.data)



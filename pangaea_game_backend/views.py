from rest_framework.decorators import api_view
from rest_framework.response import Response
import time

@api_view(['GET', 'POST'])
def test_view(request):
    if request.method == 'GET':
        return Response({'time': time.time()})

    elif request.method == 'POST':
        value = request.data.get('value', 12)
        res = time.time() - int(value)
        return Response({'new_value': res})
    
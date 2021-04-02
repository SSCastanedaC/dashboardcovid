from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.countries.models import Country

@api_view(['GET'])
def get_countries(request):
    countries = Country.objects.all().values()
    return Response({'countries': countries})
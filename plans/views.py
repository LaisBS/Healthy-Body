from plans.models import Plan
from plans.serializers import PlanSerializer
from rest_framework import generics
from plans.permissions import SuperUserAndAuthenticated
from rest_framework.authentication import TokenAuthentication


class PlanView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperUserAndAuthenticated]

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperUserAndAuthenticated]

    lookup_url_kwarg = "plan_id"

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

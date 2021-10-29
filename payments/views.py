import datetime

import pytz
from django.db import IntegrityError
from rest_framework import viewsets, status, permissions
from .models import Account, Transfer
from .serializers import AccountSerializer, TransferSerializer
from rest_framework.response import Response
import requests
from rest_framework.decorators import action


# Create your views here.


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def post_to_open_account(self, request, *args, **kwargs):
        sandbox_key = 'FLXsdT64DqLYPp13dP2hSHDGSpMjeoMH1635335604'
        my_headers = {'sandbox-key': sandbox_key}
        try:
            api_url = 'https://fsi.ng/api/heritagebank/accounts/AccountOpening/WithBVN'
            serializer = AccountSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                my_request = requests.post(api_url,
                                           data=serializer.validated_data, headers=my_headers)
                response = my_request.json()
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            return Response({"detail": e.message})

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def balance_enquiry(self, request, *args, **kwargs):
        AccountNumber = self.request.query_params.get("AccountNumber")
        sandbox_key = 'FLXsdT64DqLYPp13dP2hSHDGSpMjeoMH1635335604'
        my_headers = {'sandbox-key': sandbox_key}
        try:
            my_request = requests.get(
                f'https://fsi.ng/api/heritagebank/accounts/BalanceInquiry?AccountNumber={AccountNumber}',
                headers=my_headers)
            response = my_request.json()
            return Response(response, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({"detail": str(e.message)})

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def loan_details(self, request, *args, **kwargs):
        AccountNumber = self.request.query_params.get("loanAccount")
        sandbox_key = 'FLXsdT64DqLYPp13dP2hSHDGSpMjeoMH1635335604'
        my_headers = {'sandbox-key': sandbox_key}
        try:
            my_request = requests.get(
                f'https://fsi.ng/api/heritagebank/accounts/MiniStatementInquiry?AccountNumber={AccountNumber}',
                headers=my_headers)
            response = my_request.json()
            return Response(response, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({"detail": str(e.message)})


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def transfer(self, request, *args, **kwargs):
        sandbox_key = 'FLXsdT64DqLYPp13dP2hSHDGSpMjeoMH1635335604'
        my_headers = {'sandbox-key': sandbox_key}
        try:
            serializer = AccountSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                my_request = requests.post('https://fsi.ng/api/heritagebank/transfers/FundsTransfer/Intra',
                                           data=serializer.validated_data, headers=my_headers)
                response = my_request.json()
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            return Response({"detail": e.message})

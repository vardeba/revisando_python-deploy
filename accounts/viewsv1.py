from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404

from .serializers import AccountSerializer
from .models import Account

from utils.base_views import ListBaseView, CreateBaseView


class AccountView(ListBaseView, CreateBaseView):
    def get(self, request: Request) -> Response:
        accounts = Account.objects.all()

        serializer = AccountSerializer(accounts, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request: Request) -> Response:
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED,
        )


class AccountDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        account = get_object_or_404(Account, pk=pk)

        serializer = AccountSerializer(account)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def patch(self, request: Request, pk: int) -> Response:
        account = get_object_or_404(Account, pk=pk)

        serializer = AccountSerializer(account, request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def delete(self, request: Request, pk: int) -> Response:
        account = get_object_or_404(Account, pk=pk)

        account.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )

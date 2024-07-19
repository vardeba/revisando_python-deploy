from rest_framework import permissions
from rest_framework.views import Request, View
from parking_lots.models import ParkingLot


class IsAdminOrParkingLotOwner(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, obj: ParkingLot
    ) -> bool:

        return request.user.is_superuser or request.user == obj.account

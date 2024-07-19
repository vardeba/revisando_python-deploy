from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Account
        fields = [
            "id",
            "shift",
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}}

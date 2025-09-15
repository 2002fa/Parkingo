from rest_framework import serializers


class QRGenerateSerializer(serializers.Serializer):
    reservation_id = serializers.IntegerField()
    user_id = serializers.IntegerField()


class QRVerifySerializer(serializers.Serializer):
    qr_data = serializers.CharField()

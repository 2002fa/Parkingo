from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.utils import timezone
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.http import HttpResponse
from parking.models import Reservation
from .serializers import QRGenerateSerializer, QRVerifySerializer

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def generate_qr(request):
    serializer = QRGenerateSerializer(data=request.data)
    if serializer.is_valid():
        reservation_id = serializer.validated_data['reservation_id']
        
        try:
            reservation = Reservation.objects.get(
                id=reservation_id,
                user=request.user,
                is_active=True
            )
            
            # ایجاد QR code
            qr_data = f"reservation:{reservation.id}:user:{request.user.id}"
            qr = qrcode.make(qr_data)
            
            # ذخیره QR code در مدل reservation
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            reservation.qr_code.save(f'qr_{reservation.id}.png', ContentFile(buffer.getvalue()))
            reservation.save()
            
            return Response({
                'message': 'QR code generated successfully',
                'reservation_id': reservation.id
            })
            
        except Reservation.DoesNotExist:
            return Response(
                {'error': 'Reservation not found or not authorized'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def verify_qr(request):
    serializer = QRVerifySerializer(data=request.data)
    if serializer.is_valid():
        qr_data = serializer.validated_data['qr_data']
        
        try:
            # پارس کردن داده QR
            parts = qr_data.split(':')
            if len(parts) == 4 and parts[0] == 'reservation' and parts[2] == 'user':
                reservation_id = int(parts[1])
                user_id = int(parts[3])
                
                reservation = Reservation.objects.get(
                    id=reservation_id,
                    user__id=user_id,
                    is_active=True
                )
                
                # بررسی زمان رزرو
                now = timezone.now()
                if reservation.start_time <= now <= reservation.end_time:
                    return Response({
                        'valid': True,
                        'message': 'QR code is valid',
                        'reservation': {
                            'id': reservation.id,
                            'spot': reservation.spot.name,
                            'user': reservation.user.username
                        }
                    })
                else:
                    return Response({
                        'valid': False,
                        'message': 'Reservation is not active at this time'
                    })
            
        except (ValueError, Reservation.DoesNotExist):
            return Response({
                'valid': False,
                'message': 'Invalid QR code'
            })
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
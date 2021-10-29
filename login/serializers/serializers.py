from rest_framework import serializers
from Address_update.accounts.models import Users

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["aadhar_num", "ph_number"]
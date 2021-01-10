from rest_framework import serializers
from .models import Role, Polzovateli, Vid, Company, Category, Course, Rabota, Meropriyatia, Zapis, News


class CompanySerializer(serializers.ModelSerializer):
    # name = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Company
        fields = ('id', 'name', 'opisanie', 'fio',
                  'pochta', 'telephon', 'id_role')


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'fio', 'id_role')

from rest_framework import serializers

class CountryInfoSerializer(serializers.Serializer):
    #flag_link = serializers.CharField()
    Capital = serializers.CharField()
    largest_city = serializers.ListField(child=serializers.CharField())
    official_languages = serializers.ListField(child=serializers.CharField())
    area_total = serializers.IntegerField()
    population = serializers.CharField()
    GDP_nominal = serializers.CharField()

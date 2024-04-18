from .models import *
from rest_framework.serializers import ModelSerializer, ValidationError
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class CoordsSerializer(ModelSerializer):
    class Meta:
        model = Coords
        fields = "__all__"


class LevelSerializer(ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class ImagesSerializer(ModelSerializer):
    class Meta:
        model = Images
        exclude = ['rel_pass']


class PassSerializer(WritableNestedModelSerializer, ModelSerializer):
    tourist = UsersSerializer()
    coord = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pass
        exclude = ['add_time', 'status']

    def create(self, validated_data):
        """
        :param validated_data: dict
        :return: models.Pass object

        Method works with POST request,
        spreading data across models, related to Pass model.
        Returns new Pass object.
        """

        tourist = validated_data.pop('tourist')
        coords = validated_data.pop('coord')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        user, created = Users.objects.get_or_create(**tourist)
        coords = Coords.objects.create(**coords)
        level = Level.objects.create(**level)

        new_pass = Pass.objects.create(
            **validated_data,
            tourist=user,
            coord=coords,
            level=level,
        )

        for img in images:
            image = img.pop('image')
            title = img.pop('title')
            Images.objects.create(image=image, title=title, rel_pass=new_pass)

        return new_pass

    def validate(self, data):
        """
        :param data: dict
        :return: models.Pass object

        Method works with POST request,
        spreading data across models, related to Pass model.
        Returns new Pass object.
        """
        print(type(data))
        if self.instance is not None:
            tourist_instance = self.instance.tourist
            tourist_data = data.get('tourist')
            fields_to_validate = [
                tourist_instance.last_name != tourist_data['last_name'],
                tourist_instance.first_name != tourist_data['first_name'],
                tourist_instance.otc != tourist_data['otc'],
                tourist_instance.email != tourist_data['email'],
                tourist_instance.phone != tourist_data['phone']
            ]
            if tourist_data is not None and any(fields_to_validate):
                raise ValidationError("Unable to update user data")
        return data

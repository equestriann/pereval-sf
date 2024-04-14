from .models import *
from rest_framework.serializers import ModelSerializer


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
        fields = "__all__"


class PassSerializer(ModelSerializer):
    tourist = UsersSerializer()
    coord = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pass
        fields = [
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'tourist',
            'coord',
            'level',
            'images',
        ]

    def create(self, validated_data):
        """
        :param validated_data: dict
        :return: models.Pass object

        Method works with POST request from 'Pereval/submitDATA',
        spreading data across models, related to Pass model.
        Returns new Pass object.
        """

        tourist = validated_data.pop('tourist')
        coords = validated_data.pop('coord')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        cur_user = Users.objects.filter(email=tourist['email'])
        if cur_user.exists():
            user_srl = UsersSerializer(data=tourist)
            user_srl.is_valid(raise_exception=True)
            user = user_srl.save()
        else:
            user = Users.objects.create(**tourist)

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
            title = img.title('title')
            Images.objects.create(image=image, title=title, rel_pass=new_pass)

        return new_pass

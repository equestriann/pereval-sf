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
        fields = [
            'image',
            'title',
        ]


class PassSerializer(ModelSerializer):
    tourist = UsersSerializer()
    coord = CoordsSerializer()
    level = LevelSerializer()
    # image = ImagesSerializer()

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
            'image',
        ]

    def create(self, validated_data):
        tourist = validated_data.pop('tourist')
        coords = validated_data.pop('coord')
        level = validated_data.pop('level')
        # image = validated_data.pop('image')

        cur_user = Users.objects.filter(email=tourist['email'])
        if cur_user.exists():
            user_srl = UsersSerializer(data=tourist)
            user_srl.is_valid(raise_exception=True)
            user = user_srl.save()
        else:
            user = Users.objects.create(**tourist)

        coords = Coords.objects.create(**coords)
        level = Level.objects.create(**level)
        print(validated_data)
        new_pass = Pass.objects.create(
            **validated_data,
            tourist=user,
            coord=coords,
            level=level
        )

        # Images.objects.create(
        #     rel_pass=new_pass,
        #     **image,
        # )

        return new_pass


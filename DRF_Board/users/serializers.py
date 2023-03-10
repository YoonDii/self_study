from django.contrib.auth.models import User  #User모델
from django.contrib.auth.password_validation import validate_password #장고 기본 패스워드 검증도구
from django.contrib.auth import authenticate #토근방식으로 유저인증

from rest_framework import serializers
from rest_framework.authtoken.models import Token  #토큰모델
from rest_framework.validators import UniqueValidator #이메일 중복방지 검증도구

#회원가입 시리얼라이즈
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required =True,
        validators = [UniqueValidator(queryset=User.objects.all())],  #이메일 중복검증
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators =[validate_password],
    )

    password2 = serializers.CharField(
        write_only = True,
        required = True,
    )

    class Meta :
        model = User
        fields = ('username','email', 'password', 'password2')
    
    def vaildate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password': "비밀번호가 일치하지 않습니다."}
            )
        return data
    
    #create요청에 대해 create메소드를 오버라이딩, 유저와 토큰 생성.
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required =True, write_only= True)

    def validate(self, data):
        user = authenticate(**data) 
        if user :
            token = Token.objects.get(user=user) #토큰에서 유저찾아 응답
            return token
        raise serializers.ValidationError(
            {"error": "로그인 할 수 없습니다."}
        )
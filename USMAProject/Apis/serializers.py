from USMAApp.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from USMAApp.models import *


# from rest_framework.validators import UniqueValidator
# from rest_framework_jwt.settings import api_settings

# kwa ajili ya kumregister mtu bila kutumia token
class UserCreationSerializer(serializers.ModelSerializer):
	username=serializers.CharField(max_length=25)
	email=serializers.EmailField(max_length=50)
	password=serializers.CharField(max_length=50)


	class Meta:
		model= MyUser
		fields= ['username','email','password']
		#fields='__all__'

	def validate(self,attrs):
		username_exists = MyUser.objects.filter(username=attrs['username']).exists()
		if username_exists:
			raise serializers.ValidationError(detail="User with username already exists")


		email_exists = MyUser.objects.filter(email=attrs['email']).exists()
		if email_exists:
			raise serializers.ValidationError(detail="User with email already exists")

		return super().validate(attrs)


		

class UniversitiesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Universities
		fields = '__all__'


class UniversityCoursesSerializer(serializers.ModelSerializer):

	# hizi ni manytomany field  so badala ya kudisplay number
	# basi idisplay hilo jina la category ndo tunafanya hivi

	#university = UniversitiesSerializer(many=True)

	class Meta:
		model = UniversityCourses
		fields = '__all__'
		# fields = [
		# 'university',
		# 'CourseName',
		# 'CourseImage',
		# 'CourseDepartment',
		# 'CourseCapacity',

		# ]

class AllProjectsSerializer(serializers.ModelSerializer):
	# hizi ni foreign key so badala ya kudisplay number
	# basi idisplay hilo jina la category ndo tunafanya hivi

	#university = UniversitiesSerializer(many=False)
	#CourseName = UniversityCoursesSerializer(many=False)

	class Meta:
		model = AllProjects
		fields = '__all__'








class ArticlesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Articles
		fields = '__all__'


class ArticlesCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = ArticlesCategory
		fields = '__all__'


#----------------------HOB------------------------

class HobSerializer(serializers.ModelSerializer):

	class Meta:
		model = Hob
		fields = '__all__'


class ExpertsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Experts
		fields = '__all__'




#-----------------USER SERIALIZERS------------

# class UserSerializer(serializers.ModelSerializer):
# 	token = serializers.SerializerMethodField()
# 	email = serializers.EmailField(
# 		required=True,
# 		validators=[UniqueValidator(queryset=MyUser.objects.all())]
# 		)

# 	username = serializers.CharField(
# 		required=True,
# 		max_length=100,
# 		validators=[UniqueValidator(queryset=MyUser.objects.all())]
# 		)

# 	password = serializers.CharField(
# 		required=True,
# 		min_length=4,
# 		write_only=True
		
# 		)
# 	confirm_password = serializers.CharField(
# 		required=True,
# 		min_length=4,
# 		write_only=True
		
# 		)


# 	def create(self, validated_data):
# 		password = validated_data.pop('password', None)
# 		instance = self.Meta.model(**validated_data)
# 		if password is not None:
# 			instance.set_password(password)
# 		instance.save()
# 		return instance


# 	def get_token(self, obj):
# 		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# 		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
# 		payload = jwt_payload_handler(obj)
# 		token = jwt_encode_handler(payload)
# 		return token

# 	class Meta:
# 		model =MyUser
# 		fields = [
# 		'token', 
# 		'email',
# 		'username', 
# 		'password',
# 		'confirm_password'
# 		]
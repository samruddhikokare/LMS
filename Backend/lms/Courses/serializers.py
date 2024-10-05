from rest_framework import serializers
from .models import User  # Assuming your user model is in models.py
from courses.models import Course  # Assuming your course model is in the courses app


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone', 'is_active']
        read_only_fields = ['id']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'video_url', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class EnrollmentSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    course_id = serializers.IntegerField()

    def create(self, validated_data):
        user_id = validated_data['user_id']
        course_id = validated_data['course_id']
        # Create the enrollment logic here
        # This could involve creating a record in an Enrollment model (which you would need to create)
        pass

    def validate(self, attrs):
        # Add any validation logic here, e.g. checking if the user or course exists
        return attrs

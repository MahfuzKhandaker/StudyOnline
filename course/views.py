from django.shortcuts import render

from .models import Category, Course, Lesson, Comment
from .serializers import CourseSerializer
from .serializers import CourseListSerializer
from .serializers import LessonListSerializer
from .serializers import CommentSerializer
from .serializers import CategorySerializer
from .serializers import QuizSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['GET'])
def get_quiz(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    quiz = lesson.quizzes.first()
    serializer = QuizSerializer(quiz)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_frontpage_courses(request):
    courses = Course.objects.all()[0:4]
    serializer = CourseListSerializer(courses, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_courses(request):
    category_id = request.GET.get('category_id', '')
    courses = Course.objects.all()

    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])
        
    serializer = CourseListSerializer(courses, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_course(reqest, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseSerializer(course)
    lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)
    

    return Response({
        'course':course_serializer.data,
        'lessons':lesson_serializer.data
    })

@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    serializer = CommentSerializer(lesson.comments.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    data = request.data

    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)

    comment = Comment.objects.create(
        course=course,
        lesson=lesson,
        name=data.get('name'),
        content=data.get('content'),
        created_by=request.user
    )
    comment.save()

    serializer = CommentSerializer(comment)

    return Response(serializer.data)
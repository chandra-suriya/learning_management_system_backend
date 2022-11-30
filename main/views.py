from rest_framework import permissions, response, views, status

from main import models, serialisers

# Create your views here.


class TeacherList(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        teacher = models.Teacher.objects.all()
        teac_ser = serialisers.TeacherSerializer(teacher, many=True)
        return response.Response(teac_ser.data)


class TeacherRegister(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        full_name = data.get("full_name")
        email = data.get("email")
        password = data.get("password")
        qualification = data.get("qualification")
        mobile_no = data.get("mobile_no")
        skills = data.get("skills")

        if(not full_name and not email and not password and not qualification
           and not mobile_no and not skills):
            return response.Response({
                 "status": "Something is not filled"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            models.Teacher.objects.create(full_name=full_name, email=email,
                                          password=password,
                                          qualification=qualification,
                                          mobile_no=mobile_no,
                                          skills=skills)
            return response.Response({
                "status": "Teacher register is sucessfull"
            }, status=status.HTTP_200_OK)


class TeacherLogin(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        email = data.get("email")
        password = data.get("password")

        if(not email and not password):
            return response.Response({
                 "messages": "please enter all the fields"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            if(models.Teacher.objects.filter(email=email,
                                             password=password).exists()):
                return response.Response({
                        "status": "Teacher login is sucessfull",
                        "success": True
                    }, status=status.HTTP_200_OK)
            else:
                return response.Response({
                    "datas": {
                        "email": email,
                        "password": password
                    },
                    "status": "Invalid Username or password",
                    "success": False
                }, status=status.HTTP_200_OK)

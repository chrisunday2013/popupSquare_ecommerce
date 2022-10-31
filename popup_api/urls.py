# The run should be done at command line or terminal while server is still running from vscode 
# run this to get token ( http post http://127.0.0.1:8000/api/token/ username=ucccllassic password=jamblock )

# After running the above, pick the access token and add to the below and run to get access. 
#  http http://127.0.0.1:8000/api/vendors/ "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MjEyMDM1LCJpYXQiOjE2NjcyMTE3MzUsImp0aSI6IjA0NTQ5OWEyY2FlMDRmODNiNjUzYzAwMDM0Y2M1YWNjIiwidXNlcl9pZCI6MX0.Gn0vx7qOF433X4zO2BQKVSa_yNwKpm4D1uk1pqeBj4U"


#  run the below to get a new or refresh token
#  http http://127.0.0.1:8000/api/token/refresh/ refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MjEyMDM1LCJpYXQiOjE2NjcyMTE3MzUsImp0aSI6IjA0NTQ5OWEyY2FlMDRmODNiNjUzYzAwMDM0Y2M1YWNjIiwidXNlcl9pZCI6MX0.Gn0vx7qOF433X4zO2BQKVSa_yNwKpm4D1uk1pqeBj4U"



from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
]

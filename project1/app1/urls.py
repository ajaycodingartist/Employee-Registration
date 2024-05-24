from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about/', views.about),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('userreg/', views.userreg, name="userreg"),
    path('userregistrationconfirmation/', views.userregistrationconfirmation, name="userregistrationconfirmation"),
    path('userregedit',views.userregedit,name='userregedit'),
    path('updateuser/<int:id>',views.updateuser,name='updateuser'),
    path('updateuser/useredt/<int:id>',views.useredt,name='useredt'),
    path('userselfdelete/<int:id>',views.userselfdelete,name='userselfdelete'),
    path('workerreg/', views.workerreg, name="workerreg"),
    path('workerregistrationconfirmation/', views.workerregistrationconfirmation, name="workerregistrationconfirmation"),
    path('workerregedit',views.workerregedit,name='workerregedit'),
    path('updateworker/<int:id>',views.updateworker,name='updateworker'),
    path('updateworker/workeredt/<int:id>',views.workeredt,name='workeredt'),
    path('workerselfdelete/<int:id>',views.workerselfdelete,name='workerselfdelete'),
    path('workerslist/', views.workerslist, name="workersview"),
    path('workersprofile/', views.workersprofile, name="workersprofile"),
    path('employerprofile/', views.employerprofile, name="employerprofile"),
    path('occupationrequests',views.occupationrequests, name="occupationrequests"),
    path('occupationrequest/<int:id>',views.occupationrequest, name="occupationrequest"),
    path('occupationrequest/occupationreq/<int:id>',views.occupationreq, name="occupationreq"),
    path('jobrequestconfirmation/', views.jobrequestconfirmation, name="jobrequestconfirmation"),
    path('occupationreqview/',views.occupationreqview, name="occupationreqview"),
    path('occupationreqemployerview/',views.occupationreqemployerview, name="occupationreqemployerview"),
    path('deleterequest/<int:id>',views.deleterequest,name='deleterequest'),
    path('workeracknowledgements',views.workeracknowledgements, name="workeracknowledgements"),
    path('workeracknowledgement/<int:id>',views.workeracknowledgement, name="workeracknowledgement"),
    path('workeracknowledgement/workeracknowledgementsave/<int:id>',views.workeracknowledgementsave, name="workeracknowledgementsave"),
    path('useracknowledgementview/',views.useracknowledgementview, name="useracknowledgementview"), #1st option payment
    path('paying/',views.paying, name="paying"), #optional
    path('paymentsuccess/',views.paymentsuccess, name="paymentsuccess"),
    path('paymentsuccesstwo/',views.paymentsuccesstwo, name="paymentsuccesstwo"), #optional
    
    # path('occupationsecondrequest',views.occupationsecondrequest, name="occupationsecondrequest"),

]   
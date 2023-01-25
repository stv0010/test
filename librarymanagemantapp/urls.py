from django.urls import path

from librarymanagemantapp import views

urlpatterns=[
    path('',views.log_fun,name='log'),
    path('adminsignup',views.adminsign_fun,name='adminsignup'),
    path('studsignup',views.studentsign_fun,name='studsignup'),
    path("checkdata",views.checklog_fun),

    path('adminreg',views.adminreg_fun),
    path('studentreg',views.studentreg_fun),

    path('adminhome',views.admminhome_fun,name='adhome'),
    path('addbook',views.addbook_fun,name='addbook'),
    path('readbookdata',views.readbookdata_fun),
    path('displaybook',views.displaybook_fun,name='displaybook'),
    path('deletebook/<int:id>',views.updatebook_fun,name='updatebook'),
    path('updatebook/<int:id>',views.deletebook_fun,name='deletebook'),
    path('assignbook',views.assignbook_fun,name='assignbook'),
    path('readissuedbook',views.readissuedbook_fun),
    path('issuedbookdis',views.issuedbookdis_fun,name='issuedbookdis'),
    path('issdbkupdate/<int:id>',views.issdbkupdate_fun,name='issdbkupdate'),
    path('issdbkdelete/<int:id>',views.issdbkdelete_fun,name='issdbkdelete'),
    path('logoutad',views.logoutad_fun,name='logoutad'),

    path('studenthome',views.studenthome_fun,name='sthome'),
    path('stissdbkdetls',views.stissdbkdet_fun,name='stissdbkdet'),
    path('logoutst',views.logoutst_fun,name='logoutst'),
]
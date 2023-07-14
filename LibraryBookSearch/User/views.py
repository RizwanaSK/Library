from django.shortcuts import render
import pymysql


# Create your views here.
def index(request):
  return render(request,'User/index.html')

def userlogin(request):
  return render(request,'User/Users.html')
def register(request):
  return render(request,'User/Register.html')
def userhome(request):
  return render(request,'User/UserHome.html')
def RegAction(request):
  name=request.POST['name']
  email=request.POST['email']
  mobile=request.POST['mobile']
  address=request.POST['address']
  username=request.POST['username']
  password=request.POST['password']

  con=pymysql.connect(host="localhost",user="root",password="root",database="lsb")
  cur=con.cursor()
  i=cur.execute("insert into user values(null,'"+name+"','"+email+"','"+mobile+"','"+address+"','"+username+"','"+password+"')")
  con.commit()
  con.close()
  cur.close()
  if i>0:
    context={'data':'Registration Successful...!!'}
    return render(request,'User/Register.html',context)
  else:
    context={'data','Registration Failed...!!'}
    return render(request,'User/Register.html',context)
def LogAction(request):
  username=request.POST.get('username')
  password=request.POST.get('password')
  con=pymysql.connect(host="localhost",user="root",password="root",database="lsb")
  cur=con.cursor()
  cur.execute("select *  from user where username='"+username+"'and password='"+password+"'")
  data=cur.fetchone()
  if data is not None:
    request.session['user']=username
    request.session['userid']=data[0]
    return render(request,'User/UserHome.html')
  else:
    context={'data':'Login Failed ....!!'}
    return render(request,'User/Users.html',context)

  
def Profile(request):
  uid=str(request.session['userid'])
  con=pymysql.connect(host="localhost",user="root",password="root",database="lsb")
  cur=con.cursor()
  cur.execute("select * from user where id='"+uid+"'")
  data=cur.fetchall()
  strdata="<table border='1'><tr><th>Name</th><th>Email</th><th>Mobile</th><th>Address</th></tr>"
  for i in data:
    strdata+="<tr><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td>"+str(i[4])+"</td></tr>"
  context={'data':strdata}
  return render(request,'User/ViewProfile.html',context)
def SearchByTitle(request):
  return render(request,'User/SearchByTitle.html')
def SearchTitleAction(request):
  title=request.POST.get('title')
  con=pymysql.connect(host="localhost",user="root",password="root",database="lsb")
  cur=con.cursor()
  cur.execute("select * from books where bookname like'%"+title+"%'")
  data=cur.fetchall()
  strdata="<table border='1'><tr style='color:red;background:skyblue;height:60px;text-align:center;'><th>Book Name</th><th>Author</th><th>Publication Here</th><th>Book Genre</th><th>Description</th></tr>"
  for i in data:
    strdata+="<tr><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td>"+str(i[5])+"</td></tr>"
  context={'data':strdata}
  return render(request,'User/ViewSearchTAction.html',context)
def SearchByAuthor(request):
  return render(request,'User/SearchByAuthor.html')
def SearchAuthorAction(request):
  title=request.POST.get('author')
  con=pymysql.connect(host="localhost",user="root",password="root",database="lsb")
  cur=con.cursor()
  cur.execute("select * from books where author like'%"+title+"%'")
  data=cur.fetchall()
  strdata="<table border='1'><tr style='color:red;background:skyblue;height:60px;text-align:center;'><th>Book Name</th><th>Author</th><th>Publication Here</th><th>Book Genre</th><th>Description</th></tr>"
  for i in data:
    strdata+="<tr><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td>"+str(i[5])+"</td></tr>"
  context={'data':strdata}
  return render(request,'User/ViewSearchTAction.html',context)
def SearchByYear(request):
  return render(request,'User/SearchByYear.html')
def SearchYearAction(request):
  title=request.POST.get('year')
  con=pymysql.connect(host="localhost",user="root",password="root",database="lsb")
  cur=con.cursor()
  cur.execute("select * from books where pyear like'%"+title+"%'")
  data=cur.fetchall()
  strdata="<table border='1'><tr style='color:red;background:skyblue;height:60px;text-align:center;'><th>Book Name</th><th>Author</th><th>Publication Here</th><th>Book Genre</th><th>Description</th></tr>"
  for i in data:
    strdata+="<tr><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td>"+str(i[5])+"</td></tr>"
  context={'data':strdata}
  return render(request,'User/ViewSearchTAction.html',context)
  


from django.shortcuts import render
import pymysql
# Create your views here
def adminlogin(request):
    return render(request,'adminapp/Login.html')
def adminhome(request):
    return render(request,'adminapp/AdminHome.html')
def LogAction(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
   
    if username=='Admin' and password=='Admin':      
        return render(request,'adminapp/AdminHome.html')
    else:
        context={'data':'Login Failed ....!!'}
        return render(request,'adminapp/Login.html',context)
def AddBooks(request):
    return render(request,'adminapp/AddBooks.html')
def AddBookAction(request):
    bookname=request.POST['bookname']
    author=request.POST['author']
    pyear=request.POST['pyear']
    genre=request.POST['genre']
    description=request.POST['description']

    con=pymysql.connect(host="localhost",user="root",password="root",database="lsb")
    cur=con.cursor()
    cur.execute("select * from books where bookname='"+bookname+"'")
    dd=cur.fetchone()
    if dd is not None:
      context={'data':'Book Already Exist...!!'}
      return render(request,'adminapp/AddBooks.html',context)
    else:
      cur1=con.cursor()
      i=cur1.execute("insert into books values(null,'"+bookname+"','"+author+"','"+pyear+"','"+genre+"','"+description+"')")
      con.commit()
      if i>0:
        context={'data':'Book Added Successfully...!!'}
        return render(request,'adminapp/AddBooks.html',context)
      else:
        context={'data':'Failed To Add Book...!!'}
        return render(request,'adminapp/AddBooks.html',context)
def ViewBooks(request):
    con=pymysql.connect(host="localhost",user="root",password="root",database="lsb")
    cur=con.cursor()
    cur.execute("select * from books")
    data=cur.fetchall()
    strdata="<table border='1'><tr style='color:red;background:skyblue;height:60px;text-align:center;'><th>Book Name</th><th>Author</th><th>Publication Here</th><th>Book Genre</th><th>Description</th></tr>"
    for i in data:
     strdata+="<tr><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td>"+str(i[5])+"</td></tr>"
    context={'data':strdata}
    return render(request,'adminapp/ViewBooks.html',context)








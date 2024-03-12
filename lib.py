import mysql.connector
conn = mysql.connector.connect( 
        host='localhost', 
        user='root',  
        password = "2024", 
        db='library'
        )
def addbook():
    bn=input("enter book name:")
    c=input("enter book number:")
    t=input("total books:")
    s=input("enter subject:")
    data=(bn,c,t,s)
    sql='insert into books values(%s,%s,%s,%s)'
    c= conn.cursor() 
    c.execute(sql,data)
    conn.commit()
    print("data entered succesfully")
    main()
    
def issueb():
    n=input("enter name:")
    r=input("enter register number:")
    co=input("enter book code:")
    d=input("enter date:") 
    data=(n,r,co,d)
    a='insert into isue values(%s,%s,%s,%s)'
    c= conn.cursor() 
    c.execute(a,data)
    conn.commit()
    print("book issued to:",n)
    bookup(co,-1)

def submitb():
    n=input("enter name:")
    r=input("enter register number:")
    co=input("enter book code:")
    d=input("enter date:") 
    a='insert into submitted values(%s,%s,%s,%s)'
    data=(n,r,co,d)
    c= conn.cursor() 
    c.execute(a,data)
    conn.commit()
    print("book submitted from:",n)
    bookup(co,1)
    
def bookup(co,u):
    a="select TOTAL from books where BCODE=%s"
    data=(co,)
    c=conn.cursor
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql="update books set TOTAL=%s where BCODE=%s"
    d=(t,co)
    c.execute(sql,d)
    conn.commit()
    main()

def dbook():
    ac=input("enter book code:")
    a="delete from books where BCODE=%S"
    data=(ac,)
    c=conn.cursor()
    c.execute(a,data)
    conn.commit()
    main()
def dispbook():
    a="select *from books"
    c=conn.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Book Name:",i[0])
        print("Book Code:",i[1])
        print("total:",i[2])
        print("subject:",i[3])
    main()
def main():
    print("""

                                Library Manager


   1.ADD BOOK
   2.ISSUE BOOK
   3.SUBMIT BOOK
   4.DELETE BOOK
   5.DISPLAY BOOKS""")
    choice=input("enter your choice:")
    if(choice=='1'):
        addbook()
    elif(choice=='2'):
        issueb()
    elif(choice=='3'):
        submitb()
    elif(choice=='4'):
        dbook()
    elif(choice=='5'):
        dispbook()
    else:
        print("inavalid choice")
        main()
def pswd():
    ps=input("enter password:")
    if ps=="priya":
        main()
    else:
        print("incorrect password")
        pswd()
pswd()

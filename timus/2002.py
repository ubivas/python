N = int(raw_input())
Logins = {}
Logged = []
for i in range (0,N):
    s =  raw_input().split(' ')
    operation   = s[0]
    user        = s[1]
    if operation == "register":
        password    = s[2]
        if user in Logins:
            print( "fail: user already exists" )
        else:
            Logins[user] = password
            print( "success: new user added" )
    elif operation == "login":
        password    = s[2]
        if user not in Logins:
            print( "fail: no such user" )
        else:
            if Logins[user] != password:
                print( "fail: incorrect password" )
            else:
                if user in Logged:
                    print( "fail: already logged in" )
                else:
                    Logged.append(user)
                    print( "success: user logged in" )
    elif operation == "logout":
        if user not in Logins:
            print( "fail: no such user" )
        else:
            if user not in Logged:
                print( "fail: already logged out" )
            else:
                Logged.remove(user)
                print( "success: user logged out" )

    else:
        pass

def file_get_contents(filename):
    with open(filename) as f:
        return f.read()


list_user = file_get_contents("list_member.txt").splitlines()


real_names = file_get_contents("whitelist.txt").splitlines()
cnt = 0
for x in list_user:
    res = [ele for ele in real_names if(ele in x.lower())]

    if str(bool(res)) == "False":

        print(x)
        cnt = cnt + 1
        
    
print("----------------------------------------")
print("Possibly Fakename => %s Account(s)"%(cnt))

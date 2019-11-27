import zhihuapi as api

with open('cookie') as f:
    api.cookie(f.read())


u = api.user("aqdshg")

print(u.profile())
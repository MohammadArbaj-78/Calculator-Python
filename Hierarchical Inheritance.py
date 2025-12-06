
# Hierarchical inheritance

class company:
    company='class company'

class ceo(company):
    ceo='class ceo'

class manager(ceo):
    manager='class manager'

class team1_leader(manager):
    team1='class team1'

class team2_leader(manager):
    team2='class team2'

class employee1(team1_leader):
    employee1_team1='class employee1'

class employee2(team1_leader):
    employee2_team1='class employee2'

class employee3(team1_leader):
    employee3_team1='class employee3'

class employee1(team2_leader):
    employee1_team2='class employee1'

class employee2(team2_leader):
    employee2_team2='class employee2'

class employee3(team2_leader):
    employee3_team2='class employee3'


o_company=company()
o_employee1=employee1()

# print(o_company.company)
print(o_employee1.manager)
print(o_employee1.ceo)
print(o_employee1.company)
# print(o_company.employee1)
# print(o_company.manager)
# print(o_company.ceo)



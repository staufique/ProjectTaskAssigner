import openpyxl
from Tickets.models import State

def parser(file):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2,values_only=True):
        print(row)
        states,state_code=row
        update=State(state_name=states,state_code=state_code,updated_date=None)
        update.save()
        return "Updated"
    return 'Something wen wrong'
# parser('C:\\Users\\Maqsood\\Desktop\\Django_Todo\\Project_Minute\\Tickets\\states.xlsx')
data = open("states.xlxs","r")
print(data)
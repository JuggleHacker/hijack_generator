from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import programming

def siteswap_in_list(list_of_siteswaps, siteswap):
    """ Takes a list of siteswaps, and a siteswap we are searching for.
    Returns the index if the siteswap is in the list, None otherwise.
    Note, if searching for 744 we have found it if 447 is in the list."""
    for i in range(len(siteswap)):
        if siteswap in list_of_siteswaps:
            return list_of_siteswaps.index(siteswap)
        else:
            siteswap = siteswap[1:] + siteswap[:1]
    return None

wb = Workbook()
ws1 = wb.active
ws1.title = "Transitions"
dest_filename = "Why_not_loop.xlsx"
patterns_written = 0
patterns = [[7,8,6,2,7,7,8,6,2,7]] # keep track of all patterns found
new_patterns = [[7,8,6,2,7,7,8,6,2,7]] # keep track of patterns found on latest loop
keep_looping = True
while keep_looping:
    newer_patterns = []
    for pattern in new_patterns:
        hijack = programming.generate_hijacks(pattern, [2,6,7,8])
        if pattern[:5] != pattern[5:]:
            hijack +=  programming.generate_hijacks(pattern[1:]+pattern[:1], [2,6,7,8])
        for transition in hijack:
            if transition == None:
                continue
            index_of_pattern = siteswap_in_list(patterns, transition[1]) # None if not there
            if index_of_pattern == None:
                newer_patterns.append(transition[1])
                patterns.append(transition[1])

            current_value = ws1.cell(column=siteswap_in_list(patterns,transition[1])+2, row=siteswap_in_list(patterns,transition[0])+2).value
            patterns_written += 1
            if current_value != None:
                _ = ws1.cell(column=siteswap_in_list(patterns,transition[1])+2, row=siteswap_in_list(patterns,transition[0])+2, value="{0}".format(current_value + '\nor\n' + transition[2]))
            else:
                _ = ws1.cell(column=siteswap_in_list(patterns,transition[1])+2, row=siteswap_in_list(patterns,transition[0])+2, value="{0}".format(transition[2]))
    if newer_patterns == []:
        keep_looping = False
    else:
        new_patterns = newer_patterns

if len(patterns) != 1:

    for index, pattern in enumerate(patterns):
        _ = ws1.cell(column=siteswap_in_list(patterns,pattern)+2, row=1, value="{0}".format(str(pattern)+'\n'+str(pattern[0::2])+' vs '+str(pattern[1::2])))
        _ = ws1.cell(column=1, row=siteswap_in_list(patterns,pattern)+2, value="{0}".format(str(pattern)+'\n'+str(pattern[0::2])+' vs '+str(pattern[1::2])))


    adjacency_matrix_sheet = wb.create_sheet(title="Adjacency matrix")
    for i in range(2,len(patterns)+2):
        for j in range(2,len(patterns)+2):
            _ = adjacency_matrix_sheet.cell(column=i,row=j, value = '=IF(Transitions!{}="",0,1)'.format(get_column_letter(i)+str(j)))
    wb.save(filename = dest_filename)
    print("{} patterns written".format(patterns_written))
else:
    print('No transitions found')
    #Workbook.close()
# wb = Workbook()
#
# dest_filename = 'first_attempt.xlsx'
#
# ws1 = wb.active
# ws1.title = "Testing"
#
#
# for transition in programming.generate_hijacks([7,8,6,2,7], [2,6,7,8]):
#     ws1.append([transition[2]])
#
# wb.save(filename = dest_filename)


#
# for row in range(1, 40):
#     ws1.append(range(600))
#
# ws2 = wb.create_sheet(title="Pi")
# ws2['F5'] = 3.14
#
# ws3 = wb.create_sheet(title="Data")
# for row in range(10, 20):
#     for col in range(27, 54):
#         _ = ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
# print(ws3['AA10'].value)
#

import sys
import os

gjf_name = os.path.splitext(os.path.basename(sys.argv[1]))[0]
stream_gjf = open(sys.argv[1],'r')
list_content_gjf = list(stream_gjf)
stream_gjf.close()

null_counter = 0
coord_line = 0
line_split = []

for i in range(0,len(list_content_gjf)):
    if null_counter != 2:
        if list_content_gjf[i] == '\n':
            null_counter = null_counter + 1
    elif null_counter == 2: 
        null_counter = 0
        coord_line = i
    else:
        os.exit()

for j in range(coord_line,len(list_content_gjf)):
    if(list_content_gjf[j] != '\n'):
        line_split.append(list_content_gjf[j].split())

orca_file = open(gjf_name + '.inp','w')
orca_file.write('* xyz   ' + line_split[0][0] + "   " + line_split[0][1]  +'\n')

for i in range(1, len(line_split)):
    orca_file.write(line_split[i][0])
    for j in range(1, len(line_split[i])):
        if float(line_split[i][j]) < 0:
            orca_file.write("    " + line_split[i][j])
        else:
            orca_file.write("     " + line_split[i][j])
    orca_file.write('\n')
orca_file.write(' *\n')
        
#orca_file.write(line_split[i][0] + "     " + line_split[i][1] + "   " + line_split[i][2] + "   " + line_split[i][3] + '\n')
orca_file.close()

os.exit()

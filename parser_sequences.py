with open("aminoacids_example.txt") as f1,open("nucletotides_example.txt") as f2:
    list=[]
    for a,b in zip(f1,f2):
        out ='\t'.join([a.strip(),b.strip()])
        list.append(out)

with open("output_parser.txt", 'w') as wf:
    for line in list:
        wf.writelines(f"[CLS]{line}[SEP]"+ '\n')
print('The End!!')
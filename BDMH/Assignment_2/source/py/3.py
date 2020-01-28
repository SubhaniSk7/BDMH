import sys, os

input_file = sys.argv[1]
ch = input("1. abcpred\n2. ctlpred\n3. propred\n4. toxinpred\nSelect: ")
if(ch=='1'):
    os.system("perl abcpred/abcpred.pl -i "+ input_file + " -o out.abcpred")
elif(ch =='2'):
    os.system("perl ctlpred/ctlpred.pl -i "+ input_file + " -o out.ctlpred")
elif(ch=='3'):
    os.system("perl propred/propred.pl -i "+ input_file + " -o out.propred")
elif(ch=='4'):
    os.system("perl toxinpred/toxinpred.pl -i "+ input_file + " -o out.toxinpred")
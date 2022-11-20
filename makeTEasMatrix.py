import os
import argparse

def run(args_dict):
    input_file = args_dict['input']
    output_file = args_dict['input_dir']

    ifile = open("gene_names")
    gene_name=[]
    for line in ifile:
        gene_name.append(line.replace("\n","").replace("\r",""))
    ifile.close()

    TEmatrix=[]
    for i in range(len(gene_name)):
        TEmatrixTemp=[]
        for j in range(len(gene_name)):
            TEmatrixTemp.append(0)
        TEmatrix.append(TEmatrixTemp)

    ifile = open(input_file)
    for line in ifile:
        temp=line.replace("\n","").replace("\r","").split(",")
        TEmatrix[int(temp[0])-1][int(temp[1])-1]=float(temp[2])
        if len(temp)>3:
            TEmatrix[int(temp[1])-1][int(temp[0])-1]=float(temp[3])

    ofile = open(output_file,"w")
    ofile.write("TE")
    for i in range(len(gene_name)):
        ofile.write("\t"+gene_name[i])
    for i in range(len(gene_name)):
        ofile.write("\n"+gene_name[i])
        for j in range(len(gene_name)):
            ofile.write("\t"+str(TEmatrix[i][j]))
    ofile.close()

if __name__ == '__main__':  
    progpath = os.path.dirname(os.path.realpath(__file__))
    
    parser = argparse.ArgumentParser()    
    parser.add_argument('-i','--input', type=str, default="TE_result_all.csv",
            help='input TENET result file')
    parser.add_argument('-o','--output', type=str, default="TE_result_matrix.txt",
            help='output matrix file')
    args = parser.parse_args()
    args_dict = vars(args)
       
    run(args_dict)
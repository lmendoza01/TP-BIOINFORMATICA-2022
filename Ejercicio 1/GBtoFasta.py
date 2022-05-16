from Bio import SeqIO
import sys
import os
from translate6frames import translate6frames as TF
from txtToFasta import ConverterTxtFasta

def helpMenu():
    print("Uso: ")
    print("\t",sys.argv[0],"input_gb_file","output_fasta_file",sep=" ")

def validateArgs():
    if len(sys.argv) < 3:
        helpMenu()
        exit()
    
def main():
    
    validateArgs()

    input_gb = sys.argv[1]
    output_fasta = sys.argv[2]


    try:
        countRecords = SeqIO.convert(input_gb, "gb", output_fasta, "fasta")
    except:
        print("Valores invalidos para los archivos de input y output fueron recibidos")
        os.remove(output_fasta)
        helpMenu()
        exit()
    
    print("Se convirtieron {0} registros de GenBank a Fasta".format(countRecords))


    p = TF.translate6frames(output_fasta, 'DNA')

    p.Output()

    ConverterTxtFasta.convert()

main()
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

import sys
import os

def translate_record(record):
    """Returns a new SeqRecord with translated sequence."""
    return SeqRecord(seq=record.seq.translate(), id=record.id + "_translated", description=record.description)


def padSequence(sequence):
    remainder = len(sequence) % 3
    return sequence if remainder == 0 else sequence + Seq('N' * (3 - remainder))

def main():

    input_gb = sys.argv[1]
    output_fasta = sys.argv[2]

    try:
        # countRecords = SeqIO.convert(input_gb, "genbank", output_fasta, "fasta")
        records = SeqIO.parse(input_gb, 'gb')
        proteins = []

        for rec in records:
            proteins.append(translate_record(padSequence(rec)))

        SeqIO.write(proteins, open(output_fasta, 'w'), 'fasta')
    except:
        print("Valores invalidos para los archivos de input y output fueron recibidos")
        os.remove(output_fasta)
        exit()

main()
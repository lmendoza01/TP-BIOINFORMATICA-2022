from textwrap import wrap

class ConverterTxtFasta:

        @classmethod
        def convert(self):
            with open('proteins.fas','w') as proteins:

                for x in range(1,4):

                        with open('out2.fastaFrame'+str(x)+'Direct.txt') as fasta1:

                            lines = fasta1.readlines()

                            for index in range(0,len(lines)):

                                line = lines[index]

                                if index == 0:
                                    line = line.replace(line[:12],line[:10]+'-'+str(x-1)+'F')
                                    proteins.write(line)
                                else:
                                    sequenceDivisons = wrap(line,60)
                                    for sequence in sequenceDivisons:
                                        proteins.write(sequence.replace('_','*')+'\n')


                for y in range(1, 4):

                    with open('out2.fastaFrame' + str(y) + 'Direct.txt') as fasta2:

                        lines = fasta2.readlines()

                        for index in range(0,len(lines)):

                            line = lines[index]

                            if index == 0:
                                line = line.replace(line[:12], line[:10] + '-' + str(y - 1) + 'R')
                                proteins.write(line)
                            else:
                                sequenceDivisons = wrap(line, 60)
                                for sequence in sequenceDivisons:
                                    proteins.write(sequence.replace('_','*')+'\n')
                proteins.close()
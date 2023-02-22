# FindTelo

It is a python script to get, from the start and from the finish of a read / sequence with X number of nucleotides. This is the first step to use MEME software to find a telomeric sequeces, as exemple, but there are a number of uses for this script.

## Use

For basic use of this script you need to have Python installed in you device and run the following command:

```
python FindTelo.py -i exemple.fasta
```
This entrance will create a FindTelo_out.fasta file contening the first and last 50 nucleotides of each read / sequence from your original file. You can change the name and the type of the final file, as well the number of nucleotides collected. To do this you only need to add the **-n** XX, for the number of nucleotides and **-o** any_thing.type, for the name and format of the final file.

### Observation

The in and out file types supported are listed here https://biopython.org/wiki/SeqIO , at the Biopython library documentation.

## Contact me

Questions, suggestions, comments, etc? Just send a e-mail to pedromsouza0@gmail.com or souza.pedro@ecologia.ufjf.br

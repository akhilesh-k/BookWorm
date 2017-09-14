#Import library essentials
from sumy.parsers.plaintext import PlaintextParser 
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer 

file ="b.txt" #name of the plain-text file
parser = PlaintextParser.from_file(file, Tokenizer("english"))
summarizer = LexRankSummarizer()

summary = summarizer(parser.document, 5) #Summarize the document with 5 sentences

file = open("Summary.txt","w")
for sentence in summary:
	file.write(str(sentence))
file.close()

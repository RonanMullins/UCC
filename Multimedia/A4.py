'''
The word frequency approach
• using word frequencies within each a sliding window of n lines…
    ◦ keep n small < total/10 (depending on your text & document)
        ▪ if that is too tricky to program then just
            • take one line at a time : n=1
                ◦ and give an outline algorithm for n = r, where r = range or round
▪ and if that is too tricky, just
    • concentrate on what you decide are the crises/turning points
    • and count the words manually in that line…
    • clearly sentiment weightings could be added to the significant
      words, for a quick fix, so you know, but not needed as you're
      unlikely to have time, unless already done
• might as well use tf*idf (term_frequency * inverse_doc_frequency)=(tf/df)
    ◦ term frequency = frequency of a word within the context (n lines)
    ◦ divided by the word frequency within the entire document
        ▪ often the inverse-document-frequency is for a corpus of texts, 1 here!

The overall aim is to see how trivial these approaches are in principle, although tedious in
practice because of the large datasets required.
And of course, to correlate turning points with pointed words and phrases…
… which you can do manually if required.

'''
def word_freq ( input_file: str )-> dict:
    try:
        full_dictionary = {}
        line_count = 0

        in_file = open(input_file, "r")
        for line in in_file:
            data = line
            data = data.replace(",","") #remove commas
            data = data.replace("!","") #remove !
            data = data.replace("?","") #remove ?
            data = data.replace("\n"," * ") #every * is a new line
            data = data.lower()
            data = data.strip()
            word_list = data.split(" ")
            freq_dictionary = {}
            
            for word in word_list:

                if word == "*":
                    continue
                    
                if word in freq_dictionary:
                    freq_dictionary[word] += 1
                else:
                    freq_dictionary[word] = 1

                if word in full_dictionary:
                    full_dictionary[word] += 1
                else:
                    full_dictionary[word] = 1

            line_count += 1
            print("Line " + str(line_count))            
            for k,v in freq_dictionary.items():
                print(k,v)
            print()
        in_file.close() #close file
        print("TOTAL FREQUENCIES")
        for k,v in full_dictionary.items():
                print(k,v)
        # return full_dictionary
        return
        
    except Exception as e:
        return "Oops " + str(e)

print(word_freq("MM/screenplay.txt"))
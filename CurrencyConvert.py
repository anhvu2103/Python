#Anh Vu
#prof. Wright - Python Programming
#Currency Converter
#1 dollar = 0.93 euro
#1 dollar = 0.81 pound

def main():
    euro = 0 #hold euro values converting
    pound = 0 #hold pound values after converting
    store_dollar_data = 0  #hold dollar value read from line in input file 
    input_file = open('test.txt', 'r')
    with open ("output.txt","w") as output_file:
        for line in input_file:
            store_dollar_data = (float(line)) #make string into float.
            #i decided to make float because i get bad converting result
            #using integer
            
            euro = (float (line))*0.926075 #convert to euro, rate of May 7th
            pound = (float (line))*0.808661 #convert to pound, rate of May 7th
            
            #formatting results
            dollar_nice = '{:7,.2f}'.format(store_dollar_data)
            euro_nice = '{:7,.2f}'.format(euro)
            pound_nice = '{:7,.2f}'.format(pound)
            
            #print with good format
            print('$', (str(dollar_nice)),
                  '\u20AC',(str(euro_nice)),
                  '\u00A3', (str(pound_nice)) )
            
            #convert to string to do output file
            dollarstr = '$' + (str (dollar_nice))
            eurostr = '\u20AC' + (str (euro_nice))
            poundstr = '\u00A3' + (str (pound_nice))
            

            outstring = dollarstr + " , " + eurostr + " , " + poundstr + '\n'
            output_file.write(outstring)
         
main()

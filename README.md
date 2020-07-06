# Whatsapp-Parser
Parser for experted Whatsapp text conversation files

This code is the programming equivalent of a lemma. It's intended to input an exported file of a WhatsApp conversation and parse it into a pandas dataframe.
It inputs a text file (ANSI format because I had issues with UTF8)

If you desire then afterward the dataframe can be saved into a csv file with the following code.
  whatsapp_data.to_csv(r'WhatsApp_Conversation_Parsed.csv', index = False)

Feel free to remove any and all of the print statements. I just used them to keep track of how things were going.

To do:

  1) Tighten up the code
  
  2) Check the script against multiple different whatsapp files
  
  3) Find way to make it work with UTF8
 
The ultimate goal is to use this code in the creation of other more interesting analyses.

-#-#-#-#-#-#-#-#-
<p>
  This is my own work and code.
  
  I offer sincere appreciation to the many people on stackoverflow whose answers and ideas contributed to and helped debug the final product.
  
  If you choose to use any significant chunk of this script in your own program(s) then I would request that you include an attribution to me.
<p>
-#-#-#-#-#-#-#-#-

# WordListGen
General Purpose:
WordListGen is a program designed to assist a user in creating wordlists that may
be used with Hashcat - the Kali-Linux Password Cracking Utility. A user user can choose 
to combine up to three lists of words together to form a master wordlist which will have all potential combinations of those words. A numeric value
can also be concatenated to the wordlist as either a suffix or a prefix. This is determined by a range which is set by the user.
The numeric value can be placed at the beginning or end of the concatenated words. A user must
enter the absolute path of each wordlist in the order that they should be concatenated.

The "Example" folder within this repository contains two sample wordlists along with an example of the potential output after using the program. It also contains a single image which includes the command used to run the program and the input used to generate the example wordlist.txt file. 

Structure of Wordlists passed to the program:
The program will need the wordlists passed to it to have an individual word per line, ie:

this
is
an
example
word list

Note: In the above example, the whole string of "word list", including the space, will be used.

Where will I find my word list?
The program will save the output to a file; a user can elect to either pass a custom filename as an argument with the command, for instance "python3 ./WordListGen.py outfile.txt" where outfile.txt will be the resulting file, or the user can elect to pass no arguments in which case a default file by the name of "wordlist.txt" will be produced. 

Downloading the program:
This can be completed by using the "git clone" command along with the provided URL or the Download zip function, both of which are to be found through the green "download Code" button on the repository. 

  Using git clone:
    git clone https://github.com/Flipswxtch/WordListGen.git
    cd WordListGen
    cd Program
    chmod 764 WordListGen.py
    The program is now ready to be used.

  Using Download Zip:
    Download the zip file selecting the desired location.
    Navigate to the directory in the terminal where the zip file was saved.
    unzip WordListGen-main.zip
    cd WordListGen-main
    cd Program
    chmod 754 WordListGen.py
    The program is now ready to be used.

How to use the program:
The program can be used from the terminal with the following command: 
python3 ./WordListGen.py (filename)

Note: filename is optional and is discussed above in the "Where will I find my word list?" section above.

Once running, the program will verbosely prompt the user for input in order to acquire the desired output. The following prompts for user input are currently used (note:some prompts will not be required depending on options chosen):

1) Please enter the number of wordlists you would like to combine:
The input allowed here is either 1, 2, or 3. More than 3 word lists is not supported at this time.

2) Please provide the absolute path to the first wordlist:
3) Please provide the absolute path to the second wordlist:
4) Please provide the absolute path to the third wordlist:
A user will only be prompted to enter a path for the amount of wordlists they selected from question #1. As stated in the prompts themselves, type in the absolute path!

5) Would you like to concatenate numeric values to the word(s), Y/N?
A user can elect to concatenate a range of numbers to all generated word combinations. An answer of 'y' or 'n' is required to proceed.

6) Where would you like to concatenate the numbers? Please enter 'beginning' or 'end':
This question determines where the numbers should be concatenated. Should they be a prefix or a suffix? The input must match 'beginning' or 'end' exactly. This prompt will not show if a user has elected to not concatenate numbers to the words.

7) Please enter the starting value of the numeric range:
This prompt requires an integer as input. The number entered here will be the first number concatenated to each combination of words. This is also not asked if the user entered 'n' for question #5.

8) Please enter the ending value of the numeric range:
This prompt requires an integer as input. The number entered here will be the last number concatenated to each combination of words. This is not asked if the user entered 'n' for question #5.

9) Does the pin need to contain preceeding zeroes, Y/N? Example: 001, 002, 003:
The required input is either 'y' or 'n'. The amount of zeroes that preceed the number is directly correlated to the ending range value in question #8. The above output may not accurately represent the options you have chosen.

Once all questions have been answered, a line of text saying "Generating your wordlist now..." is printed to the screen. After the wordlist has been completed, the program will let you know the wordlist has been generated and the program will exit. 

The output file will be located within the directory of the program itself. 

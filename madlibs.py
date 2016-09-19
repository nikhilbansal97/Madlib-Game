levels=["beginner","normal","intermediate","expert"]
string=["HTML stands for _1_. It is used to build basic _2_ of webpage._3_ is used to enhance the appearance of webpage.HTML files are saved with _4_ extention","len function is use to get the _1_ of the string or list._2_ function is used to transfrom string into list._3_ function is used to transform the list into single string._4_ language is used to make webpage dynamic.",
"Inside _1_ HTML tag we put the JavaScript._2_ tag besides <i> is used to make the font italics._3_ tag is used to make a vertical line in html.Full form of css is _4_.",""]
answers=[["hyper text markup language","structure","css",".html"],["length","split","join","java script"],["script","em","hr","cascading style sheets"]]
print "\t"*5+"Welcome to MadLibs Game!!\n"
print "\t"*4+"1.beginner\t2.normal\t\t3.interediate\t\t4.expert\n"

def replace(index,element,string):
    string=string.replace("_"+str(element+1)+"_",answers[index][element])
    return string

def madlib_process(index,string):
    print string
    i=1
    while i<5:
        blank=raw_input("What is answer for blank "+str(i)+" ").lower()
        if blank==answers[index][i-1]:
            string = replace(index,i-1,string)
            print string
            i=i+1
        else:
            print "WRONG ANSWER! What is answer for blank "+str(i)
        

def level_check(level,levels):
    index=0
    while index<len(levels):
        if levels[index]==level:
            madlib_process(index,string[index])
        index+=1
        
def play_madlibs():
    level=raw_input("Please choose your level : ").lower()
    level_check(level,levels)
    user_input=raw_input("Enter yes if you want to play again or enter no to quit ")
    if user_input=="yes":
        print "\n"
        play_madlibs()
    else:
        print "ThankYou for playing"

play_madlibs()

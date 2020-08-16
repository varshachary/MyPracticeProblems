"""Consider the following:

A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

The characters in  are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .

Input Format

The first line contains a single string denoting .
The second line contains an integer, , denoting the length of each subsegment."""
#Hackerrank

def merge_the_tools(string, k):
   for i in range(0,len(string), k):
        #slice string upto k characters
        line = string[i:i+k]
        seen = set()
        for i in line:
            #only print if we haven't already seen this character
            if i not in seen:
                print(i,end="")
                seen.add(i)
        #prints a new line
        print()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

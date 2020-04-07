#include <iostream>
#include <stdlib.h>
#include <string>
#include <ctype.h>
#include <vector>

using namespace std;


/**
* Program : This programme translates the text from English Language to the Japanese Language.
* There is no restriction on the size of the text (i.e. text length). The only restriction is
* that the text has to be alphabets (from 'A' to 'Z' - in upper or lower case), but no numbers
* or special characters please... the programme can be improve to incorporate this (may be next
* time) :). Thank you and Enjoy.
*
* @Author - Anay Chopade
* @Date - 01-Apr-2020
*
**/
void clearScreen()
{
    cout << "\n\n";
    system("pause");
    system("CLS");
}

void letterConversion(string name)
{
    vector <string> japaneseName;
    for(int i = 0; i < name.length(); i++)
    {
        switch(toupper(name[i]))
        {
            case 'A':
                japaneseName.push_back("ka");
                break;
            case 'B':
                japaneseName.push_back("tu");
                break;
            case 'C':
                japaneseName.push_back("mi");
                break;
            case 'D':
                japaneseName.push_back("te");
                break;
            case 'E':
                japaneseName.push_back("ku");
                break;
            case 'F':
                japaneseName.push_back("lu");
                break;
            case 'G':
                japaneseName.push_back("ji");
                break;
            case 'H':
                japaneseName.push_back("ri");
                break;
            case 'I':
                japaneseName.push_back("ki");
                break;
            case 'J':
                japaneseName.push_back("zu");
                break;
            case 'K':
                japaneseName.push_back("me");
                break;
            case 'L':
                japaneseName.push_back("ta");
                break;
            case 'M':
                japaneseName.push_back("rin");
                break;
            case 'N':
                japaneseName.push_back("to");
                break;
            case 'O':
                japaneseName.push_back("mo");
                break;
            case 'P':
                japaneseName.push_back("no");
                break;
            case 'Q':
                japaneseName.push_back("ke");
                break;
            case 'R':
                japaneseName.push_back("shi");
                break;
            case 'S':
                japaneseName.push_back("ari");
                break;
            case 'T':
                japaneseName.push_back("chi");
                break;
            case 'U':
                japaneseName.push_back("do");
                break;
            case 'V':
                japaneseName.push_back("ru");
                break;
            case 'W':
                japaneseName.push_back("mei");
                break;
            case 'X':
                japaneseName.push_back("na");
                break;
            case 'Y':
                japaneseName.push_back("fu");
                    break;
            case 'Z':
                japaneseName.push_back("zi");
                break;
            default :
                break;
        }
    }
    for(int i = 0; i < name.length(); i++)
    {
        cout << japaneseName[i];
    }
int main()
{
    string englishName = "";

    system("color F3");
    cout << "----------------------------------------------------------------------------------" << endl;
    cout << "************************ENGLISH TO JAPANESE NAME CONVERTER************************" << endl;
    cout << "----------------------------------------------------------------------------------" << endl;
    cout << "\n\nThis is a program that allows you to enter any name and will give the Japanese \nequivalence of the input..." << endl;
    //clearScreen();
    //cout << "----------------------------------------------------------------------------------" << endl;
    //cout << "************************ENGLISH TO JAPANESE NAME CONVERTER************************" << endl;
    //cout << "----------------------------------------------------------------------------------" << endl;
    cout << "\n\nPlease enter your name : ";
    while(getline(cin, englishName))
    {
        cout<<endl;
        cout << "----------------------------------------------------------------------------------" << endl;
        cout << "******* RESULT ******************" << endl;
        cout << "----------------------------------------------------------------------------------" << endl;
        cout << "\nYour English name is : " << englishName << endl;
        cout << "----------------------------------------------------------------------------------" << endl;
        cout << "\nYour Japanese name is : ";
        letterConversion(englishName);
        cout << "\n----------------------------------------------------------------------------------" << endl;
        cout << "Enter another name or press Ctrl-Z to end the program : ";
    }
}

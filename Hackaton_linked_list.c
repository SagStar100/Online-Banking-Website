#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct personalinfo
{
    char numbers[50];
    char letters[50];
    char ssn[50];
    char name[20];
};
struct personalinfo ID;

struct credit
{
    int score;
};
struct credit credit_update;

struct deposit
{
    struct personalinfo value;
    double balance;
    struct deposit *next;
};
struct deposit adding;
struct deposit *head = NULL;
struct withdrawal
{
    struct personalinfo value;
    double wid_balance;
};
struct type
{
    char type_of_account[30];
};
struct type account_type;
int main()
{
    // fflush(stdin);
    printf("Enter the name to be on your account:");
    scanf("%s", ID.name);
    printf("Enter a password starting with numbers: ");
    scanf(" %s", ID.numbers);
    printf("Enter a password with remaining letters: ");
    scanf(" %s", ID.letters);
    printf("New pasword combined:\n %s%s", ID.numbers, ID.letters);
    printf("\nEnter your SSN value: ");
    scanf(" %s", ID.ssn);
    printf("Enter your credit score: ");
    scanf(" %d", &credit_update.score);
    if (credit_update.score > 690 || credit_update.score > 800 && credit_update.score < 850)
    {
        printf("You are doing great with your credit score !!");
    }
    else
    {
        printf("Here are some tips to help improve your credit score:\n");
        printf("A. Keep a budget and stop uneccesary spendings\n");
        printf("B. cut down on exntertainment and other costly vacation trips\n");
        printf("C. Ask for a free consultation to go over financial planning");
    }
    int total = 0;
    printf("\nEnter a deposit balance of atleast $25\n");
    scanf("%lf", &adding.balance);
    if (adding.balance >= 25)
    {
        printf("Balance added-(new amount): $%.2f", adding.balance);
    }
    else
    {
        printf("Insuffiencent funds please add more to continue inital account set up");
        exit(EXIT_FAILURE);
    }
    char values[50], Letter_value[50], social[50], name[20];
    int credit_score;
    // coverting each value to an array:
    strcpy(values, ID.numbers);
    strcpy(social, ID.ssn);
    credit_score = credit_update.score;
    strcpy(Letter_value, ID.letters);
    strcpy(name, ID.name);
    printf("Summary of account creation: ");
    printf("Name:%s\n", name);
    printf("Newly created Password:%s%s\n", values, Letter_value);
    printf("SSN:%s\n", social);
    printf("credit_score:%d\n", credit_score);
    printf("balance:$%.2f\n", adding.balance);
}

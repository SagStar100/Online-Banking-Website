#include <iostream>
#include <conio.h>

using namespace std;

struct Cuenta {
	char first[30];
	char second[30];
	char email[30];
	int dob;
	char gender[30];
	char ethnicity[30];
	float starting;
} c1;

int main() {
	
	int opc;
	
	cout<<"\t Home Page"<<endl;
	cout<<"1. Create Account: "<<endl;
	cout<<"2. Login: "<<endl;
	cout<<"3. Exit: "<<endl;
	cout<<"Option: "<<endl;
	cin>>opc;
	
	switch(opc){
		case 1 :
			fflush(stdin);
			cout<<"First Name: ";
			cin.getline(c1.first, 30, '\n');
			cout<<"Last Name: ";
			cin.getline(c1.second, 30, '\n');
			cout<<"E-mail: ";
			cin.getline(c1.email, 30, '\n');
			cout<<"Date of Birth: ";
			cin>>c1.dob;
			fflush(stdin);
			cout<<"Gender: ";
			cin.getline(c1.gender, 30, '\n');
			cout<<"Ethnicity: ";
			cin.getline(c1.ethnicity, 30, '\n');
			cout<<"Starting balance: ";
			cin>>c1.starting;
			cout<<"Thank you "<<c1.first<<", for creating an account. Please check the confirmation mail sent to "<<c1.email<<". Your starting balance is "<<c1.starting;

			break;
	}
	
	
	
	getch();
	return 0;
}
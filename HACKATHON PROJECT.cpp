#include <iostream>
#include <conio.h>

using namespace std;

void cajero();

int opc;

int main() {
	int money=0;
	float extra, retire;
	
	cout<<"How much money do you have? ";cin>>money;
	
	cajero();
	
	switch(opc){
		case 1:
			cout<<"How much money would you like to deposit: ";cin>>extra;
			money= money+extra;
			cout<<"Money in account: "<<money;break;
		case 2:
			cout<<"How much money would you like to withdraw: ";cin>>retire;
			if(retire > money ){
				cout<<"You do not have enough money";
		}
			else{
				money= money - retire;
				cout<<"Money in account: "<<money;break;
			}
	}
	
	return 0;
}

void cajero() {
	
	cout<<"\t Welcome to your ATM"<<endl;
	cout<<"1. Deposit money. "<<endl;
	cout<<"2. Withdraw money. "<<endl;
	cout<<"3. Account balances."<<endl;
	cout<<"4. Credit score. "<<endl;
	cout<<"4. Exit."<<endl;
	cout<<"Option: "<<endl;
	cin>>opc;
	
}
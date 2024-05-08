#include<iostream>
#include<string>

#define N 10

#define SERIOUS 1
#define NONSERIOUS 2
#define CHECKUP 3

using namespace std;
string Q[N];  //Size of Queue
int Pr[N];   //FOR CATAGORY OF Patient 
int r = -1,f = -1;
void enqueue(string name,int p)//Enqueue function to insert data and its priority in queue
{
	int i;
	
		if(f==-1) 
		{ //if Queue is empty
			f = r = 0;
			Q[r] = name;         //FIRST ENTRY
			Pr[r] = p;           //FIRST ENTRY

		}
	
		else
		 {      //second patient onwards
			for(i = r;i>=f;i--) {
				if(p<Pr[i]) //if priority of the new patient is > exixting patient then shift the existing patient one place right
				{
					Q[i+1] = Q[i];
					Pr[i+1] = Pr[i];	
				}
				else break;
			}
			Q[i+1] = name;
			Pr[i+1] = p;
			r++;
		}	
	

}
void print() { //print the data of Queue
	int i;
	for(i=f;i<=r;i++) {
		cout << "Patient's Name - "<<Q[i];
		switch(Pr[i]) {
			case 3: 
				cout << " Priority - 'Checkup' " << endl;
			break;
			case 2:
				cout << " Priority - 'Non-serious' " << endl;
			break;
			case 1:
				cout << " Priority - 'Serious' " << endl;
			break;
			default:
				cout << "Priority not found" << endl;
		}
	}
}

void dequeue() { //remove the data from front
	if(f == -1) {
		cout<<"Queue is Empty";
	}	
	else {
	cout<<"deleted Element ="<<Q[f]<<endl;
	
		if(f==r) f = r = -1;
		else f++;
	}
}

int main() 
{
	string name;
	int opt,n,i,p;
	cout<<"Enter Your Choice:-"<<endl;
while(1) 
 {
	cout << "\nMenu \n 1)Insert Data in Queue" << endl << " 2)show the Data in Queue " << endl <<" 3)Delete data from the Queue" 
		<< endl <<" 4)Exit"<< endl;
	cin >> opt;
		switch(opt) 
		{
			case 1:
				if(r==N-1)
				{
					cout<<"\nQueue is full";
				}
				else
				{
				cout << "Enter the number of patinent" << endl;
				cin >> n;
				i = 0;
				while(i < n) 
				{
					cout << "Enter your name of the patient : ";
					cin >> name;
				
						cout << "Enter your Prioritys (1: Serious, 2: Non-serious, 3: General checkup) : ";
						cin >> p;
						enqueue(name,p);
							
					i++;
				}//while
				}//else queue not full
			break;
			case 2:
				print();
			break;
			case 3:
				 dequeue();
			break;
			case 4:
				
			exit(0);
			default:
			cout<<"Incorrect Choice"<<endl;

		}
	}
        return 0;
}

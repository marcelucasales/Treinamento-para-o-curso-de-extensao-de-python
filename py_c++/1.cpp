//1 questão
#include<iostream>
using namespace std;
int main(void){
	int a,b,c,maior,menor,med;
	maior = menor = med = 0;
	do{
		cout<<"Digite um numero: "<<endl;
		cin>>a;
		cout<<"Digite outro numero: "<<endl;
		cin>>b;
		cout<<"Digite outro numero: "<<endl;
		cin>>c;
		system("cls");
		if(a==b || a==c || b==c){
			cout<<"Numeros nao podem ser iguais!"<<endl;
		}
	} while(a==b || a==c || b==c);
	if(a>b && a>c){
		maior = a;
		if(b<c){
			menor = b;
			med = c;
		} else{
			menor = c;
			med = b;
		}
	} else if(b>a && b>c){
		maior = b;
		if(a<c){
			menor = a;
			med = c;
		} else{
			menor = c;
			med = a;
		}
	} else if(c>b && c>a){
		maior = c;
		if(b<a){
			menor = b;
			med = a;
		} else{
			menor = a;
			med = b;
		}
	}
	cout<<"Os numeros em ordem decrescente e: "<<maior<<" "<<med<<" "<<menor<<endl;
	return 0;
}

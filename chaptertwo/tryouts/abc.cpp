#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    for(int i=0 ; i<t ; i++){
        int n , c;
        int chestnum[n+1];
        for(int j=0 ; j<n+1;j++){
            chestnum[j]=0;
        }
        cin>>n;
        cin>>c;
        int j=0;
        while(j<n){
            int a ;
            cin>>a;
            if (a<c){
                chestnum[j]=a;
                j++;
            }
            else{
                chestnum[j]=a;
                chestnum[j+1]=c;
                j+=2;
                c=INT16_MAX;
            }
        }
        for(int j=0 ; j<n+1;j++){
            cout<<chestnum[j]<<endl;
        }
    }
}
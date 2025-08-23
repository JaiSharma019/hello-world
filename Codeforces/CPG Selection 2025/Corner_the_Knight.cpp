#include <iostream>

using namespace std;

int main() {
    int t{};
    cin>>t;
    int n_arr[t];
    for (int i=0;i<t;++i) {
        cin>>n_arr[i];
    }
    int feasible_arr[t];
    for (int i=0;i<t;++i) {
        int feasible{0};
        int count{};
        for (int a=0; a<n_arr[i];++a) {
            
            for (int b=count; b<a;++b) {
                if ((a+b)%3==0) {
                    feasible+=2;
                    count+= 1; 
                    break;                  
                }
                
            }
            
        }
        for (int a=0;a<n_arr[i];++a) {
            if (a%3==0) {
                    feasible+=1;
            }    
            
        }
        feasible_arr[i]=feasible;
    }
    for (int i=0;i<t;++i) {
        cout<<feasible_arr[i]<<endl;
    }
}
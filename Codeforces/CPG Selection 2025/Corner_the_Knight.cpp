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
        
        for (int a=0; a<n_arr[i];++a) {
            if(n_arr[i]%2==0) {
                (n_arr[i]-a)%2==0?feasible+=2:feasible+=1;
            }
            else {
                (n_arr[i]-a)%2==0?feasible+=1:feasible+=2;
            }
            
            
            
        }
           
            
        
        feasible_arr[i]=feasible;
    }
    for (int i=0;i<t;++i) {
        cout<<feasible_arr[i]<<endl;
    }
}
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

const long long MOD {998244353};
int F(int k, int arr[], int size) {
    int count{};
    for (int i=0;i<size;++i) {
        if (arr[i]%k==0) {
            count += 1;
        }
    }
    return count;
}

int G(int k, int arr[], int size) {
    int count{};
    for (int i=0;i<size;++i) {
        if (k%arr[i]==0) {
            count += 1;
        }
    }
    return count;
}

long long sum(int arr[], int size) {
    int max{arr[size-1]};
    long long answer{};

    for (int m=1;m<=max;++m) {
        
        vector <int> factors;
        for (int i=1;i<=sqrt(m);++i) {
            if (m%i==0) {
                factors.push_back(i);
                if (i!=m/i) {
                    factors.push_back(m/i);
            }
        }
    }
    
    for (int k:factors) {
        answer = (answer + (1LL*m*m*F(k, arr, size)*G(m/k, arr, size)%MOD)%MOD);    
    }
    }
    return answer;
}

int main() {
    int n{};
    cin>>n;
    int A[n];
    for (int i=0;i<n;++i) {
        cin>>A[i];
    }
    sort(A, A+n);
    long int ans = sum(A,n);
    cout<<ans<<"\n";
}
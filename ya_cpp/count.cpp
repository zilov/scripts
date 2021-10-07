#include <iostream>
using namespace std;

int last_number() {
    int n, ans;
    cin >> n;
    ans = n % 10;
    cout << ans;
    // put your code here
    return 0;
}

int first_number() {
    int n, ans;
    cin >> n;
    ans = n / 10;
    cout << ans;
    // put your code here
    return 0;
}

int prelast_number() {
    int n, ans;
    cin >> n;
    ans = (n / 10) % 10;
    cout << ans;
    return 0;
}

int numbers_sum() {
    int n, ans;
    cin >> n;
    ans = n % 10 + (n / 10) % 10 + n / 100;
    cout << ans;
    return 0;
}

int next_even() {
    int n, ans;
    cin >> n;
    ans = n + (2 - n % 2);
    cout << ans;
    return 0;
}

int school_tables() {
    int c1, c2, c3, ans;
    cin >> c1 >> c2 >> c3;
    ans = (c1 + (c1 % 2)) / 2 
    + (c2 + (c2 % 2)) / 2 
    + (c3 + (c3 % 2)) / 2;
    cout << ans;
    return 0;
}

int main() {
    school_tables();
    return 0;
}
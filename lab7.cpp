#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

double U(double x, double y, double z)
{
    return (x * exp(-x) - 4 * y - 8 * z) / 5;//выраизили y''
}
double V(double z)
{
    return z;//z=y'
}

double Houna_Y_(double x, double y, double z, double h)//метод Хойна для y
{
    double k1 = V(z);
    double k2 = V(z + U(x, y, z) * h / 2);
    return y + h * (k1 + 2 * k2) / 6;
}

double Houna_Z_(double x, double y, double z, double h)//метод Хойна для z=y'
{
    double q1 = U(x, y, z);
    double q2 = U(z + h / 2, y + z * h / 2, z + q1 * h / 2);
    return z + h * (q1 + 2 * q2) / 6;
}

int main()
{
    double a = 0;
    double b = 2;
    double h = 0.01;
    double n = (b - a) / h;
    double X[200];
    double Y[200];
    double Y1[200];
    X[0] = a;
    Y[0] = 1;
    Y1[0] = 0;
    
    ofstream out;
    out.open("7.txt");
    out << X[0] << " " << Y[0] << " " << Y1[0] << endl;
    for (int i = 1; i < n; i++)//само решение задачи Коши
    {
        X[i] = a + i * h;
        Y[i] = Houna_Y_(X[i - 1], Y[i - 1], Y1[i - 1], h);
        Y1[i] = Houna_Z_(X[i - 1], Y[i - 1], Y1[i - 1], h);
        out << X[i] << " " << Y[i] << " " << Y1[i] << endl;
    }
  
    return 0;
   
}

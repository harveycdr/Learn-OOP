#include <iostream>

class MyString
{
private:
    char *i;
    int len;
public:
    template <size_t s>
    MyString(char h[s]){
        this->i = new char[s];
        this->i = h;
        this->len = s;
    }
    void prin(){
        for(int i=0; i<len; i++){
            printf("%c", this->i[i]);
        }
    }
    ~MyString(){}
};

int main(){
    char h[17] = "hello ban ten gi";
    MyString a(h);
    a.prin();
    return 0;
}

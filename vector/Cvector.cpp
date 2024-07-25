#include <iostream>
#include <vector>

template<class T>
class Cvector
{
private:
    Cvector *head;
    Cvector *tail;
    int size;
    T item;
public:
    Cvector() : head(NULL), tail(NULL), size(0) {}
    Cvector(const std::initializer_list<T>& values);
    ~Cvector();
    
    int getSize() {return this->size;}
    bool IsEmpty() {return (this->head==NULL) ? true : false;}
    
    Cvector<T> *makeNode(const T& item);
    
    void append(const T item);
    
    T& operator[](int index);
    Cvector<T>& operator=(Cvector values);
};

template<class T> Cvector<T>::Cvector(const std::initializer_list<T> &values): Cvector()
{
    for (const T& value : values) {
        this->append(value);
    }
}

template<class T> Cvector<T>::~Cvector(){
    if (this->head == NULL) delete this->head; 
    if (this->tail == NULL) delete this->tail; 
}

template<class T> Cvector<T>* Cvector<T>::makeNode(const T &item){
    Cvector<T> *p = new Cvector<T>;
    p->head = NULL;
    p->tail = NULL;
    p->item = item;
    return p;
}

template<class T> void Cvector<T>::append(const T item){
    if(this->IsEmpty()){
        this->head = this->makeNode(item);
        this->tail = this->head;
    }else{
        Cvector<T> *p = this->tail;
        p->head = this->makeNode(item);
        this->tail = p->head;
    }
    this->size += 1;
}

template<class T> T& Cvector<T>::operator[](int index)
{
    int count = 0;
    Cvector<T> *p;
    for(p = this->head; p != NULL; p = p->head){
        if (index == count){break;}
        count += 1;
    }
    return p->item;
}

template<class T> Cvector<T> &Cvector<T>::operator=(Cvector<T> values)
{
    Cvector<T> *new_vector = new Cvector<T>();
    for(Cvector<T> *p = values.head; p != NULL; p = p->head){
        // T item = p->item;
        new_vector->append(p->item);
    }
    this->head = new_vector->head;
    this->tail = new_vector->tail;
    this->size = new_vector->size;
    return *this;
}

template<class T> std::ostream &operator<<(std::ostream &out, Cvector<T> &vector)
{
    if (vector.IsEmpty())
    {
        out<<"Vector is empty!\n";
        return out;
    }
    out<<"(";
    for(int i=0; i < vector.getSize();++i){
        out<<vector[i]<<" ";
    }
    out<<")\n";
    return out;
}

template<class T> std::istream &operator>>(std::istream &in, Cvector<T> &vector)
{
    return in;
}

// int main(){
//     Cvector<int> vec1 = {1,2,3,4,5,6};
//     Cvector<int> vec2 = {1,2,3,4,5,6,7,8,9};
//     Cvector<int> vec3;
//     vec3 = vec2;
//     vec2[2] = 100;

//     std::cout<<vec1;
//     std::cout<<vec2;
//     std::cout<<vec3;

//     return 0;
// }
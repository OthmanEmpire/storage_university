#include <iostream>

class MyClass
{
private:
    int counter = 0;
public:
    void Foo()
    { 
        std::cout << "Foo" << std::endl;    
    }

    void Foo() const
    {
        std::cout << "Foo const" << std::endl;
    }

};

int main(void)
{
    MyClass* cc = new MyClass();
    const MyClass* ccc = cc;
    cc->Foo();
    ccc->Foo();
    delete cc;
    ccc = NULL;
    return 0;
}

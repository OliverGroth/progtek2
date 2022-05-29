#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		int fib(int);
		void set(int);
	private:
		int age;
		int fib_n;
	};
 
Person::Person(int n){
	age = n;
	fib_n = n;
	}
 
int Person::get(){
	return age;
	}

int Person::fib(){
	return _fib(age)
	}

int Person::_fib(int fib_n){
	if fib_n <= 1{
		return fib_n;
	}
	else{
		return(_fib(fib_n-1) + _fib(fib_n-2));
	}
	}
 
void Person::set(int n){
	age = n;
	}


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	int Person_fib(Person* person) {return person->fib();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
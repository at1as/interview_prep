## class, object (and the difference between the two)

A class is a definition, or blue print (like a House that defines common methods). An object is a copy of that object (like one particular house built from that blueprint)

## instantiation

Instantiation is the creation of an instance of a class (i.e., an object created using a class as its blueprint, defining its getters/setters/methods/etc). For `t = Thread.new()`, t is an instance of the Thread class.

## method (as opposed to, say, a C function)

A function is called by name and optionally passed data to operate on. A method is part of a class definition and may gather data contained within the class to operate on.

## virtual method, pure virtual method

JW: TODO

## class/static method
 
A class (or static method) is a method on the class itself rather than one particular object. This can be used to mutate data that is accessible to each instance of the class (like a counter that increments everytime an object is created)

## static/class initializer
 
A static initializer will initialize the class variables/methods, but do not depend on an instance of the class being created to be called. They will be initialized on instantiation, calling a class method directly, assigning a value to a class variable, etc.

## constructor

Called on instantation of class. In Python this is the "__init__(self):" method that runs when a new instance of a class is created. Often the constructor will accept arguments upon object creation.

## destructor/finalizer

A destructor method is invoked automatically when an object is destroyed, in order to reclaim memory.

## superclass or base class

A superclass of X is any class that X inherits from. In `class Car(Vehicle):` Vehicle is a superclass of Car. In `class Vehicle(object):` Python's reserved object class is the superclass of Car.

## subclass or derived class
 
A subclass is class X is any class that inherits from X. In `class Car(Vehicle)`, Car is a subclass of Vehicle

## inheritance
 
A way for a class to inherit characteristics from another parent class. In Python, class "Car(Vehicle)", the Car class would have available to it all the methods available to Vehicle. Vehicle could have a "drive" method that could be inherited by various classes, Car, Motorcycle, etc without having to redefine it for every type of vehicle.

## encapsulation
 
Enclosing data and components into one component (like a class, in which a repeated variable name as another class would not cause unpredictable behavoiour in the application). Can also be used to restrict access to information within a class, as sme languagues require specific getters and setters to get external class information.

## multiple inheritance (and give an example)

A way for classes to inherit characterists from multiple other parent classes. In Python, class "ElectricCar(Vehicle, Car):" would be an electric car that inherits all characteristics from the Vehicle class (and its subclasses) and the Car class (and its subclasses). Calling a method on an instance of ElectricCar first search for it within ElectricVehcile definition, then Vehicle, then Vehicle subclasses, then Car, and then Car subclasses.

## delegation/forwarding

JW: TODO

## composition/aggregation

JW: TODO

## abstract class
 
A class declared as abstract can be subclassed, but not instantiated. It may optionally contain abstract methods which are declared, but must be defined in their subclasses.

## interface/protocol (and different from abstract class)

Similar to an abstract class in that it cannot be instantiated, but all methods are necessarily public, static and final.
 
## method overriding
 
method overriding allows subclasses to override a method in their parent class, with their own implementation

## method overloading (and difference from overriding)

method overloading allows the same method name to defined multiple times with different input parameters. The method called will depend on the number of inputs and data types passed as arguments.

## polymorphism (without resorting to examples)

JW: TODO

## is-a versus has-a relationships (with examples)

Is-a is a property of inheritance (if Honda is a Subclass of Car, then myHonda is a Car). The inheritance chain moves in one direction (a Car definition is not a Honda). Has-a is a property of whether a particular instance of a class references another object 
 
## method signatures (what's included in one)

A method signature is the method name and parameters (both quantity and type).
 
## method visibility (e.g. public/private/other)
 
A public method is accessible from outside of the class (by any subclass or any other class). A protected method is accessible only from a class and its subclasses (denoted as _methodname by convention in Python). A private method is accessible only from within a class (denoted __methodname in python by convention)

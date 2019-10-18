""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Decorators
MetaDescription: Python Decorators BuiltIn and Custom Decorators
MetaKeywords: Python Decorators BuiltIn and Custom Decorators, @STATICMETHOD @CLASSMETHOD
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: python-decorators
---
MARKDOWN """

""" MARKDOWN
# PYTHON DECORATORS
* Decorators are a feature that adds functionality to an existing piece of code.
* They act as a wrapper to an existing function, modifying its behavior.
* Also called as metaprogramming, The wrapping action happens at the compile time.
MARKDOWN """

""" MARKDOWN
## Python Built-in Class Decorators
* Creating Static and class methods
* Python provides a mechanism to call class functions WITHOUT creating a class 
  Object, This is done through 2 Decorators @staticmethods and @classmethod
* Any function 'decorated' with @staticmethod is callable without instantiating 
  the class. It’s definition is immutable via inheritance.
* @staticmethods, is a class decorator, that enables a class function to be 
  used without creating an object, This neither accepts a self (the object instance)
  nor the class is implicitly passed as the first argument. They behave like plain 
  functions except that you can call them from an instance or the class.
* @classmethod is a decorator when used provides a function in a class, 
  as the class object to work on instead of the class instance.
* Enables to call a classes method with out creating an object with classmethods, 
  the class of the object instance is implicitly passed as the first argument 
  instead of self.
MARKDOWN """

# MARKDOWN ```
# Create class with TWO methods
class tinitiate:
    "Class to demonstrate @classmethod and @staticmethod Decorations"

    # Decorated Using the "@classmethod"
    @classmethod
    def class_function(cls, x):
        print(cls, x)

    # Decorated Using the "@staticmethod"
    # No need to pass the "self" (the object instance) for static method
    @staticmethod
    def static_function(x):
        print(x)


# Create an object of the class tinitiate
obj = tinitiate()

# Call the "CLASS_FUNCTION" using the object
obj.class_function("Class Object Test")

# Call the "STATIC_FUNCTION" using the object
obj.static_function("Static Object Test")

# Call the "STATIC_FUNCTION" directly without the object
tinitiate.static_function("Static Test")

# Call the "CLASS_FUNCTION" directly without the object
tinitiate.class_function("Class Test")
# MARKDOWN ```


""" MARKDOWN
## Python Custom Decorators
* 
* 
MARKDOWN """

# MARKDOWN ```


# MARKDOWN ```

tests/						All files, classes and methods must be unit tested and be PEP 8 validated in this folder. 


models/base.py, models/__init__.py		__init__.py inside - with this file, the folder will become a Python package
							This class is the “base” of all other classes in this project.
							The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)



models/rectangle.py				class Rectangle that inherits from Base


models/rectangle.py				Updated the class Rectangle by adding validation of all setter methods and instantiation (id excluded)


models/rectangle.py				Updated the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.


models/rectangle.py				Updated the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character #


models/rectangle.py				Updated the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>


models/rectangle.py				Updated the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y


models/rectangle.py				Updated the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute


models/rectangle.py				Updated the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes


models/square.py					class Square that inherits from Rectangle


models/square.py					Updated the class Square by adding the public getter and setter size


models/square.py					Updated the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes


models/rectangle.py				Updated the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle


models/square.py					Updated the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square


models/base.py					Updated the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries


models/base.py					Updated the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file


models/base.py					Updated the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string


models/base.py					Updated the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set


models/base.py					Updated the class Base by adding the class method def load_from_file(cls): that returns a list of instances


models/						Updated the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV


models/base.py					Updated the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares





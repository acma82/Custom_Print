# Example MarkDown Title Python
## SubTitle
### SubSubTitle
#### Somthing more but bold
##### Too small but bold.....!

1. Hello
2. Hola
3. Bye
4. Adios

* Bullet 1
* Bullet 2
    * SubBullet
    * SubBullet
        * Hello_1
        * Hello_2
            * last one
            * last two

+ Bullet 1
+ Bullet 2
    + SubBullet
    + SubBullet
        + Hello_1
        + Hello_2
            + last one
            + last two


**Bold Text**  <br> ***Bold and Italic***  <br> *italic*

    Hello There. Using the box with just using indentation
    Another line. Here   All spaces are respected.

>> Another way to use a box but without using the indentation <br> Method. This the   Spaces are NOT respected. Neither <br> jumping lines. Use the br to jump lines it means break.

> Another way to use a box but without using the indentation <br> Method. This the   Spaces are NOT respected. Neither <br> jumping lines. Use the br to jump lines it means break.

This is Normal text inside MarkDown. Just as it is in nature.

```
Another type of box but know using a different method. Here the spaces    are respected as well. 
```

<pre>  hello this another box in a different way. </pre>

```python
# Here We can write Python Code. This is a comment.
import enum

class Case(enum.StrEnum):
    UPPER = "upper"
    LOWER = "lower"
    CAPITALIZE = "capitalize"

print(f"The case option: {Case.UPPER}")
```


<span style="color:green"> **I am green Font Bold Using Asterisk** </span>

<span style="color:green"><strong> I am green Font Bold Using Strong </strong> </span>

<span style="background-color:yellow"> <span style="color:blue "> <strong> &nbsp; Hello There! I am yellow background and blue font and adding spaces. &nbsp; </strong> </span> </span>

<span style="background-color:white"> <span style="color:blue "> <strong> &nbsp; Hello My Table 1. &nbsp; </strong> </span> </span>

| Left Header | Center Header | Right Header |
|:------------|:-------------:|-------------:|
|I am left    | I am center   | I am right   |
|Col 0        | Col 1         | Col 3        |
|Row 3        | Row 3         | Row 3        |
|             |               |              |


**<span style="font-size:14px;">[[TOP]](#python)</span>**


[This is an external link to www.genome.gov](https://www.genome.gov/)

[Link Text To Main Title](#example-markdown-title-python)

**Click [Here](PyLO.md) to Open PyLO Class**

**Click [Here To Back](MarkDown_Example.md) to Open MarkDown_Example Document**


<!--- This is a Comment here --->
The comment is over know.....
<!-- Another Comment -->
Good Bye

```python
import enum
#---------------------------------------------------------
#                                                       --
#---------------------------------------------------------
class animal:
    def __init__(self):

        self.dog = "Perro"
        self.cat = "Gato"

        self._poppy = "perrito"


    def print_animals(self):
        print(self.dog)
        print(self.cat)

    @property
    def poppy(self):
        return self._poppy

#---------------------------------------------------------
#                                                       --
#---------------------------------------------------------
class Animal(enum.Enum):
    # This variables are private. They can't be unchangeble.
    BAT = "Bat"
    OWL = "Tecolote"
```


Title: How Is Swift Changing the Way We Learn Programming?
Date: 2015-02-09
Category: Swift
Summary: *Swift*, the new programming language introduced by Apple eight months ago and which already reached the 25th rank of the most used languages list according to [TIOBE’s index](http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html), might be more important than expected for worldwide developer’s community.

*Swift*, the new programming language introduced by Apple eight months ago and which already reached the 25th rank of the most used languages list according to [TIOBE’s index](http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html), might be more important than expected for worldwide developer’s community.

![Swift logo]({attach}swift-logo.png)

Every programmer first looking at a Swift program should be able to understand its logic, firstly because Swift is highly readable but above all because *Swift is not a total revolution*! Yes, it does introduce new concepts and keywords but it does not change things radically.
You can find in Swift a wide common background with almost every object-oriented language like variables, conditions, functions, objects, classes, methods, etc.

As Python, Swift was created with simplicity in mind but is, according to benchmarks, more efficient than its predecessor. Anyway, the debate *Python VS Swift* is not really interesting because both are not designed for same platforms, Swift being totally dedicated to iOS/OS X.

![Benchmark of Swift performances]({attach}swift-performances.png)

For me, the first big breakup that Swift creates with previous C-inspired languages is by not being a superset of it, meaning that *you can’t compile C code in a Swift project* as you could do in C++ or Objective-C for example. Backward compatibility with C, as in every area, is both a good and bad thing; by abandoning C, Swift allows us to start on good foundation.

Swift introduces ease of use for a programmer coming from low-level programming languages as C, but stays highly safe. Safety is, without any doubt, one of the best word to describe Swift.
For exemple, types of variables in Swift are inferred during compilation; we just use the keyword `var` to declare any variable, like in JavaScript. However, unlike JavaScript, Swift allows only one type to be stored in a variable, insuring stable program execution.

Often described as a simple language to have fun with, Swift can not be reduced to that.
Swift provides extremely fast compilation and can handle big amount of data without any problem as it is actually perfect to try a few lines of code too. The mecanism introduced with *Playgrounds*, defined as “a place where people can play”, is really a welcome function which allows to test some code without hundreds of configuration parameters and files.

~~~swift
// Traditional "Hello, world!" program in Swift
println("Hello, world!")
~~~

~~~swift
// Simplest way to use a string!
var name = "Swift"
println("Hello, \(name)")
~~~

As a student often exposed to IT and especially programming, it’s been some years that I am wondering how will programming be taught in the future.
Without really becoming more complex, languages now involve a higher level of abstraction and handle some basic operations for us; we do not have to write functions to create a window, handle keyboard, etc. Instead of this, we have to develop in the framework already provided.
I think we are in a transition period between a inevitable education about low-level computer functionalities and a future world in which people will either work in high-level programming or in conception of low-level links between hardware and software; we have to accept that we can not anymore have a whole knowledge in IT.

Another interesting point is that, as shown amongst others by introduction of M7 motion coprocessor by Apple in iPhone 5S, industry slowly comes back to a CISC architecture, opposed to the current RISC one, meaning concretely communication capabilities between different classic elements (sound card, GPS, etc.) without necessarily going through the CPU runtime.
We can then think that future of programming will be about specialization in one field, as complex as many fields before.

Eventally, even if Swift will probably never be available on other platforms than iOS and OS X, it opens a new way to define what programming languages will look like tomorrow, based on ease and efficiency with both quick playgrounds and bigger programs, all with a simpler syntax without any compromise about safety.

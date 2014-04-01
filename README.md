cython-demo
=============
To run and install this application you will need to do 2 things. 






First, you will need to compile the code. Conveniently, I have provided a makefile to do this for you. 

In case you forgot, just run <code>make</code> from the root directory.

From here, you can import the newly created files into any project.
	Still from inside the src directory, start python (in the terminal). You can import the files now.
	
	
	Alternatively, you can change your directory in idle with 
	<code>import sys, os  
	path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'path to the cython-demo src directory'))  
	if not path in sys.path:  
	    sys.path.insert(1, path)  
	</code>  
	From there you can insert your code as per usual.
	
	If you do not use idle and just run python from the directory containing the code you wish to import, it will automatically see all the files need to import. 
	
To run the tests, just run <code>nosetests</code> from the root directory.

Keep in mind the tests will not complete if you have not used <code>make</code> from the root directory first.

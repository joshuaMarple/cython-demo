cython-demo
=============
To run and install this application you will need to do 2 things. 

First, you need to compile the python code.
	From inside the src directory, run 
	<code>python setup.py build_ext --inplace </code>

From here, you can import the newly created files into any project.
	Still from inside the src directory, start python (in the terminal)
	Alternatively, you can change your directory in idle with 
	<code>import sys, os
	path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'path to the cython-demo src directory'))
	if not path in sys.path:
	    sys.path.insert(1, path)
	</code>
	From there you can insert your code as per usual.

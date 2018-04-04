CC=python

envelope: setup.py
	$(CC) setup.py build_ext --inplace

clean:
	rm envelope.*
	rm -rf build

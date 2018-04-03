CC=python

envelope: setup.py
	$(CC) setup.py build_ext --inplace

clean:
	rm envelope.c envelope.cpython-35m-x86_64-linux-gnu.so
	rm -rf build

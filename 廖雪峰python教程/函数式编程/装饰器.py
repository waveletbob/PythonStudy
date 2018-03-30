def wrapper(f):
	def fun(l):
		f('+91 {} {}'.format(n[-10:-5],n[-5:])for n in l)
	return fun


@wrapper
def sort(l):
	print('\n'.join(sorted(l)))

if __name__ == '__main__':
	l=[raw_input() for _ in xrange(int(raw_input()))]
	sort(l)
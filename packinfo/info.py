import re

class AUTH:

	def __init__(self,author):
		self.__n, self.__m = self._parse(author)

	def _parse(self,s):
		a,m = [],[]
		for i in s.split('\n'):
			t = self.auth_parse.match(i)
			if t:
				a.append(t.group(1))
				m.append(t.group(2))
		return " and ".join(a)," or ".join(m)

	def __get__(self):
		return '\n'.join((' - '.join(a) for a in zip(self.__n.split(" and "), self.__m.split(" or "))))

	@property
	def name(self):
		return self.__n

	@property
	def mail(self):
		return self.__m

class INFO:
	auth_parse = re.compile(r"^\s*([^\s]+)\s+<([^@]+@[^>]+)>\s*$")

	def __init__(self,name,version,desc,author,url):
		self.__n = name
		self.__v = version
		self.__d = desc
		self.__u = url
		self.__a = AUTH(author)


	@property
	def NAME(self):
		return self.__n

	@property
	def VERSION(self):
		return self.__v

	@property
	def DESCR(self):
		return self.__d

	@property
	def AUTHOR(self):
		return self.__a

	@property
	def URL(self):
		return self.__u



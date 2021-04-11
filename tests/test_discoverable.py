from toypipe import Discoverable

class Test_Discoverable:
	def test_subclass1(self):
		class A(Discoverable):
			pass

		class B(A):
			pass

		assert list(Discoverable.childClasses) == [Discoverable, A, B]
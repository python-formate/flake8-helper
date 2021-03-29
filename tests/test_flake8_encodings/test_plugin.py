# stdlib
import ast
from textwrap import dedent

# 3rd party
from coincidence.regressions import AdvancedDataRegressionFixture
from domdf_python_tools.paths import PathPlus
from flake8_encodings import Plugin


def test_plugin(tmp_pathplus: PathPlus, advanced_data_regression: AdvancedDataRegressionFixture):
	example_source = """

	import builtins, io

	source = open("source.py")


	def foo():

		result = builtins.open("source.py")
		result = io.open("source.py")
		result = open("source.py", encoding=None)


	class F:

		def foo():
			result = open("source.py", encoding="utf-8")
			result = open("source.py", mode="rb")

		def read(mode: str = "r"):
			result = open("source.py", mode=mode)

	"""

	(tmp_pathplus / "code.py").write_clean(example_source)
	plugin = Plugin(ast.parse(dedent(example_source)), filename=tmp_pathplus / "code.py")
	advanced_data_regression.check(list("{}:{}: {}".format(*r) for r in plugin.run()))

import nox

@nox.session(name="tests", python="3.8")
def tests(session):
    """Run pytest"""
    session.install("pipenv")
    session.run("pipenv", "install")
    session.run("pytest", "flask/tests")
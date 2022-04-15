from invoke import task


@task
def start(ctx):
    ctx.run("python3 kare/src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest kare/src")

@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest kare/src\ncoverage html")
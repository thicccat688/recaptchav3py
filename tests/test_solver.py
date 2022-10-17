from recaptchav3py.main import RecaptchaV3Solver
from recaptchav3py.constants import CONSTANTS


def test_solver_with_anchor_url():
    solver = RecaptchaV3Solver(
        anchor_url=CONSTANTS.ANCHOR_URL,
    )

    assert isinstance(solver.solve(), str)


def test_solver_without_anchor_url():
    solver = RecaptchaV3Solver()

    assert isinstance(solver.solve(), str)

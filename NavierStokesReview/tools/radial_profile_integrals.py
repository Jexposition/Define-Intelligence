"""Symbolic checks for the radial moment interfaces used by the review.

This tool does not extract a selected Cartesian field from Lean.  It evaluates
profile expressions supplied explicitly by the reviewer, so its output is a
reproducible calculation aid rather than a proof of the selected endpoint.

Example:
    python radial_profile_integrals.py \
      --dv "R*exp(-R)" --ga "R**2*exp(-R)" \
      --V "1+R" --G "R" --debt "1,2,3" --a 1 --b 2
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import sympy as sp


R = sp.symbols("R", real=True)


@dataclass
class FiveRowResult:
    integral_dv_R2: str
    integral_ga_R: str
    pressure_row: str
    angular_row: str
    axial_row: str
    residual_against_debt: list[str]


def expression(text: str) -> sp.Expr:
    """Parse a reviewer-supplied expression with only the radial symbol exposed."""
    return sp.sympify(text, locals={"R": R, "exp": sp.exp, "sqrt": sp.sqrt})


def integrate(expr: sp.Expr, a: sp.Expr, b: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.integrate(expr, (R, a, b)))


def five_rows(
    dv: sp.Expr,
    ga: sp.Expr,
    V: sp.Expr,
    G: sp.Expr,
    debt: tuple[sp.Expr, sp.Expr, sp.Expr],
    a: sp.Expr,
    b: sp.Expr,
) -> FiveRowResult:
    """Evaluate the five `FiveRowRank.FiveRows` integrals on [a,b]."""
    d0, d1, d2 = debt
    rows = (
        integrate(R**2 * dv, a, b),
        integrate(R * ga, a, b),
        integrate((2 * V / R) * dv, a, b),
        integrate(R**2 * (G * dv + V * ga), a, b),
        integrate(2 * R * G * ga - R * V * dv, a, b),
    )
    target = (0, 0, -d0, -d1, -d2)
    residual = [sp.simplify(row - rhs) for row, rhs in zip(rows, target)]
    return FiveRowResult(*(str(row) for row in rows), [str(x) for x in residual])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dv", required=True, help="correction profile dv(R)")
    parser.add_argument("--ga", required=True, help="correction profile ga(R)")
    parser.add_argument("--V", required=True, help="background profile V(R)")
    parser.add_argument("--G", required=True, help="background profile G(R)")
    parser.add_argument("--debt", required=True, help="three comma-separated debt entries")
    parser.add_argument("--a", required=True, help="left endpoint")
    parser.add_argument("--b", required=True, help="right endpoint")
    args = parser.parse_args()

    debt = tuple(expression(part.strip()) for part in args.debt.split(","))
    if len(debt) != 3:
        raise SystemExit("--debt must contain exactly three comma-separated expressions")

    result = five_rows(
        expression(args.dv),
        expression(args.ga),
        expression(args.V),
        expression(args.G),
        debt,  # type: ignore[arg-type]
        expression(args.a),
        expression(args.b),
    )
    print(json.dumps(asdict(result), indent=2))


if __name__ == "__main__":
    main()

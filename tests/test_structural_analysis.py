import os
import runpy
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
BEAM_SCRIPT = REPO_ROOT / "qiita_08_beam" / "qiita_doboku_8.py"
TRUSS_SCRIPT = REPO_ROOT / "qiita_09_truss" / "qiita_doboku_9.py"


def _load_script_namespace(script_path: Path) -> dict:
    previous_backend = os.environ.get("MPLBACKEND")
    os.environ["MPLBACKEND"] = "Agg"
    matplotlib.use("Agg", force=True)
    try:
        namespace = runpy.run_path(
            str(script_path),
            run_name="__test_import__",
        )
    finally:
        plt.close("all")
        if previous_backend is None:
            os.environ.pop("MPLBACKEND", None)
        else:
            os.environ["MPLBACKEND"] = previous_backend
    return namespace


@pytest.fixture(scope="module")
def beam_ns() -> dict:
    return _load_script_namespace(BEAM_SCRIPT)


@pytest.fixture(scope="module")
def truss_ns() -> dict:
    return _load_script_namespace(TRUSS_SCRIPT)


class TestSimplySupportedBeam:
    def test_baseline_script_equilibrium_and_peak_values(
        self, beam_ns: dict
    ) -> None:
        length = beam_ns["L"]
        load = beam_ns["q"]
        young = beam_ns["E"]
        inertia = beam_ns["I"]

        assert beam_ns["RA"] == pytest.approx(load * length / 2)
        assert beam_ns["RB"] == pytest.approx(load * length / 2)
        assert beam_ns["M_max"] == pytest.approx(load * length**2 / 8)
        assert beam_ns["delta_max"] == pytest.approx(
            5 * load * length**4 / (384 * young * inertia)
        )

    def test_beam_response_boundary_and_symmetry(
        self, beam_ns: dict
    ) -> None:
        beam_response = beam_ns["beam_response"]
        max_deflection = beam_ns["max_deflection"]

        length = 12.0
        load = 8_000.0
        young = 210e9
        inertia = 6.5e-5
        x = np.linspace(0.0, length, 401)

        shear, moment, deflection = beam_response(
            L=length,
            q=load,
            E=young,
            I=inertia,
            x=x,
        )

        # Support boundary conditions: zero deflection and zero moment
        assert deflection[0] == pytest.approx(0.0, abs=1e-15)
        assert deflection[-1] == pytest.approx(0.0, abs=1e-15)
        assert moment[0] == pytest.approx(0.0, abs=1e-12)
        assert moment[-1] == pytest.approx(0.0, abs=1e-12)

        # Shear force at supports and zero at midspan
        assert shear[0] == pytest.approx(load * length / 2)
        assert shear[-1] == pytest.approx(-load * length / 2)
        mid = len(x) // 2
        assert shear[mid] == pytest.approx(0.0, abs=1e-10)

        # Maximum moment and deflection at midspan
        assert moment[mid] == pytest.approx(load * length**2 / 8)
        expected_delta = max_deflection(length, load, young, inertia)
        assert expected_delta == pytest.approx(
            5 * load * length**4 / (384 * young * inertia)
        )
        assert deflection[mid] == pytest.approx(expected_delta)

        # Symmetry of bending moment and deflection; antisymmetry of shear
        assert np.allclose(moment, moment[::-1])
        assert np.allclose(deflection, deflection[::-1])
        assert np.allclose(shear, -shear[::-1])

    def test_beam_scaling_laws(self, beam_ns: dict) -> None:
        beam_response = beam_ns["beam_response"]
        max_deflection = beam_ns["max_deflection"]

        length = 10.0
        load = 10_000.0
        young = 200e9
        inertia = 8.0e-5
        x = np.linspace(0.0, length, 101)

        v1, m1, w1 = beam_response(length, load, young, inertia, x)
        v2, m2, w2 = beam_response(length, 2 * load, young, inertia, x)
        _, _, w_stiff = beam_response(length, load, 2 * young, 2 * inertia, x)

        assert np.allclose(v2, 2 * v1)
        assert np.allclose(m2, 2 * m1)
        assert np.allclose(w2, 2 * w1)
        assert np.allclose(w_stiff, w1 / 4)

        d1 = max_deflection(length, load, young, inertia)
        d_double_span = max_deflection(2 * length, load, young, inertia)
        assert d_double_span == pytest.approx(16.0 * d1)


class TestTrussFEM:
    def test_geometry_and_direction_cosines(self, truss_ns: dict) -> None:
        member_length = truss_ns["member_length"]
        direction_cosines = truss_ns["direction_cosines"]
        nodes = truss_ns["nodes"]

        assert member_length(nodes, 0, 1) == pytest.approx(4.0)
        assert member_length(nodes, 0, 2) == pytest.approx(np.sqrt(13.0))
        assert member_length(nodes, 1, 2) == pytest.approx(np.sqrt(13.0))

        cos_ab, sin_ab = direction_cosines(nodes, 0, 1)
        assert cos_ab == pytest.approx(1.0)
        assert sin_ab == pytest.approx(0.0)

        cos_ac, sin_ac = direction_cosines(nodes, 0, 2)
        assert cos_ac == pytest.approx(2.0 / np.sqrt(13.0))
        assert sin_ac == pytest.approx(3.0 / np.sqrt(13.0))
        assert cos_ac**2 + sin_ac**2 == pytest.approx(1.0)

    def test_element_stiffness_matrix_properties(
        self, truss_ns: dict
    ) -> None:
        truss_element_stiffness = truss_ns["truss_element_stiffness"]
        element_dofs = truss_ns["element_dofs"]
        nodes = truss_ns["nodes"]

        assert element_dofs(0, 2) == [0, 1, 4, 5]

        k_ac = truss_element_stiffness(200e9, 1.0e-3, nodes, 0, 2)
        assert k_ac.shape == (4, 4)
        # Symmetry
        assert np.allclose(k_ac, k_ac.T)
        # Rigid-body x and y translations produce zero internal force
        assert np.allclose(k_ac @ np.array([1.0, 0.0, 1.0, 0.0]), 0.0, atol=1e-6)
        assert np.allclose(k_ac @ np.array([0.0, 1.0, 0.0, 1.0]), 0.0, atol=1e-6)
        # Positive semi-definite
        eigvals = np.linalg.eigvalsh(k_ac)
        assert np.min(eigvals) >= -1e-6

    def test_truss_solution_against_analytical_and_equilibrium(
        self, truss_ns: dict
    ) -> None:
        solve_truss = truss_ns["solve_truss"]
        member_axial_force = truss_ns["member_axial_force"]
        nodes = truss_ns["nodes"]
        members = truss_ns["members"]

        young = 200e9
        area = 1.0e-3
        load_p = 10_000.0
        loads = np.zeros(2 * len(nodes))
        loads[5] = -load_p
        fixed_dofs = [0, 1, 3]

        stiffness, disp, reactions = solve_truss(
            nodes=nodes,
            members=members,
            E=young,
            A=area,
            loads=loads,
            fixed_dofs=fixed_dofs,
        )

        # Boundary conditions enforced
        assert disp[0] == 0.0
        assert disp[1] == 0.0
        assert disp[3] == 0.0

        # Global equilibrium K u = f + r
        assert np.allclose(stiffness @ disp - loads, reactions)
        assert reactions[0] == pytest.approx(0.0, abs=1e-7)
        assert reactions[1] == pytest.approx(load_p / 2)
        assert reactions[3] == pytest.approx(load_p / 2)
        assert reactions[1] + reactions[3] - load_p == pytest.approx(0.0, abs=1e-7)
        # Moment equilibrium around support A (x=0, y=0)
        assert 4.0 * reactions[3] - 2.0 * load_p == pytest.approx(0.0, abs=1e-7)

        # Analytical axial forces for 4m base, 3m height triangle truss
        n_ab = member_axial_force(young, area, nodes, 0, 1, disp)
        n_ac = member_axial_force(young, area, nodes, 0, 2, disp)
        n_bc = member_axial_force(young, area, nodes, 1, 2, disp)

        assert n_ab == pytest.approx(load_p / 3)
        assert n_ac == pytest.approx(-load_p * np.sqrt(13.0) / 6)
        assert n_bc == pytest.approx(-load_p * np.sqrt(13.0) / 6)

        # Kinematic check: apex C moves right by half of B's elongation and downward
        assert disp[2] > 0.0
        assert disp[4] == pytest.approx(0.5 * disp[2])
        assert disp[5] < 0.0

        # Baseline script results match solve_truss
        assert np.allclose(disp, truss_ns["u"])
        assert np.allclose(reactions, truss_ns["reactions"])

    def test_truss_linearity_and_determinate_invariance(
        self, truss_ns: dict
    ) -> None:
        solve_truss = truss_ns["solve_truss"]
        member_axial_force = truss_ns["member_axial_force"]
        nodes = truss_ns["nodes"]
        members = truss_ns["members"]
        fixed_dofs = [0, 1, 3]

        loads_base = np.zeros(2 * len(nodes))
        loads_base[5] = -10_000.0

        _, u_base, r_base = solve_truss(
            nodes, members, 200e9, 1.0e-3, loads_base, fixed_dofs
        )
        _, u_double_p, r_double_p = solve_truss(
            nodes, members, 200e9, 1.0e-3, 2 * loads_base, fixed_dofs
        )
        _, u_double_ea, r_double_ea = solve_truss(
            nodes, members, 400e9, 2.0e-3, loads_base, fixed_dofs
        )

        # Load linearity
        assert np.allclose(u_double_p, 2 * u_base)
        assert np.allclose(r_double_p, 2 * r_base)

        # Stiffness inverse scaling & statically determinate force invariance
        assert np.allclose(u_double_ea, u_base / 4)
        assert np.allclose(r_double_ea, r_base)
        for i, j in members:
            n1 = member_axial_force(200e9, 1.0e-3, nodes, i, j, u_base)
            n2 = member_axial_force(400e9, 2.0e-3, nodes, i, j, u_double_ea)
            assert n2 == pytest.approx(n1)
